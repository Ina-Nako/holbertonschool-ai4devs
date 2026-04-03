"""TC3 – top_n_neighbours clamped when only one other user exists."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from recommender import RecommendationEngine

def test_neighbour_count_clamped():
    engine = RecommendationEngine()
    result = engine.recommend(
        users={
            "alice": ["p1", "p2", "p3"],
            "bob":   ["p2", "p3", "p4", "p5"],
        },
        target_user="alice",
        top_n_neighbours=99,
        top_k_recommendations=10,
    )
    ids = [r["product_id"] for r in result["recommendations"]]
    assert "p4" in ids
    assert "p5" in ids
