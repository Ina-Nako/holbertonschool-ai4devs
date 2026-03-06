# Bug Descriptions

---

### Bug 1 – bug1.py

**Intended Behavior**: Return the last `n` items of a list.

**Issue Type**: Off-by-one error.

**Expected Example**:
```
last_n_items([1, 2, 3, 4, 5], 2)  → [4, 5]
last_n_items([1, 2, 3, 4, 5], 5)  → [1, 2, 3, 4, 5]
last_n_items([10, 20, 30], 1)     → [30]
```

**Actual Behavior**: Returns `[5]` instead of `[4, 5]`, and `[2, 3, 4, 5]` instead of `[1, 2, 3, 4, 5]`.

**Why It Deviates**: The slice start index is computed as `len(items) - n + 1`, but the correct expression is `len(items) - n` (or simply `items[-n:]`). The extra `+ 1` shifts the starting position one element too far to the right, so every result is missing its first expected element. The bug is hidden when `n == 1` because both formulas produce the same index.

---

### Bug 2 – bug2.js

**Intended Behavior**: Compute the average of an array of numeric scores.

**Issue Type**: Off-by-one error / runtime exception.

**Expected Example**:
```
averageScore([10, 20, 30])    → 20
averageScore([100])           → 100
averageScore([5, 15, 25, 35]) → 20
```

**Actual Behavior**: Returns `NaN` for every input.

**Why It Deviates**: The `for` loop uses `i <= scores.length` instead of `i < scores.length`. On the final iteration `scores[scores.length]` is `undefined`, and adding `undefined` to a number yields `NaN`, which propagates through the division. Changing `<=` to `<` fixes the boundary.

---

### Bug 3 – bug3.py

**Intended Behavior**: Return the maximum value in a list of numbers.

**Issue Type**: Logical error.

**Expected Example**:
```
find_max([3, 7, 2, 8, 1])    → 8
find_max([-5, -1, -10, -3])  → -1
find_max([0, 0, 0])          → 0
```

**Actual Behavior**: Returns `8` correctly for positive lists, but returns `0` instead of `-1` for all-negative lists.

**Why It Deviates**: `max_val` is initialised to `0`. Every negative number is less than `0`, so the `if num > max_val` check never triggers and the function returns the initial `0` — a value that isn't even in the list. The fix is to initialise `max_val` to `float('-inf')` or to the first element of the list.

---

### Bug 4 – bug4.js

**Intended Behavior**: Remove duplicate values from an array while preserving insertion order.

**Issue Type**: Misuse of data types (object property coercion).

**Expected Example**:
```
removeDuplicates([1, 2, 2, 3, 1])       → [1, 2, 3]
removeDuplicates([false, 0, "", null])   → [false, 0, "", null]
removeDuplicates(["a", "b", "a"])        → ["a", "b"]
```

**Actual Behavior**: The first call returns `[1, 2, 2, 3, 1]` (no duplicates removed). The second call incorrectly conflates falsy values due to object key coercion.

**Why It Deviates**: Two problems combine. First, `seen[arr[i]]` is checked but never set to `true`, so the "already seen" guard never activates and every element is pushed — duplicates included. Second, even if the flag were set, plain-object keys are coerced to strings, meaning distinct values like `false`, `0`, `""`, and `null` can collide (e.g., `String(false) === "false"` while `String(null) === "null"`, but `!seen[0]` is truthy regardless because `"0"` was never stored). Using a `Set` instead of an object and properly adding items to it would fix both issues.

**Why It's Critical**: This bug is especially dangerous because it fails silently — the function returns an array without errors, giving the caller false confidence that duplicates were removed. In production, this could lead to data integrity issues such as duplicate database entries, repeated API calls, or inflated analytics. The type-coercion aspect adds a second layer of risk: even after fixing the missing `seen` update, code that handles mixed types (e.g., form inputs, parsed query parameters) would still produce subtly wrong results that are difficult to trace.

---

### Bug 5 – bug5.py

**Intended Behavior**: Parse a JSON configuration string and extract `timeout`, `retries`, and `verbose` settings into a dictionary.

**Issue Type**: Runtime exception (unhandled errors).

**Expected Example**:
```
parse_config('{"settings": {"timeout": 30, "retries": 3, "verbose": true}}')
  → {'timeout': 30, 'retries': 3, 'verbose': True}
parse_config('{"settings": {"timeout": 30}}')
  → Should handle missing keys gracefully (e.g., return defaults or a clear error)
parse_config('{"settings": timeout: 30}')
  → Should handle malformed JSON gracefully
```

**Actual Behavior**: The first call works, but the second crashes with `KeyError: 'retries'` and the third crashes with `json.JSONDecodeError`.

**Why It Deviates**: The function directly indexes into nested dictionary keys (`config["settings"]["retries"]`, etc.) without checking whether those keys exist. It also calls `json.loads()` without a `try/except` block. Any missing key raises `KeyError`, and any malformed JSON string raises `json.JSONDecodeError`. Adding `try/except` handling and using `dict.get()` with default values would make it robust.

**Why It's Critical**: Configuration parsing sits at the boundary between external input and application logic — it is one of the first things that runs and everything downstream depends on it. An unhandled crash here means the entire application fails to start or aborts mid-operation with no user-friendly message. In a deployed service, malformed or incomplete config files are common (manual edits, partial deployments, environment differences), so this function must be resilient. Without proper error handling, debugging becomes harder because the raw `KeyError` or `JSONDecodeError` traceback gives no context about which config file or field caused the failure.
