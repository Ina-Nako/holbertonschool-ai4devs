"""TC2 – Target user with no purchase history returns empty recommendations."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from recommender import RecommendationEngine

def test_target_user_no_history():
    engine = RecommendationEngine()
    result = engine.recommend(
        users={"alice": ["p1", "p2"], "dave": []},
        target_user="dave",
        top_n_neighbours=1,
        top_k_recommendations=5,
    )
    assert result == {"target_user": "dave", "recommendations": []}
