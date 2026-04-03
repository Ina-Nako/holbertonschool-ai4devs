# Cross-Language Specification - Product Recommendation Engine

## Algorithm

A collaborative-filtering recommendation engine that suggests products to a user based on purchase history overlap with other users.

Steps:
1. Load the user-product interaction matrix (which users bought which products).
2. For the target user, compute a cosine similarity score against every other user.
3. Select the top-N most similar users (neighbours).
4. Aggregate the products purchased by those neighbours but not yet purchased by the target user.
5. Rank candidate products by weighted purchase frequency (weight = similarity score of the neighbour who bought it).
6. Return the top-K ranked product IDs with their scores.

## Input Format

A JSON object with the following fields:

```json
{
  "users": {
    "<user_id>": ["<product_id>", ...]
  },
  "target_user": "<user_id>",
  "top_n_neighbours": <integer>,
  "top_k_recommendations": <integer>
}
```

- `users`: dictionary mapping each user ID (string) to the list of product IDs (strings) they have purchased.
- `target_user`: the user ID for whom recommendations are generated; must exist in `users`.
- `top_n_neighbours`: how many similar users to consider (positive integer, default 5).
- `top_k_recommendations`: how many products to return (positive integer, default 10).

## Output Format

A JSON object:

```json
{
  "target_user": "<user_id>",
  "recommendations": [
    { "product_id": "<product_id>", "score": <float> },
    ...
  ]
}
```

- `recommendations` is sorted descending by `score`.
- `score` is a float in the range [0.0, 1.0] representing aggregate neighbour similarity weight.
- If no recommendations can be produced, `recommendations` is an empty array.

## Edge Cases

- **Empty user catalogue**: `users` dict is empty or contains only the target user — return empty recommendations.
- **Target user has no purchase history**: cosine similarity is undefined (zero vector); return empty recommendations without error.
- **Target user has purchased everything**: no unseen products exist to recommend; return empty recommendations.
- **All users have identical purchase history**: all similarity scores are 1.0; ranking falls back to alphabetical product ID order for determinism.
- **`top_n_neighbours` exceeds total available users**: clamp neighbour count to the actual number of other users without raising an error.
- **Duplicate product IDs in a user's list**: deduplicate before computing the matrix; treat repeated entries as a single purchase.
- **Non-existent target user**: raise a descriptive `ValueError` / equivalent; do not silently return empty results.
- **`top_k_recommendations` is zero or negative**: raise a `ValueError` with a clear message.

## Test Cases

### Test Case 1 – Typical recommendation
**Input:**
```json
{
  "users": {
    "alice": ["p1", "p2", "p3"],
    "bob":   ["p1", "p2", "p4"],
    "carol": ["p3", "p5"]
  },
  "target_user": "alice",
  "top_n_neighbours": 2,
  "top_k_recommendations": 3
}
```
**Expected output:** `p4` appears in recommendations; `p1`, `p2`, `p3` do not (already purchased by alice).

---

### Test Case 2 – Target user with no purchase history
**Input:**
```json
{
  "users": {
    "alice": ["p1", "p2"],
    "dave":  []
  },
  "target_user": "dave",
  "top_n_neighbours": 1,
  "top_k_recommendations": 5
}
```
**Expected output:** `{ "target_user": "dave", "recommendations": [] }`

---

### Test Case 3 – Only one other user in catalogue
**Input:**
```json
{
  "users": {
    "alice": ["p1", "p2", "p3"],
    "bob":   ["p2", "p3", "p4", "p5"]
  },
  "target_user": "alice",
  "top_n_neighbours": 5,
  "top_k_recommendations": 10
}
```
**Expected output:** recommendations contain `p4` and `p5`; `top_n_neighbours` is clamped to 1 without error.

---

### Test Case 4 – Target user has purchased all available products
**Input:**
```json
{
  "users": {
    "alice": ["p1", "p2", "p3"],
    "bob":   ["p1", "p2"],
    "carol": ["p3"]
  },
  "target_user": "alice",
  "top_n_neighbours": 2,
  "top_k_recommendations": 5
}
```
**Expected output:** `{ "target_user": "alice", "recommendations": [] }`

---

### Test Case 5 – Scores sorted descending
**Input:**
```json
{
  "users": {
    "alice": ["p1", "p2"],
    "bob":   ["p1", "p2", "p3"],
    "carol": ["p1", "p4"],
    "dave":  ["p1", "p2", "p5"]
  },
  "target_user": "alice",
  "top_n_neighbours": 3,
  "top_k_recommendations": 5
}
```
**Expected output:** `p3` and `p5` ranked above `p4` because `bob` and `dave` have higher similarity to `alice` (share two products) than `carol` (shares one product).

---

### Test Case 6 – Non-existent target user
**Input:**
```json
{
  "users": {
    "alice": ["p1"]
  },
  "target_user": "zara",
  "top_n_neighbours": 2,
  "top_k_recommendations": 5
}
```
**Expected output:** Error raised — `"target_user 'zara' not found in users"`.

---

### Test Case 7 – Duplicate products in purchase list
**Input:**
```json
{
  "users": {
    "alice": ["p1", "p1", "p2"],
    "bob":   ["p1", "p2", "p3"]
  },
  "target_user": "alice",
  "top_n_neighbours": 1,
  "top_k_recommendations": 5
}
```
**Expected output:** Duplicate `p1` is deduplicated; `p3` appears in recommendations; same result as if alice's list were `["p1", "p2"]`.
