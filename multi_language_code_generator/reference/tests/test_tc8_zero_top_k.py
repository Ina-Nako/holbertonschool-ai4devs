"""TC8 – top_k_recommendations = 0 raises ValueError."""
import sys, os, pytest
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from recommender import RecommendationEngine

def test_zero_top_k_raises():
    engine = RecommendationEngine()
    with pytest.raises(ValueError, match="top_k_recommendations"):
        engine.recommend(
            users={"alice": ["p1"]},
            target_user="alice",
            top_n_neighbours=1,
            top_k_recommendations=0,
        )
