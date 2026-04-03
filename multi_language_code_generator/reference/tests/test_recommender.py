"""
Test suite for RecommendationEngine.
Covers all 7 spec test cases + additional edge cases = 12 tests total.
Run with: python -m pytest reference/tests/test_recommender.py -v
"""

import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from recommender import RecommendationEngine


@pytest.fixture
def engine():
    return RecommendationEngine()


# ---------------------------------------------------------------------------
# Test Case 1 – Typical recommendation (spec TC1)
# ---------------------------------------------------------------------------
def test_typical_recommendation(engine):
    result = engine.recommend(
        users={
            "alice": ["p1", "p2", "p3"],
            "bob": ["p1", "p2", "p4"],
            "carol": ["p3", "p5"],
        },
        target_user="alice",
        top_n_neighbours=2,
        top_k_recommendations=3,
    )
    product_ids = [r["product_id"] for r in result["recommendations"]]
    assert result["target_user"] == "alice"
    assert "p4" in product_ids
    assert "p1" not in product_ids
    assert "p2" not in product_ids
    assert "p3" not in product_ids


# ---------------------------------------------------------------------------
# Test Case 2 – Target user with no purchase history (spec TC2)
# ---------------------------------------------------------------------------
def test_target_user_no_history(engine):
    result = engine.recommend(
        users={"alice": ["p1", "p2"], "dave": []},
        target_user="dave",
        top_n_neighbours=1,
        top_k_recommendations=5,
    )
    assert result == {"target_user": "dave", "recommendations": []}


# ---------------------------------------------------------------------------
# Test Case 3 – top_n_neighbours clamped when only one other user (spec TC3)
# ---------------------------------------------------------------------------
def test_neighbour_count_clamped(engine):
    result = engine.recommend(
        users={
            "alice": ["p1", "p2", "p3"],
            "bob": ["p2", "p3", "p4", "p5"],
        },
        target_user="alice",
        top_n_neighbours=99,
        top_k_recommendations=10,
    )
    product_ids = [r["product_id"] for r in result["recommendations"]]
    assert "p4" in product_ids
    assert "p5" in product_ids


# ---------------------------------------------------------------------------
# Test Case 4 – Target user has purchased all available products (spec TC4)
# ---------------------------------------------------------------------------
def test_target_user_purchased_everything(engine):
    result = engine.recommend(
        users={
            "alice": ["p1", "p2", "p3"],
            "bob": ["p1", "p2"],
            "carol": ["p3"],
        },
        target_user="alice",
        top_n_neighbours=2,
        top_k_recommendations=5,
    )
    assert result == {"target_user": "alice", "recommendations": []}


# ---------------------------------------------------------------------------
# Test Case 5 – Scores sorted descending (spec TC5)
# ---------------------------------------------------------------------------
def test_scores_sorted_descending(engine):
    result = engine.recommend(
        users={
            "alice": ["p1", "p2"],
            "bob": ["p1", "p2", "p3"],
            "carol": ["p1", "p4"],
            "dave": ["p1", "p2", "p5"],
        },
        target_user="alice",
        top_n_neighbours=3,
        top_k_recommendations=5,
    )
    recs = result["recommendations"]
    scores = [r["score"] for r in recs]
    assert scores == sorted(scores, reverse=True), "Scores must be in descending order"

    product_ids = [r["product_id"] for r in recs]
    # p3 and p5 come from higher-similarity neighbours (share 2 products)
    # p4 comes from carol (shares 1 product), so p3/p5 rank above p4
    assert product_ids.index("p3") < product_ids.index("p4")
    assert product_ids.index("p5") < product_ids.index("p4")


# ---------------------------------------------------------------------------
# Test Case 6 – Non-existent target user raises ValueError (spec TC6)
# ---------------------------------------------------------------------------
def test_nonexistent_target_user_raises(engine):
    with pytest.raises(ValueError, match="zara"):
        engine.recommend(
            users={"alice": ["p1"]},
            target_user="zara",
            top_n_neighbours=2,
            top_k_recommendations=5,
        )


# ---------------------------------------------------------------------------
# Test Case 7 – Duplicate products in purchase list deduplicated (spec TC7)
# ---------------------------------------------------------------------------
def test_duplicate_products_deduplicated(engine):
    result_with_dupes = engine.recommend(
        users={
            "alice": ["p1", "p1", "p2"],
            "bob": ["p1", "p2", "p3"],
        },
        target_user="alice",
        top_n_neighbours=1,
        top_k_recommendations=5,
    )
    result_clean = engine.recommend(
        users={
            "alice": ["p1", "p2"],
            "bob": ["p1", "p2", "p3"],
        },
        target_user="alice",
        top_n_neighbours=1,
        top_k_recommendations=5,
    )
    assert result_with_dupes["recommendations"] == result_clean["recommendations"]


# ---------------------------------------------------------------------------
# Test Case 8 – top_k_recommendations = 0 raises ValueError
# ---------------------------------------------------------------------------
def test_zero_top_k_raises(engine):
    with pytest.raises(ValueError, match="top_k_recommendations"):
        engine.recommend(
            users={"alice": ["p1"]},
            target_user="alice",
            top_n_neighbours=1,
            top_k_recommendations=0,
        )


# ---------------------------------------------------------------------------
# Test Case 9 – top_k_recommendations negative raises ValueError
# ---------------------------------------------------------------------------
def test_negative_top_k_raises(engine):
    with pytest.raises(ValueError, match="top_k_recommendations"):
        engine.recommend(
            users={"alice": ["p1"]},
            target_user="alice",
            top_n_neighbours=1,
            top_k_recommendations=-3,
        )


# ---------------------------------------------------------------------------
# Test Case 10 – Only target user in catalogue returns empty recommendations
# ---------------------------------------------------------------------------
def test_only_target_user_in_catalogue(engine):
    result = engine.recommend(
        users={"alice": ["p1", "p2"]},
        target_user="alice",
        top_n_neighbours=5,
        top_k_recommendations=5,
    )
    assert result == {"target_user": "alice", "recommendations": []}


# ---------------------------------------------------------------------------
# Test Case 11 – top_k_recommendations limits returned results
# ---------------------------------------------------------------------------
def test_top_k_limits_results(engine):
    result = engine.recommend(
        users={
            "alice": ["p1"],
            "bob": ["p1", "p2", "p3", "p4", "p5", "p6"],
        },
        target_user="alice",
        top_n_neighbours=1,
        top_k_recommendations=3,
    )
    assert len(result["recommendations"]) == 3


# ---------------------------------------------------------------------------
# Test Case 12 – Identical purchase histories yield score 1.0 and alphabetical order
# ---------------------------------------------------------------------------
def test_identical_histories_alphabetical_order(engine):
    result = engine.recommend(
        users={
            "alice": ["p1", "p2"],
            "bob": ["p1", "p2", "pZ"],
            "carol": ["p1", "p2", "pA"],
        },
        target_user="alice",
        top_n_neighbours=2,
        top_k_recommendations=5,
    )
    # Both bob and carol have similarity 1.0 to alice; unseen products are pA and pZ.
    # Both receive equal aggregate score, so alphabetical order applies: pA before pZ.
    product_ids = [r["product_id"] for r in result["recommendations"]]
    assert product_ids.index("pA") < product_ids.index("pZ")
