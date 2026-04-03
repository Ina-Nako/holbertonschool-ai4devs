"""TC7 – Duplicate product IDs in a purchase list are deduplicated before scoring."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from recommender import RecommendationEngine

def test_duplicate_products_deduplicated():
    engine = RecommendationEngine()
    result_dupes = engine.recommend(
        users={"alice": ["p1", "p1", "p2"], "bob": ["p1", "p2", "p3"]},
        target_user="alice",
        top_n_neighbours=1,
        top_k_recommendations=5,
    )
    result_clean = engine.recommend(
        users={"alice": ["p1", "p2"], "bob": ["p1", "p2", "p3"]},
        target_user="alice",
        top_n_neighbours=1,
        top_k_recommendations=5,
    )
    assert result_dupes["recommendations"] == result_clean["recommendations"]
