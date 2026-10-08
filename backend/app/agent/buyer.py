import math
from typing import List, Optional
from sqlalchemy.orm import Session, selectinload

from ..models import Product, Merchant, ProductReview
from ..aws_config import generate_text_embedding
from .intent import IntentMandate
from .scorer import (
    matches_hard_constraints,
    calculate_score_breakdown,
    analyze_product_reviews,
)


def compute_cosine_similarity(vec1: list[float], vec2: list[float]) -> float:
    """Compute cosine similarity between two float vectors."""
    if not vec1 or not vec2 or len(vec1) != len(vec2):
        return 0.5
    dot = sum(a * b for a, b in zip(vec1, vec2))
    norm1 = math.sqrt(sum(a * a for a in vec1))
    norm2 = math.sqrt(sum(b * b for b in vec2))
    if norm1 == 0 or norm2 == 0:
        return 0.5
    sim = dot / (norm1 * norm2)
    # Cosine similarity for normalized text vectors typically sits between 0.3 and 1.0; clamp to [0, 1]
    return max(0.0, min(1.0, float(sim)))


def compute_fallback_lexical_similarity(query: str, product_text: str) -> float:
    """Fallback lexical similarity when vector embeddings are unavailable."""
    if not query:
        return 0.70
    q_words = set(query.lower().replace(",", " ").replace("-", " ").split())
    p_words = set(product_text.lower().replace(",", " ").replace("-", " ").split())
    if not q_words:
        return 0.70
    overlap = len(q_words.intersection(p_words))
    jaccard = overlap / len(q_words)
    return min(1.0, max(0.40, 0.40 + jaccard * 0.60))


def discover_products(
    db: Session,
    mandate: IntentMandate,
):
    query_text = (mandate.raw_query or f"{mandate.category or ''} {mandate.attributes.get('other') or ''}").strip()
    query_vec = None
    if query_text:
        query_vec = generate_text_embedding(query_text)

    # Load products joined with merchant and reviews
    products = (
        db.query(Product)
        .join(Merchant)
        .options(selectinload(Product.reviews))
        .all()
    )

    candidates = []

    for product in products:
        merchant = product.merchant
        prod_reviews = getattr(product, "reviews", [])

        # Calculate semantic similarity via pgvector embedding or fallback
        if query_vec is not None and product.embedding is not None:
            semantic_sim = compute_cosine_similarity(query_vec, product.embedding)
        else:
            prod_summary = f"{product.title} {product.attributes.get('brand', '')} {product.attributes.get('category', '')} {' '.join(str(c) for c in product.attributes.get('color', [])) if isinstance(product.attributes.get('color'), list) else ''}"
            semantic_sim = compute_fallback_lexical_similarity(query_text, prod_summary)

        matches, hard_explanation = matches_hard_constraints(
            product=product,
            budget_max=mandate.budget_max,
            size=mandate.size,
            delivery_by=mandate.delivery_by,
            category=mandate.category,
            semantic_similarity=semantic_sim,
        )

        score = None
        breakdown = None
        sentiment_summary = analyze_product_reviews(prod_reviews)

        if matches:
            score, breakdown = calculate_score_breakdown(
                product=product,
                merchant_rating=merchant.rating,
                budget_max=mandate.budget_max,
                delivery_by=mandate.delivery_by,
                semantic_similarity=semantic_sim,
                reviews=prod_reviews,
            )
            # Compose explainability summary
            math_explanation = (
                f"Accepted: Score {score:.1f}/100 | "
                f"Semantic: {semantic_sim:.0%} match (+{breakdown['semantic']['points']} pts) | "
                f"Sentiment: {sentiment_summary['positive_ratio']:.0%} positive across {sentiment_summary['total_reviews']} reviews (+{breakdown['sentiment']['points']} pts) | "
                f"Price: ₹{product.price:.0f} (+{breakdown['price']['points']} pts) | "
                f"Merchant: {merchant.name} {merchant.rating}★ (+{breakdown['merchant']['points']} pts) | "
                f"Delivers {product.delivery_eta} (+{breakdown['delivery']['points']} pts)"
            )
            customers_say_snippet = sentiment_summary.get("customers_say") or f"Customers praise its {', '.join(sentiment_summary.get('merits', [])[:2])}."
            explanation = f"Customers say: {customers_say_snippet}"
        else:
            math_explanation = hard_explanation
            explanation = hard_explanation

        candidate = {
            "product_id": product.id,
            "title": product.title,
            "merchant": merchant.name,
            "price": product.price,
            "stock": product.stock,
            "delivery_eta": product.delivery_eta,
            "merchant_rating": merchant.rating,
            "image_url": product.image_url or (product.attributes.get("image_url") if isinstance(product.attributes, dict) else None),
            "attributes": product.attributes,
            "semantic_similarity": round(semantic_sim, 2),
            "sentiment_summary": sentiment_summary,
            "customers_say": sentiment_summary.get("customers_say"),
            "merits": sentiment_summary.get("merits", []),
            "demerits": sentiment_summary.get("demerits", []),
            "aspect_pills": sentiment_summary.get("aspect_pills", []),
            "score_breakdown": breakdown,
            "math_explanation": math_explanation,
            "reviews_sample": [
                {
                    "author": getattr(r, "author", r.get("author") if isinstance(r, dict) else ""),
                    "rating": getattr(r, "rating", r.get("rating") if isinstance(r, dict) else 5.0),
                    "sentiment": getattr(r, "sentiment", r.get("sentiment") if isinstance(r, dict) else "POSITIVE"),
                    "comment": getattr(r, "comment", r.get("comment") if isinstance(r, dict) else ""),
                }
                for r in prod_reviews[:3]
            ],
            "accepted": matches,
            "explanation": explanation,
            "score": score,
        }

        candidates.append(candidate)

    accepted = [
        candidate
        for candidate in candidates
        if candidate["accepted"]
    ]

    accepted.sort(
        key=lambda item: item["score"],
        reverse=True
    )

    return {
        "total_products_considered": len(candidates),
        "matching_products": len(accepted),
        "all_candidates": candidates,
        "ranked_candidates": accepted,
        "best_candidate": (
            accepted[0]
            if accepted
            else None
        ),
    }