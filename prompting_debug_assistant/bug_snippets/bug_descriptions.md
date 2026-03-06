# Bug Descriptions

## Bug 1 – bug1.py
**Intended Behavior**: Return the last n items of a list.  
**Issue Type**: Off-by-one error.  
**Notes**: The slice start index is one too small: `len(items) - n - 1` should be `len(items) - n`. This returns `n+1` items when `0 < n < len(items)`, and it also fails when `n == len(items)` (it returns only the last element because the start becomes `-1`).

## Bug 2 – bug2.js
**Intended Behavior**: Remove duplicates and return ascending numbers.  
**Issue Type**: Logical error (inverted condition).  
**Notes**: The code adds a number only if it is already present in `result` (`result.includes(...)`), so starting from an empty array it never adds unique values. Fix by inverting the condition (add when NOT present: `!result.includes(numbers[i])`).

## Bug 3 – bug3.java
**Intended Behavior**: Compute average string length ignoring nulls.  
**Issue Type**: Runtime exception (NullPointerException).  
**Notes**: `str` can be null, so `str.length()` can throw. Fix by skipping nulls (e.g., `if (str == null) continue;`) and only incrementing `count` for non-null strings.

## Bug 4 – bug4.py
**Intended Behavior**: Sum values in a dict where values are numeric strings.  
**Issue Type**: Data type misuse (string concatenation vs numeric addition).  
**Notes**: `total` is initialized as a string, so `+=` concatenates (e.g., `"10" + "5" -> "105"`). Fix by initializing `total = 0` and converting each value (`total += int(value)`), so the function returns an integer.

## Bug 5 – bug5.js
**Intended Behavior**: Fetch user JSON and return the user's name uppercased.  
**Issue Type**: Syntax error (async/await misuse).  
**Notes**: `await` is used inside a non-async function, which is a syntax error. Fix by declaring the function as `async` and awaiting it from an async context (or using `.then(...)`).

## Bug 6 – bug6.py
**Intended Behavior**: Find the first pair of consecutive numbers that sum to target.  
**Issue Type**: Loop logic error (infinite loop).  
**Notes**: The index `i` increments only when a match is found; if no pair matches, `i` never changes and the loop runs forever. Fix by incrementing `i` on every non-matching iteration (i.e., ensure `i += 1` happens when the condition is false).

# Overview

## Bug 1 – bug1.py
**Intended Behavior**: Return the last n items of a list.  
**Issue Type**: Off-by-one error.  
**Notes**: Start index is `len(items) - n - 1` but should be `len(items) - n`.

## Bug 2 – bug2.js
**Intended Behavior**: Remove duplicates and return ascending numbers.  
**Issue Type**: Logical error (inverted condition).  
**Notes**: Uses `result.includes(x)` instead of `!result.includes(x)` when deciding to push.

## Bug 3 – bug3.java
**Intended Behavior**: Compute average string length ignoring nulls.  
**Issue Type**: Runtime exception (NullPointerException).  
**Notes**: Missing null check before calling `length()`; also count should only include non-null strings.

## Bug 4 – bug4.py
**Intended Behavior**: Sum values in a dict where values are numeric strings.  
**Issue Type**: Data type misuse (string concatenation vs numeric addition).  
**Notes**: `total` is a string and values aren’t converted to `int`.

## Bug 5 – bug5.js
**Intended Behavior**: Fetch user JSON and return the user's name uppercased.  
**Issue Type**: Syntax error (async/await misuse).  
**Notes**: `await` is used in a non-`async` function; make it `async` and await at call site.

## Bug 6 – bug6.py
**Intended Behavior**: Find the first pair of consecutive numbers that sum to target.  
**Issue Type**: Loop logic error (infinite loop).  
**Notes**: Missing `i += 1` when no match occurs.