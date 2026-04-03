"""TC4 – Target user has purchased all available products; no recommendations."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from recommender import RecommendationEngine

def test_target_user_purchased_everything():
    engine = RecommendationEngine()
    result = engine.recommend(
        users={
            "alice": ["p1", "p2", "p3"],
            "bob":   ["p1", "p2"],
            "carol": ["p3"],
        },
        target_user="alice",
        top_n_neighbours=2,
        top_k_recommendations=5,
    )
    assert result == {"target_user": "alice", "recommendations": []}
