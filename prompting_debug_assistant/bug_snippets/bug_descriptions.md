# Bug Descriptions

---

## Bug 1 – bug1.py

### Intended Behavior

Return the last `n` items of a list as a new list, preserving order. For example:
- `last_n_items([1, 2, 3, 4, 5], 2)` → `[4, 5]`
- `last_n_items([1, 2, 3, 4, 5], 5)` → `[1, 2, 3, 4, 5]`
- `last_n_items([10, 20, 30], 1)` → `[30]`

### Issue Type

Off-by-one error.

### Notes

The slice uses `len(items) - n + 1` instead of `len(items) - n`. The extra `+ 1` skips one element, so the result is always missing its first expected item. The function fails when `n == len(items)`.

### Edge Cases

- `n == 0` should return an empty list `[]` (already handled by the guard clause).
- `n == len(items)` should return the full list; the bug causes it to drop the first element.
- `n > len(items)` — behaviour is unspecified; the fix `items[-n:]` handles this safely by returning the whole list.

---

## Bug 2 – bug2.js

### Intended Behavior

Compute the arithmetic mean of an array of numeric scores and return it as a number. For example:
- `averageScore([10, 20, 30])` → `20`
- `averageScore([100])` → `100`
- `averageScore([5, 15, 25, 35])` → `20`

### Issue Type

Off-by-one error / runtime exception.

### Notes

The loop condition `i <= scores.length` should be `i < scores.length`. The extra iteration accesses `scores[scores.length]` which is `undefined`, turning the entire sum into `NaN`.

### Edge Cases

- An array with a single element should return that element unchanged.
- An empty array would cause a division by zero (`0 / 0 = NaN`); input validation should guard against this.
- Arrays containing non-numeric values would also produce `NaN` and should be validated at the call site.

---

## Bug 3 – bug3.py

### Intended Behavior

Return the maximum value in a list of numbers, correctly handling all-positive, all-negative, and mixed lists. For example:
- `find_max([3, 7, 2, 8, 1])` → `8`
- `find_max([-5, -1, -10, -3])` → `-1`
- `find_max([0, 0, 0])` → `0`

### Issue Type

Logical error (wrong initial value).

### Notes

`max_val` is initialised to `0` instead of `float('-inf')` or the first element. When all numbers are negative, no element beats `0`, so the function returns a value that isn't even in the list.

### Edge Cases

- All-negative lists return `0` instead of the correct maximum — the most visible failure.
- A list containing only `0` returns `0` correctly by coincidence, masking the bug.
- A single-element list `[x]` returns `x` only if `x > 0`; otherwise it returns `0`.
- An empty list should raise an error or return `None`; the current code returns `0`, which is misleading.

---

## Bug 4 – bug4.js

### Intended Behavior

Return a new array with all duplicate values removed, keeping only the first occurrence of each value and preserving insertion order. For example:
- `removeDuplicates([1, 2, 2, 3, 1])` → `[1, 2, 3]`
- `removeDuplicates([false, 0, "", null])` → `[false, 0, "", null]` (all four are distinct)
- `removeDuplicates(["a", "b", "a"])` → `["a", "b"]`

### Issue Type

Misuse of data types (object property coercion) and missing state update.

### Notes

`seen[arr[i]]` is checked but never set to `true`, so no duplicate is ever detected. Additionally, using a plain object coerces keys to strings, causing distinct values like `false`, `0`, and `""` to collide. A `Set` fixes both issues.

### Edge Cases

- Falsy values (`false`, `0`, `""`, `null`, `undefined`) must each be treated as distinct; object-key coercion silently conflates some of them.
- An empty array `[]` should return `[]` without error.
- An array where every element is the same (e.g., `[5, 5, 5]`) should return `[5]`.

---

## Bug 5 – bug5.py

### Intended Behavior

Parse a JSON configuration string and return a dictionary containing `timeout`, `retries`, and `verbose` settings. For valid input the function should return the extracted values, and for missing keys or malformed JSON it should handle errors gracefully instead of crashing. For example:
- `parse_config('{"settings": {"timeout": 30, "retries": 3, "verbose": true}}')` → `{'timeout': 30, 'retries': 3, 'verbose': True}`
- Partial or missing keys should return safe defaults rather than raising an exception.
- Malformed JSON should return an error indicator rather than propagating a `JSONDecodeError`.

### Issue Type

Runtime exception (unhandled errors).

### Notes

The function accesses nested keys directly without checking they exist and calls `json.loads()` without `try/except`. Missing keys raise `KeyError` and malformed JSON raises `json.JSONDecodeError`. Using `dict.get()` with defaults and wrapping in `try/except` makes it robust.

### Edge Cases

- `settings` key entirely absent from the JSON object causes an immediate `KeyError`.
- Only some sub-keys present (e.g., only `timeout`) causes a `KeyError` for `retries` and `verbose`.
- Completely invalid JSON string (e.g., `"not json"`) raises `json.JSONDecodeError` before any key access.
- An empty string `""` passed as input also raises `json.JSONDecodeError`.

---

## Bug 6 – bug6.c

### Intended Behavior

Reverse a string in place so that the characters appear in the opposite order, modifying the original character array directly. For example:
- `"hello"` → `"olleh"`
- `"abcd"` → `"dcba"`
- `"a"` → `"a"`

### Issue Type

Off-by-one error in loop boundary.

### Notes

The loop condition `i <= len / 2` should be `i < len / 2`. The extra iteration re-swaps the two middle characters back to their original positions, leaving even-length strings only partially reversed.

### Edge Cases

- Even-length strings are incorrectly reversed; the two middle characters end up back in their original positions.
- Odd-length strings appear correct because the extra iteration only swaps the middle character with itself, which is a no-op.
- A single-character string `"a"` is unaffected and returns correctly.
- An empty string `""` results in `len == 0`, so the loop body never executes — correct behaviour by accident.
