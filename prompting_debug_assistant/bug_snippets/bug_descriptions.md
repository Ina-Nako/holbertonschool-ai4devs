# Bug Descriptions

## Bug 1 – bug1.py
**Intended Behavior**: Return the last `n` items of a list.
**Issue Type**: Off-by-one error.
**Expected Example**:
```
last_n_items([1, 2, 3, 4, 5], 2)  → [4, 5]
last_n_items([1, 2, 3, 4, 5], 5)  → [1, 2, 3, 4, 5]
```
**Actual Behavior**: Returns `[5]` instead of `[4, 5]`, and `[2, 3, 4, 5]` instead of `[1, 2, 3, 4, 5]`.
**Notes**: The slice `len(items) - n + 1` skips one element. When `n == len(items)`, the function returns all items except the first instead of the full list. For `n == 1`, it works by coincidence.

---

## Bug 2 – bug2.js
**Intended Behavior**: Compute the average of an array of numeric scores.
**Issue Type**: Off-by-one error / runtime exception.
**Expected Example**:
```
averageScore([10, 20, 30])  → 20
averageScore([100])         → 100
```
**Actual Behavior**: Returns `NaN` for every input.
**Notes**: The loop condition `i <= scores.length` iterates one past the last index, reading `undefined`. Adding `undefined` to a number produces `NaN`, so the function always returns `NaN`.

---

## Bug 3 – bug3.py
**Intended Behavior**: Return the maximum value in a list of numbers.
**Issue Type**: Logical error.
**Expected Example**:
```
find_max([3, 7, 2, 8, 1])    → 8
find_max([-5, -1, -10, -3])  → -1
```
**Actual Behavior**: Returns `8` correctly for positive lists, but returns `0` instead of `-1` for all-negative lists.
**Notes**: Initializing `max_val` to `0` instead of the first element (or `-inf`) causes the function to fail for lists containing only negative numbers — it incorrectly returns `0`.

---

## Bug 4 – bug4.js
**Intended Behavior**: Remove duplicate values from an array while preserving insertion order.
**Issue Type**: Misuse of data types (object property coercion).
**Expected Example**:
```
removeDuplicates([1, 2, 2, 3, 1])       → [1, 2, 3]
removeDuplicates([false, 0, "", null])   → [false, 0, "", null]
```
**Actual Behavior**: The first call returns `[1, 2, 2, 3, 1]` (no duplicates removed) because `seen` is never updated. The second call incorrectly conflates falsy values due to object key coercion.
**Notes**: Using a plain object as a set causes all keys to be coerced to strings. Falsy values like `false`, `0`, `""`, and `null` all coerce to falsy or colliding string keys, so the function incorrectly drops or conflates distinct values (e.g., `0` and `false` may share behavior through `!seen[arr[i]]`). Additionally, `seen[arr[i]]` is never set to `true`, so no duplicates are actually tracked.

---

## Bug 5 – bug5.py
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
**Actual Behavior**: Crashes with `KeyError` on missing keys and `json.JSONDecodeError` on invalid JSON.
**Notes**: The function does not handle missing keys (`KeyError`) or malformed JSON (`json.JSONDecodeError`). It crashes on the second and third test cases instead of returning a sensible default or error message.

---

## Bug 6 – bug6.c
**Intended Behavior**: Reverse a string in place so that the characters appear in the opposite order.
**Issue Type**: Off-by-one error in loop boundary.
**Expected Example**:
```
"hello" → "olleh"
"abcd"  → "dcba"
"a"     → "a"
```
**Actual Behavior**: Strings with an even length (e.g., `"abcd"`) are not fully reversed — the two middle characters get swapped back to their original positions, producing `"abcd"` instead of `"dcba"`.
**Notes**: The loop condition `i <= len / 2` causes one extra iteration compared to the correct `i < len / 2`. On that extra pass the middle characters are swapped a second time, undoing the earlier swap.
