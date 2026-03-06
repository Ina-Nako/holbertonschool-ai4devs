# Bug Descriptions

## Bug 1 – bug1.py
**Intended Behavior**: Return the last n items of a list.  
**Issue Type**: Off-by-one error.  
**Notes**: Handle edge cases first: if `n <= 0`, return `[]`; if `n >= len(items)`, return the full list. The bug is the start index: `len(items) - n - 1` should be `len(items) - n` (or `max(0, len(items) - n)`).

## Bug 2 – bug2.js
**Intended Behavior**: Remove duplicates and return ascending numbers.  
**Issue Type**: Logical error (inverted condition).  
**Notes**: The code pushes a number only if it is already present in `result`, so unique numbers are never added. Fix by inverting the condition: push only when `!result.includes(numbers[i])`.

## Bug 3 – bug3.java
**Intended Behavior**: Compute average string length ignoring nulls.  
**Issue Type**: Runtime exception (NullPointerException).  
**Notes**: `str` can be null, so calling `str.length()` throws. Fix by skipping nulls (e.g., `if (str == null) continue;`) and increment `count` only for non-null strings.

## Bug 4 – bug4.py
**Intended Behavior**: Sum values in a dict where values are numeric strings.  
**Issue Type**: Data type misuse (string concatenation vs numeric addition).  
**Notes**: `total` is initialized as a string, so `+=` concatenates. Fix by using an integer accumulator and converting each value: set `total = 0` and do `total += int(value)`; return `total` as an int.

## Bug 5 – bug5.js
**Intended Behavior**: Fetch user JSON and return the user's name uppercased.  
**Issue Type**: Syntax error (async/await misuse).  
**Notes**: `await` must be inside an `async` function; using it in a normal function is a syntax error. Fix by declaring `async function fetchUserNameUpper(userId) { ... }` and awaiting/catching the returned Promise at the call site.

## Bug 6 – bug6.py
**Intended Behavior**: Find the first pair of consecutive numbers that sum to target.  
**Issue Type**: Loop logic issue (infinite loop).  
**Notes**: The index increments only on match; when there is no match, `i` never changes and the loop can run forever. Fix by incrementing `i` on every non-matching iteration (ensure there is an `i += 1` when the condition is false).