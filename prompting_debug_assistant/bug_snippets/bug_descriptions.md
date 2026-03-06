# Bug Descriptions

---

## Bug 1 – bug1.py

### Intended Behavior

Return the last `n` items of a list.

### Issue Type

Off-by-one error.

### Notes

The slice uses `len(items) - n + 1` instead of `len(items) - n`. The extra `+ 1` skips one element, so the result is always missing its first expected item. The function fails when `n == len(items)`.

---

## Bug 2 – bug2.js

### Intended Behavior

Compute the average of an array of numeric scores.

### Issue Type

Off-by-one error / runtime exception.

### Notes

The loop condition `i <= scores.length` should be `i < scores.length`. The extra iteration accesses `scores[scores.length]` which is `undefined`, turning the entire sum into `NaN`.

---

## Bug 3 – bug3.py

### Intended Behavior

Return the maximum value in a list of numbers.

### Issue Type

Logical error (wrong initial value).

### Notes

`max_val` is initialised to `0` instead of `float('-inf')` or the first element. When all numbers are negative, no element beats `0`, so the function returns a value that isn't even in the list.

---

## Bug 4 – bug4.js

### Intended Behavior

Remove duplicate values from an array while preserving insertion order.

### Issue Type

Misuse of data types (object property coercion) and missing state update.

### Notes

`seen[arr[i]]` is checked but never set to `true`, so no duplicate is ever detected. Additionally, using a plain object coerces keys to strings, causing distinct values like `false`, `0`, and `""` to collide. A `Set` fixes both issues.

---

## Bug 5 – bug5.py

### Intended Behavior

Parse a JSON configuration string and extract `timeout`, `retries`, and `verbose` settings.

### Issue Type

Runtime exception (unhandled errors).

### Notes

The function accesses nested keys directly without checking they exist and calls `json.loads()` without `try/except`. Missing keys raise `KeyError` and malformed JSON raises `json.JSONDecodeError`. Using `dict.get()` with defaults and wrapping in `try/except` makes it robust.

---

## Bug 6 – bug6.c

### Intended Behavior

Reverse a string in place.

### Issue Type

Off-by-one error in loop boundary.

### Notes

The loop condition `i <= len / 2` should be `i < len / 2`. The extra iteration re-swaps the two middle characters back to their original positions, leaving even-length strings only partially reversed.
