# Bug Descriptions

## Bug 1 - bug1.py
**Intended Behavior**: Return the last n items of a list.  
**Issue Type**: Off-by-one error.  
**Notes**:
- Edge cases: if `n <= 0`, return `[]`.
- Edge cases: if `n >= len(items)`, return the full list.
- Fix start index: `len(items) - n - 1` should be `len(items) - n` (or clamp with `max(0, len(items) - n)`).

## Bug 2 - bug2.js
**Intended Behavior**: Remove duplicates and return ascending numbers.  
**Issue Type**: Logical error (inverted condition).  
**Notes**:
- The condition is reversed: it pushes only when the value is already in `result`.
- Fix by adding when NOT present: `if (!result.includes(numbers[i])) result.push(numbers[i]);`.

## Bug 3 - bug3.java
**Intended Behavior**: Compute average string length ignoring nulls.  
**Issue Type**: Runtime exception (NullPointerException).  
**Notes**:
- `str` may be null; `str.length()` can throw.
- Skip nulls (e.g., `if (str == null) continue;`).
- Increment `count` only for non-null strings.

## Bug 4 - bug4.py
**Intended Behavior**: Sum values in a dict where values are numeric strings.  
**Issue Type**: Data type misuse (string concatenation vs numeric addition).  
**Notes**:
- `total` starts as a string, so `+=` concatenates.
- Convert each numeric string to an int: `int(value)`.
- Use numeric accumulator: set `total = 0`, then `total += int(value)`; return an int.

## Bug 5 - bug5.js
**Intended Behavior**: Fetch user JSON and return the user's name uppercased.  
**Issue Type**: Syntax error (async/await misuse).  
**Notes**:
- `await` must be inside an `async` function; otherwise it’s a syntax error.
- Fix by declaring `async function fetchUserNameUpper(userId) { ... }`.
- Callers must await/handle the returned Promise (e.g., from an async context or via `.then(...)`).

## Bug 6 - bug6.py
**Intended Behavior**: Find the first pair of consecutive numbers that sum to target.  
**Issue Type**: Loop logic issue (infinite loop).  
**Notes**:
- `i` increments only on match; on non-match it never changes → infinite loop possible.
- Ensure `i += 1` happens on the non-matching path (every iteration unless returning).