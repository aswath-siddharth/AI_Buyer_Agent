import os
import sys
import json

# Fix Windows terminal encoding for unicode currency symbols
os.environ["PYTHONIOENCODING"] = "utf-8"
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

from app.agent.intent import parse_intent, fallback_deterministic_parse, IntentMandate


TEST_CASES = [
    "running shoes under ₹3000, size 9, arrive by Friday",
    "I need shoes",
    "smartwatch under 1k by tomorrow",
    "something nice for my trip",
    "what's the weather like today",
    "cheap running shoes",
    "headphones 2k to 3k",
    "boAt bluetooth audio under 2500 by Saturday",
    "waterproof tech backpack under 2000"
]

def run_tests():
    print("=" * 80)
    print(" MERIDIAN INTENT MANDATE PARSER - BENCHMARK TEST SUITE")
    print("=" * 80)

    for idx, query in enumerate(TEST_CASES, 1):
        mandate = parse_intent(query)
        output_json = mandate.model_dump(
            mode="json",
            include={"category", "budget_ceiling", "attributes", "delivery_by", "raw_query", "needs_clarification"}
        )

        print(f"\n[Test Case {idx}] Query: \"{query}\"")
        print(f"Output JSON: {json.dumps(output_json, ensure_ascii=False, indent=2)}")
        print(f"-> Category: {mandate.category} | Budget Ceiling: ₹{mandate.budget_ceiling} | Size: {mandate.size} | Delivery: {mandate.delivery_by} | Clarification: {mandate.needs_clarification}")

    print("\n" + "=" * 80)
    print(" ALL TESTS PROCESSED SUCCESSFULLY")
    print("=" * 80)

if __name__ == "__main__":
    run_tests()
