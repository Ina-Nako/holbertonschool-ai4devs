"""TC12 – Identical purchase histories yield equal scores; tie-breaks alphabetically."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from recommender import RecommendationEngine

def test_identical_histories_alphabetical_order():
    engine = RecommendationEngine()
    result = engine.recommend(
        users={
            "alice": ["p1", "p2"],
            "bob":   ["p1", "p2", "pZ"],
            "carol": ["p1", "p2", "pA"],
        },
        target_user="alice",
        top_n_neighbours=2,
        top_k_recommendations=5,
    )
    ids = [r["product_id"] for r in result["recommendations"]]
    # Both pA and pZ have equal aggregate score; alphabetical order applies
    assert ids.index("pA") < ids.index("pZ")
