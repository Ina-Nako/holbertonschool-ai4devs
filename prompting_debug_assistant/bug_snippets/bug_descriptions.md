# Bug Descriptions

## Bug 1 – bug1.py
**Intended Behavior**: Return the last n items of a list.  
**Issue Type**: Off-by-one error.  
**Notes**:
- Issue: The slice start index is calculated as `len(items) - n - 1`, which shifts the slice one position too far left.
- Fix: Use `len(items) - n` (optionally clamp: `max(0, len(items) - n)`).
- Edge cases: If `n <= 0`, return `[]`; if `n >= len(items)`, return the full list.

## Bug 2 – bug2.js
**Intended Behavior**: Remove duplicates and return ascending numbers.  
**Issue Type**: Logical error.  
**Notes**:
- Issue: The condition is inverted; it pushes values only when they are already present in `result`.
- Fix: Invert the condition to add only when `!result.includes(numbers[i])`.
- Result: After collecting uniques, sort ascending with `(a, b) => a - b`.

## Bug 3 – bug3.java
**Intended Behavior**: Compute average string length ignoring nulls.  
**Issue Type**: Runtime exception (NullPointerException).  
**Notes**:
- Issue: `str` may be null, so calling `str.length()` can throw `NullPointerException`.
- Fix: Skip nulls (e.g., `if (str == null) continue;`).
- Correctness: Increment `count` only for non-null strings so the average is computed properly.

## Bug 4 – bug4.py
**Intended Behavior**: Sum values in a dict where values are numeric strings.  
**Issue Type**: Data type misuse.  
**Notes**:
- Issue: `total` is initialized as a string, so `+=` concatenates instead of adding numerically.
- Fix: Initialize `total = 0` and convert each value: `total += int(value)`.
- Output: Return `total` as an integer (not a string).

## Bug 5 – bug5.js
**Intended Behavior**: Fetch user JSON and return the user's name uppercased.  
**Issue Type**: Syntax error (async/await misuse).  
**Notes**:
- Issue: `await` is used inside a non-async function, which is a syntax error.
- Fix: Declare the function as `async function fetchUserNameUpper(userId) { ... }`.
- Usage: Callers must await/handle the returned Promise (async context or `.then(...)`).

## Bug 6 – bug6.py
**Intended Behavior**: Find the first pair of consecutive numbers that sum to target.  
**Issue Type**: Logic error (infinite loop).  
**Notes**:
- Issue: The index `i` increments only on match; on non-match it never changes, causing an infinite loop when no pair matches.
- Fix: Ensure `i` increments on the non-matching path (every iteration unless returning).
- Behavior: Return the first matching consecutive pair; otherwise return `None`.