"""TC5 – Recommendations are sorted descending by score; higher-similarity neighbours rank first."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from recommender import RecommendationEngine

def test_scores_sorted_descending():
    engine = RecommendationEngine()
    result = engine.recommend(
        users={
            "alice": ["p1", "p2"],
            "bob":   ["p1", "p2", "p3"],
            "carol": ["p1", "p4"],
            "dave":  ["p1", "p2", "p5"],
        },
        target_user="alice",
        top_n_neighbours=3,
        top_k_recommendations=5,
    )
    scores = [r["score"] for r in result["recommendations"]]
    ids = [r["product_id"] for r in result["recommendations"]]
    assert scores == sorted(scores, reverse=True)
    # bob and dave share 2 products with alice; carol shares 1 — so p3/p5 rank above p4
    assert ids.index("p3") < ids.index("p4")
    assert ids.index("p5") < ids.index("p4")
