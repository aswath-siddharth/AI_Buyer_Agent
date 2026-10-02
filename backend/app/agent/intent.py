import os
import re
import json
from datetime import date, timedelta
from typing import Optional, Any, Dict

from dotenv import load_dotenv
from pydantic import BaseModel, Field, model_validator

try:
    from groq import Groq
except ImportError:
    Groq = None

from ..aws_config import get_bedrock_runtime_client, BEDROCK_MODEL_ID

load_dotenv()

SYSTEM_PROMPT = """You are the Intent Mandate Parser for Meridian, an autonomous shopping agent.

═══════════════════════════════════════════
KNOWLEDGE BASE (from Meridian's merchant catalog)
═══════════════════════════════════════════
Valid categories: running shoes, sneakers, smartwatches, audio (headphones/
earbuds), bags. If the user's request doesn't map to one of these, set 
category to the closest catalog term, or null if no reasonable match exists.

Attribute vocabulary per category:
- running shoes / sneakers -> size (UK/US), color
- smartwatches -> strap size, connectivity (GPS/Bluetooth)
- audio -> form factor (in-ear/over-ear)

Budget normalization:
"3k" / "3 k" / "3000" / "₹3,000"         -> 3000
"under X" / "below X" / "less than X"     -> budget_ceiling = X
"X-Y" / "X to Y"                          -> budget_ceiling = Y (upper bound)
"cheap" / "affordable" (no number given)  -> null (never inferred)

═══════════════════════════════════════════
TASK
═══════════════════════════════════════════
Convert a single user shopping request into a structured IntentMandate JSON 
object. You do not decide whether to buy anything — you only extract what 
the user actually said.

OUTPUT SCHEMA
{
  "category": string | null,
  "budget_ceiling": number | null,
  "attributes": { "size": string | null, "other": string | null },
  "delivery_by": string | null,
  "raw_query": string,
  "needs_clarification": boolean   // true only if category is null
}

═══════════════════════════════════════════
EXTRACTION RULES (priority order)
═══════════════════════════════════════════
1. Extract only what is explicitly stated or unambiguously implied. Never 
   invent a value.
2. If no budget is mentioned, set "budget_ceiling": null. Do NOT default to 
   an assumed price range, even if the user says "cheap" or "affordable."
3. Apply the budget normalization table above for numeric shorthand.
4. Compound constraints must all be captured separately — "under ₹3000 AND 
   arriving by Friday" is two constraints; do not drop or merge either.
5. If ambiguous between two readings, prefer null over guessing.
6. category is the only required field. If it cannot be determined, set 
   "category": null and "needs_clarification": true; leave every other 
   field null and do not attempt catalog matching.
7. If the query has no purchasable intent at all (e.g. "what's the 
   weather"), return all fields null, needs_clarification: false, and 
   raw_query set to the original text.
8. Output ONLY the JSON object — no explanation, no markdown fences, no 
   commentary. If your previous output in this conversation was rejected 
   for invalid JSON, return corrected JSON only, nothing else.

═══════════════════════════════════════════
FEW-SHOT EXAMPLES
═══════════════════════════════════════════
Query: "running shoes under ₹3000, size 9, arrive by Friday"
Output: {"category": "running shoes", "budget_ceiling": 3000, "attributes": {"size": "9", "other": null}, "delivery_by": "Friday", "raw_query": "running shoes under ₹3000, size 9, arrive by Friday", "needs_clarification": false}

Query: "I need shoes"
Output: {"category": "shoes", "budget_ceiling": null, "attributes": {"size": null, "other": null}, "delivery_by": null, "raw_query": "I need shoes", "needs_clarification": false}

Query: "smartwatch under 1k by tomorrow"
Output: {"category": "smartwatch", "budget_ceiling": 1000, "attributes": {"size": null, "other": null}, "delivery_by": "tomorrow", "raw_query": "smartwatch under 1k by tomorrow", "needs_clarification": false}

Query: "something nice for my trip"
Output: {"category": null, "budget_ceiling": null, "attributes": {}, "delivery_by": null, "raw_query": "something nice for my trip", "needs_clarification": true}

Query: "what's the weather like today"
Output: {"category": null, "budget_ceiling": null, "attributes": {}, "delivery_by": null, "raw_query": "what's the weather like today", "needs_clarification": false}
"""


class IntentMandate(BaseModel):
    """
    Trusted structured representation of the user's shopping authorization.
    Conforms strictly to the Meridian IntentMandate schema with full backward-compatible accessors.
    """
    category: Optional[str] = Field(
        default=None,
        description="Closest valid catalog term or user requested category"
    )
    budget_ceiling: Optional[float] = Field(
        default=None,
        description="Maximum budget constraint extracted explicitly from query in INR"
    )
    attributes: Dict[str, Any] = Field(
        default_factory=lambda: {"size": None, "other": None},
        description="Extracted attributes vocabulary (size, color, strap size, etc.)"
    )
    delivery_by: Optional[Any] = Field(
        default=None,
        description="Delivery deadline requirement (string or date)"
    )
    raw_query: str = Field(
        default="",
        description="Original natural language query string"
    )
    needs_clarification: bool = Field(
        default=False,
        description="True only if category is null and user intent requires category clarification"
    )
    max_retries: int = Field(
        default=2,
        ge=0,
        description="Maximum retry attempts on checkout/inventory failure"
    )
    is_greeting: bool = Field(
        default=False,
        description="Whether message was purely conversational/greeting"
    )
    conversational_reply: Optional[str] = Field(
        default=None,
        description="Conversational response if user did not request an immediate purchase"
    )

    @model_validator(mode="before")
    @classmethod
    def normalize_incoming_data(cls, data: Any) -> Any:
        if isinstance(data, dict):
            # Backward-compat: budget_max -> budget_ceiling
            if "budget_max" in data and "budget_ceiling" not in data:
                data["budget_ceiling"] = data["budget_max"]
            elif "budget_ceiling" in data and "budget_max" not in data:
                data["budget_max"] = data["budget_ceiling"]

            # Backward-compat: delivery_deadline -> delivery_by
            if "delivery_deadline" in data and "delivery_by" not in data:
                data["delivery_by"] = data["delivery_deadline"]
            elif "delivery_by" in data and "delivery_deadline" not in data:
                data["delivery_deadline"] = data["delivery_by"]

            # Ensure attributes dict has size & other
            attrs = data.get("attributes")
            if attrs is None or not isinstance(attrs, dict):
                attrs = {}
            if "size" in data and "size" not in attrs and data["size"] is not None:
                attrs["size"] = str(data["size"])
            if "size" not in attrs:
                attrs["size"] = None
            if "other" not in attrs:
                attrs["other"] = None
            data["attributes"] = attrs
        return data

    # Backward compatibility properties & accessors
    @property
    def budget_max(self) -> Optional[float]:
        return self.budget_ceiling

    @budget_max.setter
    def budget_max(self, val: Optional[float]):
        self.budget_ceiling = val

    @property
    def size(self) -> Optional[str]:
        if isinstance(self.attributes, dict):
            return self.attributes.get("size")
        return None

    @size.setter
    def size(self, val: Optional[str]):
        if not isinstance(self.attributes, dict):
            self.attributes = {}
        self.attributes["size"] = str(val) if val is not None else None

    @property
    def delivery_deadline(self) -> Optional[str]:
        if self.delivery_by is not None:
            return str(self.delivery_by)
        return None

    @property
    def categoryLabel(self) -> str:
        if not self.category:
            return "all categories"
        cat = str(self.category).lower()
        if "run" in cat or "shoe" in cat:
            return "running shoes"
        elif "sneak" in cat:
            return "sneakers"
        elif "watch" in cat:
            return "smartwatches"
        elif "audio" in cat or "headphone" in cat or "earbud" in cat:
            return "audio (headphones/earbuds)"
        elif "bag" in cat or "pack" in cat:
            return "bags"
        return self.category


def fallback_deterministic_parse(user_message: str) -> IntentMandate:
    """
    Resilient deterministic fallback parser adhering to all 8 extraction rules
    and the Meridian catalog knowledge base.
    """
    text = user_message.strip()
    lower_text = text.lower()

    # Rule: Greeting check
    greeting_pattern = r"^(hi|hello|hey|greetings|hola|help|what can you do|who are you|hi there)[!.]*$"
    if re.match(greeting_pattern, lower_text):
        return IntentMandate(
            category=None,
            budget_ceiling=None,
            attributes={"size": None, "other": None},
            delivery_by=None,
            raw_query=text,
            needs_clarification=False,
            is_greeting=True,
            conversational_reply=(
                "👋 Hello! I am Meridian, your Autonomous AI Shopping Agent.\n\n"
                "Tell me what you'd like to buy and your constraints, for example:\n"
                "• *'running shoes under ₹3000, size 9, arrive by Friday'*\n"
                "• *'smartwatch under 1k by tomorrow'*\n"
                "• *'Sony bluetooth headphones under ₹3000'*\n"
                "• *'waterproof tech backpack under ₹2000'*\n\n"
                "I enforce strict budget mandates, verify catalog stock across merchants, "
                "and execute authorized payments with single-invoice cryptographic proof!"
            )
        )

    # Rule 7: Non-purchasable check (e.g. weather, general QA, jokes)
    non_purchasable_triggers = [
        "what's the weather", "what is the weather", "weather today", "weather like",
        "tell me a joke", "who is the prime minister", "how are you", "what time is it",
        "calculate", "define ", "meaning of"
    ]
    if any(trigger in lower_text for trigger in non_purchasable_triggers):
        return IntentMandate(
            category=None,
            budget_ceiling=None,
            attributes={},
            delivery_by=None,
            raw_query=text,
            needs_clarification=False,
            is_greeting=False,
            conversational_reply=(
                "I am Meridian, specialized in autonomous commerce across verified merchant catalogs "
                "(running shoes, sneakers, smartwatches, audio, bags). Ask me to find or purchase items for you!"
            )
        )

    # Shopping intent indicator
    shopping_triggers = ["buy", "need", "want", "find", "get", "order", "purchase", "looking for", "shop", "shoes", "shoe", "watch", "headphone", "earbuds", "bag", "sneaker"]
    has_shopping_intent = any(w in lower_text for w in shopping_triggers)

    # Rule 6 & Knowledge Base: Valid category extraction
    category = None
    if any(w in lower_text for w in ["running shoe", "running shoes", "running", "runners", "run shoes"]):
        category = "running shoes"
    elif any(w in lower_text for w in ["sneaker", "sneakers", "streetwear", "casual shoe", "kicks"]):
        category = "sneakers"
    elif any(w in lower_text for w in ["smartwatch", "smartwatches", "smart watch", "fitness tracker", "fitness band", "smart band"]):
        category = "smartwatch"
    elif any(w in lower_text for w in ["audio", "headphone", "headphones", "earbuds", "earbud", "earphone", "earphones", "tws"]):
        category = "audio (headphones/earbuds)"
    elif any(w in lower_text for w in ["bag", "bags", "backpack", "backpacks", "duffel", "sling bag", "travel bag"]):
        category = "bags"
    elif any(w in lower_text for w in ["shoes", "shoe", "footwear"]):
        category = "shoes"
    elif any(w in lower_text for w in ["watch", "watches"]):
        category = "smartwatch"

    # Rule 6: If category cannot be determined
    if category is None:
        # Ambiguous purchasable intent (e.g., "something nice for my trip", "a gift for my brother")
        if any(w in lower_text for w in ["something", "gift", "item", "product", "nice", "for my trip", "surprise"]) or has_shopping_intent:
            return IntentMandate(
                category=None,
                budget_ceiling=None,
                attributes={},
                delivery_by=None,
                raw_query=text,
                needs_clarification=True,
                is_greeting=False,
                conversational_reply="Could you please specify the product category you're looking for? (e.g. running shoes, sneakers, smartwatches, audio, or bags)"
            )
        else:
            # Query has no purchasable intent (Rule 7)
            return IntentMandate(
                category=None,
                budget_ceiling=None,
                attributes={},
                delivery_by=None,
                raw_query=text,
                needs_clarification=False,
                is_greeting=False
            )

    # Rule 2 & 3: Budget Normalization
    budget_ceiling = None

    # Shorthand "1k", "3k", "3 k", "2.5k"
    k_match = re.search(r"(\d+(?:\.\d+)?)\s*k\b", lower_text)
    # Range "2000-3000", "2000 to 3000", "2k-3k", "2k to 3k"
    range_match = re.search(r"(?:₹|rs\.?|inr)?\s*(\d+(?:\.\d+)?k?)\s*(?:-|to)\s*(?:₹|rs\.?|inr)?\s*(\d+(?:\.\d+)?k?)", lower_text)

    if range_match:
        # Upper bound takes precedence (Rule: X-Y -> Y)
        upper_str = range_match.group(2).lower()
        if "k" in upper_str:
            try:
                budget_ceiling = float(upper_str.replace("k", "").strip()) * 1000.0
            except ValueError:
                pass
        else:
            try:
                budget_ceiling = float(upper_str.replace(",", "").strip())
            except ValueError:
                pass
    elif k_match:
        try:
            budget_ceiling = float(k_match.group(1)) * 1000.0
        except ValueError:
            pass
    else:
        # Numeric "under X", "below X", "less than X", "₹3,000", "rs 3000"
        num_match = re.search(r"(?:under|below|less than|within|max|budget|ceiling|limit|rs\.?|₹|inr)\s*(\d+[\d,]*)", lower_text)
        if num_match:
            try:
                val = float(num_match.group(1).replace(",", ""))
                if val > 50:
                    budget_ceiling = val
            except ValueError:
                pass

    # "cheap" / "affordable" without numbers -> budget_ceiling remains None (Rule 2)

    # Attribute vocabulary per category
    size = None
    other = None

    # Size extraction (UK/US/generic numeric)
    size_match = re.search(r"(?:size|sz|uk|us)\s*[:=]?\s*(\d+(?:\.\d+)?)", lower_text)
    if size_match:
        size = size_match.group(1)

    # Color extraction
    color_match = re.search(r"\b(black|white|red|blue|crimson|green|grey|gray|beige|silver|gold)\b", lower_text)
    if color_match:
        other = color_match.group(1)

    # Smartwatches connectivity / strap size
    if category == "smartwatch":
        if "gps" in lower_text:
            other = "GPS"
        elif "bluetooth" in lower_text or "calling" in lower_text:
            other = "Bluetooth"
        strap_match = re.search(r"(\d+(?:\.\d+)?\s*(?:mm|inch|in))\b", lower_text)
        if strap_match:
            size = strap_match.group(1)

    # Audio form factor
    if "audio" in str(category) or "headphone" in str(category):
        if "in-ear" in lower_text or "earbuds" in lower_text or "tws" in lower_text:
            other = "in-ear"
        elif "over-ear" in lower_text or "on-ear" in lower_text or "headphone" in lower_text:
            other = "over-ear"

    # Delivery deadline (Compound constraints - Rule 4)
    delivery_by = None
    if re.search(r"\b(tomo|tomorrow|urgent|1 day|one day)\b", lower_text):
        delivery_by = "tomorrow"
    elif re.search(r"\b(friday|fri)\b", lower_text):
        delivery_by = "Friday"
    elif re.search(r"\b(saturday|sat)\b", lower_text):
        delivery_by = "Saturday"
    elif re.search(r"\b(sunday|sun)\b", lower_text):
        delivery_by = "Sunday"
    elif re.search(r"\b(weekend)\b", lower_text):
        delivery_by = "weekend"
    elif re.search(r"\b(2 day|two day|2 days)\b", lower_text):
        delivery_by = "in 2 days"

    return IntentMandate(
        category=category,
        budget_ceiling=budget_ceiling,
        attributes={"size": size, "other": other},
        delivery_by=delivery_by,
        raw_query=text,
        needs_clarification=False,
        max_retries=2,
        is_greeting=False
    )


def parse_intent(user_message: str) -> IntentMandate:
    """
    Convert natural-language shopping intent into a structured IntentMandate using Amazon Bedrock
    (Meta Llama 3.3 70B: us.meta.llama3-3-70b-instruct-v1:0), with automatic deterministic fallback.
    """
    try:
        bedrock = get_bedrock_runtime_client()

        response = bedrock.converse(
            modelId=BEDROCK_MODEL_ID,
            system=[{"text": SYSTEM_PROMPT}],
            messages=[{"role": "user", "content": [{"text": user_message}]}],
            inferenceConfig={"temperature": 0.0, "maxTokens": 400}
        )

        content = response["output"]["message"]["content"][0]["text"]
        if not content:
            return fallback_deterministic_parse(user_message)

        clean_content = content.strip()
        if clean_content.startswith("```"):
            clean_content = re.sub(r"^```(?:json)?\s*", "", clean_content)
            clean_content = re.sub(r"\s*```$", "", clean_content)

        data = json.loads(clean_content)

        # Parse budget
        budget_ceiling = None
        if data.get("budget_ceiling") is not None:
            try:
                budget_ceiling = float(data["budget_ceiling"])
            except (ValueError, TypeError):
                budget_ceiling = None

        # Parse attributes
        attrs = data.get("attributes")
        if not isinstance(attrs, dict):
            attrs = {}
        size_val = attrs.get("size")
        other_val = attrs.get("other")

        category_val = data.get("category")
        needs_clarification_val = bool(data.get("needs_clarification", category_val is None))

        # Check for greeting or non-purchasable conversation
        is_greeting = False
        greeting_pattern = r"^(hi|hello|hey|greetings|hola|help|what can you do|who are you|hi there)[!.]*$"
        if re.match(greeting_pattern, user_message.lower().strip()):
            is_greeting = True

        return IntentMandate(
            category=category_val,
            budget_ceiling=budget_ceiling,
            attributes={"size": size_val, "other": other_val},
            delivery_by=data.get("delivery_by"),
            raw_query=data.get("raw_query") or user_message,
            needs_clarification=needs_clarification_val,
            max_retries=2,
            is_greeting=is_greeting,
            conversational_reply=None
        )

    except Exception as e:
        print(f"Bedrock parsing notice: {e}. Using deterministic parser.")
        # Gracefully fall back to deterministic parser on network or API latency
        return fallback_deterministic_parse(user_message)
