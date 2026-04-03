"""TC11 – top_k_recommendations correctly limits the number of returned products."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from recommender import RecommendationEngine

def test_top_k_limits_results():
    engine = RecommendationEngine()
    result = engine.recommend(
        users={
            "alice": ["p1"],
            "bob":   ["p1", "p2", "p3", "p4", "p5", "p6"],
        },
        target_user="alice",
        top_n_neighbours=1,
        top_k_recommendations=3,
    )
    assert len(result["recommendations"]) == 3
