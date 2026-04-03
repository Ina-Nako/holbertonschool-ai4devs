"""TC6 – Non-existent target user raises ValueError."""
import sys, os, pytest
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from recommender import RecommendationEngine

def test_nonexistent_target_user_raises():
    engine = RecommendationEngine()
    with pytest.raises(ValueError, match="zara"):
        engine.recommend(
            users={"alice": ["p1"]},
            target_user="zara",
            top_n_neighbours=2,
            top_k_recommendations=5,
        )
