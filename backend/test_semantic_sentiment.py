import os
import sys

os.environ["PYTHONIOENCODING"] = "utf-8"
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

from app.database import SessionLocal
from app.models import Product, ProductReview
from app.agent.intent import IntentMandate
from app.agent.buyer import discover_products
from app.agent.orchestrator import run_buyer_orchestration

db = SessionLocal()
try:
    p_count = db.query(Product).count()
    r_count = db.query(ProductReview).count()
    print(f"Verified Database: {p_count} products, {r_count} reviews in RDS PostgreSQL.")

    # Test 1: Semantic search for cushioned marathon runners under ₹3000
    print("\n" + "=" * 60)
    print("TEST 1: Semantic Search & Sentiment - Cushioned Marathon Shoes")
    print("=" * 60)
    mandate1 = IntentMandate(
        category="running_shoes",
        budget_max=3000.0,
        size="9",
        raw_query="marathon running shoes with responsive shock absorbing cushion under 3000",
    )
    res1 = discover_products(db, mandate1)
    print(f"Total Considered: {res1['total_products_considered']}")
    print(f"Matching Candidates: {res1['matching_products']}")
    print("\nTop 3 Ranked Products:")
    for idx, c in enumerate(res1["ranked_candidates"][:3], 1):
        print(f"{idx}. {c['title']} ({c['merchant']}) - ₹{c['price']:.0f}")
        print(f"   Total Score: {c['score']:.1f}/100")
        print(f"   Semantic Match: {c['semantic_similarity']:.0%}")
        print(f"   Sentiment: {c['sentiment_summary']['sentiment_label']} | Points: {c['sentiment_summary']['sentiment_points']}/30")
        if c['sentiment_summary']['top_pros']:
            print(f"   Pros: {', '.join(c['sentiment_summary']['top_pros'])}")
        if c['sentiment_summary']['top_cons']:
            print(f"   Cons: {', '.join(c['sentiment_summary']['top_cons'])}")
        print(f"   Explanation: {c['explanation']}")
        print()

    # Test 2: Semantic search for tech water-resistant laptop bag
    print("\n" + "=" * 60)
    print("TEST 2: Semantic Search - Tech laptop backpack with rain protection")
    print("=" * 60)
    mandate2 = IntentMandate(
        category="bags",
        budget_max=2500.0,
        raw_query="waterproof commuter tech backpack for 16 inch macbook laptop",
    )
    res2 = discover_products(db, mandate2)
    print(f"Top Bag Pick: {res2['best_candidate']['title'] if res2['best_candidate'] else 'None'}")
    if res2['best_candidate']:
        bc = res2['best_candidate']
        print(f"Price: ₹{bc['price']:.0f} | Semantic Match: {bc['semantic_similarity']:.0%} | Score: {bc['score']}")
        print(f"Sentiment: {bc['sentiment_summary']['sentiment_label']} ({bc['sentiment_summary']['sentiment_points']} pts)")

finally:
    db.close()
