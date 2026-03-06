# Bug Descriptions

## Bug 1 – bug1.py
**Intended Behavior**: Return the last `n` items of a list.
**Issue Type**: Off-by-one error.
**Notes**: The slice `len(items) - n + 1` skips one element. When `n == len(items)`, the function returns all items except the first instead of the full list. For `n == 1`, it works by coincidence.

## Bug 2 – bug2.js
**Intended Behavior**: Compute the average of an array of numeric scores.
**Issue Type**: Off-by-one error / runtime exception.
**Notes**: The loop condition `i <= scores.length` iterates one past the last index, reading `undefined`. Adding `undefined` to a number produces `NaN`, so the function always returns `NaN`.

## Bug 3 – bug3.py
**Intended Behavior**: Return the maximum value in a list of numbers.
**Issue Type**: Logical error.
**Notes**: Initializing `max_val` to `0` instead of the first element (or `-inf`) causes the function to fail for lists containing only negative numbers — it incorrectly returns `0`.

## Bug 4 – bug4.js
**Intended Behavior**: Remove duplicate values from an array while preserving insertion order.
**Issue Type**: Misuse of data types (object property coercion).
**Notes**: Using a plain object as a set causes all keys to be coerced to strings. Falsy values like `false`, `0`, `""`, and `null` all coerce to falsy or colliding string keys, so the function incorrectly drops or conflates distinct values (e.g., `0` and `false` may share behavior through `!seen[arr[i]]`). Additionally, `seen[arr[i]]` is never set to `true`, so no duplicates are actually tracked.

## Bug 5 – bug5.py
**Intended Behavior**: Parse a JSON configuration string and extract `timeout`, `retries`, and `verbose` settings.
**Issue Type**: Runtime exception (unhandled errors).
**Notes**: The function does not handle missing keys (`KeyError`) or malformed JSON (`json.JSONDecodeError`). It crashes on the second and third test cases instead of returning a sensible default or error message.

## Bug 6 – bug6.c
**Intended Behavior**: Reverse a string in place.
**Issue Type**: Off-by-one error in loop boundary.
**Notes**: The loop condition `i <= len / 2` swaps one extra iteration when the string has an even length. For a string like `"abcd"` (length 4), the middle characters get swapped twice — once forward and once back — leaving them in their original position and producing incorrect output.
