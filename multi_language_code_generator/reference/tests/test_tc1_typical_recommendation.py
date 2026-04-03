"""TC1 – Typical recommendation: p4 appears, already-purchased products do not."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from recommender import RecommendationEngine

def test_typical_recommendation():
    engine = RecommendationEngine()
    result = engine.recommend(
        users={
            "alice": ["p1", "p2", "p3"],
            "bob":   ["p1", "p2", "p4"],
            "carol": ["p3", "p5"],
        },
        target_user="alice",
        top_n_neighbours=2,
        top_k_recommendations=3,
    )
    ids = [r["product_id"] for r in result["recommendations"]]
    assert result["target_user"] == "alice"
    assert "p4" in ids
    assert "p1" not in ids
    assert "p2" not in ids
    assert "p3" not in ids
