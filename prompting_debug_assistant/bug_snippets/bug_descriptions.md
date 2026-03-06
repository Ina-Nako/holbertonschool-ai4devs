# Bug Descriptions

## Bug 1 - bug1.py
**Intended Behavior**: Return the last n items of a list.
**Issue Type**: Off-by-one error.
**Notes**: Issue: start index uses `len(items) - n - 1` causing extra item(s). Fix: use `len(items) - n` (and keep `n <= 0` returning `[]`).

## Bug 2 - bug2.js
**Intended Behavior**: Remove duplicates and return ascending numbers.
**Issue Type**: Logical error.
**Notes**: Issue: condition is inverted (pushes only if already included). Fix: push only when `!result.includes(numbers[i])`, then sort ascending.

## Bug 3 - bug3.java
**Intended Behavior**: Compute average string length ignoring nulls.
**Issue Type**: Runtime exception (NullPointerException).
**Notes**: Issue: `str` may be null and `str.length()` throws. Fix: skip nulls and increment `count` only for non-null strings.

## Bug 4 - bug4.py
**Intended Behavior**: Sum values in a dict where values are numeric strings.
**Issue Type**: Data type misuse.
**Notes**: Issue: `total` is a string so `+=` concatenates. Fix: set `total = 0` and add with `total += int(value)`.

## Bug 5 - bug5.js
**Intended Behavior**: Fetch user JSON and return the user's name uppercased.
**Issue Type**: Syntax error (async/await misuse).
**Notes**: Issue: `await` is inside a non-async function. Fix: declare `async function fetchUserNameUpper(...)` and await/handle the returned Promise at the call site.

## Bug 6 - bug6.py
**Intended Behavior**: Find the first pair of consecutive numbers that sum to target.
**Issue Type**: Logic error (infinite loop).
**Notes**: Issue: `i` increments only on match, so it can loop forever. Fix: increment `i` on non-match each iteration; return `None` if no pair matches.