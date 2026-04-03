"""
Product Recommendation Engine
Collaborative filtering using cosine similarity.

Spec: multi_language_code_generator/cross_language_spec.md
"""

import math
from typing import Dict, List


class RecommendationEngine:
    """Collaborative-filtering recommendation engine based on cosine similarity."""

    def _build_vectors(
        self, users: Dict[str, List[str]]
    ) -> Dict[str, Dict[str, int]]:
        """Return binary purchase vectors keyed by user then product."""
        return {user: {p: 1 for p in set(products)} for user, products in users.items()}

    def _cosine_similarity(
        self, vec_a: Dict[str, int], vec_b: Dict[str, int]
    ) -> float:
        """Compute cosine similarity between two sparse binary vectors."""
        if not vec_a or not vec_b:
            return 0.0
        dot = sum(vec_a.get(p, 0) * vec_b.get(p, 0) for p in vec_b)
        mag_a = math.sqrt(sum(v * v for v in vec_a.values()))
        mag_b = math.sqrt(sum(v * v for v in vec_b.values()))
        if mag_a == 0.0 or mag_b == 0.0:
            return 0.0
        return dot / (mag_a * mag_b)

    def recommend(
        self,
        users: Dict[str, List[str]],
        target_user: str,
        top_n_neighbours: int = 5,
        top_k_recommendations: int = 10,
    ) -> dict:
        """
        Generate product recommendations for *target_user*.

        Args:
            users: Mapping of user_id -> list of purchased product_ids.
            target_user: User for whom to generate recommendations.
            top_n_neighbours: Number of most-similar users to consider.
            top_k_recommendations: Maximum number of products to return.

        Returns:
            Dict with keys ``target_user`` and ``recommendations`` (list of
            dicts with ``product_id`` and ``score``, sorted descending by score).

        Raises:
            ValueError: If target_user is not in users, or top_k_recommendations
                        is not a positive integer.
        """
        if target_user not in users:
            raise ValueError(f"target_user '{target_user}' not found in users")
        if top_k_recommendations <= 0:
            raise ValueError(
                f"top_k_recommendations must be a positive integer, "
                f"got {top_k_recommendations}"
            )

        # Deduplicate purchase lists
        vectors = self._build_vectors(users)
        target_vec = vectors[target_user]

        # Compute similarity to every other user
        others = {uid: vec for uid, vec in vectors.items() if uid != target_user}
        if not others or not target_vec:
            return {"target_user": target_user, "recommendations": []}

        similarities = {
            uid: self._cosine_similarity(target_vec, vec)
            for uid, vec in others.items()
        }

        # Clamp neighbour count to available users
        n = min(top_n_neighbours, len(others))
        neighbours = sorted(similarities, key=lambda u: (-similarities[u], u))[:n]

        # Aggregate scores for unseen products
        already_purchased = set(target_vec.keys())
        scores: Dict[str, float] = {}
        for uid in neighbours:
            sim = similarities[uid]
            for product in vectors[uid]:
                if product not in already_purchased:
                    scores[product] = scores.get(product, 0.0) + sim

        if not scores:
            return {"target_user": target_user, "recommendations": []}

        # Sort descending by score, then alphabetically for determinism
        ranked = sorted(scores.items(), key=lambda item: (-item[1], item[0]))
        top_k = ranked[:top_k_recommendations]

        return {
            "target_user": target_user,
            "recommendations": [
                {"product_id": pid, "score": round(score, 6)}
                for pid, score in top_k
            ],
        }
