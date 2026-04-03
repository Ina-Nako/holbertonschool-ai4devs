"""TC10 – Only the target user in the catalogue returns empty recommendations."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from recommender import RecommendationEngine

def test_only_target_user_in_catalogue():
    engine = RecommendationEngine()
    result = engine.recommend(
        users={"alice": ["p1", "p2"]},
        target_user="alice",
        top_n_neighbours=5,
        top_k_recommendations=5,
    )
    assert result == {"target_user": "alice", "recommendations": []}
