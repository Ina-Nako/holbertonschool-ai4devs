# Bug Descriptions

## Bug 1 – bug1.py
**Intended Behavior**: Return the last n items of a list.  
**Issue Type**: Off-by-one error.  
**Notes**: If `n <= 0`, return `[]`; otherwise the start index is off by one (`len(items) - n - 1` should be `len(items) - n`).

## Bug 2 – bug2.js
**Intended Behavior**: Remove duplicates and return ascending numbers.  
**Issue Type**: Logical error.  
**Notes**: The condition is inverted: it pushes a number only if it is already in `result`; invert to add only when `!result.includes(numbers[i])`.

## Bug 3 – bug3.java
**Intended Behavior**: Compute average string length ignoring nulls.  
**Issue Type**: Runtime exception (NullPointerException).  
**Notes**: `str` may be null; add a null-check before `str.length()` and count only non-null strings.

## Bug 4 – bug4.py
**Intended Behavior**: Sum values in a dict where values are numeric strings.  
**Issue Type**: Data type misuse.  
**Notes**: `total` must be an integer (start with `0`) and each `value` must be converted with `int(value)` before adding.

## Bug 5 – bug5.js
**Intended Behavior**: Fetch user JSON and return the user's name uppercased.  
**Issue Type**: Syntax error (async/await misuse).  
**Notes**: `await` must be inside an `async` function; declare `fetchUserNameUpper` as `async` and await/handle the returned Promise at the call site.

## Bug 6 – bug6.py
**Intended Behavior**: Find the first pair of consecutive numbers that sum to target.  
**Issue Type**: Logic error (infinite loop).  
**Notes**: The loop doesn’t increment `i` on non-matches; ensure `i` increments each iteration unless returning a match.