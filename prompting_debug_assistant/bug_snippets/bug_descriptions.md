

# Bug Descriptions

## Bug 1 – bug1.py | Off-by-one Error (Python)
**Intended Behavior**: Return the last `n` items of a list.  
**Issue Type**: Off-by-one error — incorrect slice start index causes one extra item to be returned.  
**Context & Implementation**: The slice uses `len(items) - n - 1` as the start index, returning `n + 1` items instead of `n`. The correct start index is `len(items) - n`.

---

## Bug 2 – bug2.js | Logical Error (JavaScript)
**Intended Behavior**: Remove duplicate numbers from an array and return the unique values in ascending order.  
**Issue Type**: Logical error — inverted boolean condition prevents any unique value from being added.  
**Context & Implementation**: The condition `result.includes(numbers[i])` adds a number only when it is already in `result`, which is always false for the first occurrence. The condition must be negated: `!result.includes(numbers[i])`.

---

## Bug 3 – bug3.java | Runtime Exception (Java)
**Intended Behavior**: Calculate the average character length of non-null strings in a list, skipping null entries.  
**Issue Type**: Runtime exception — missing null check causes a `NullPointerException` when iterating over null list entries.  
**Context & Implementation**: `str.length()` is called without first verifying that `str != null`. A null guard must be added before accessing any method on `str`.

---

## Bug 4 – bug4.py | Data Type Misuse (Python)
**Intended Behavior**: Sum all numeric values stored as strings in a dictionary and return the integer total.  
**Issue Type**: Data type misuse — accumulator initialized as a string causes string concatenation instead of numeric addition.  
**Context & Implementation**: `total = ""` combined with `total += value` concatenates strings (e.g., `"10" + "5"` → `"105"`). The fix is to initialize `total = 0` and convert each value with `int(value)` before adding.

---

## Bug 5 – bug5.js | Syntax Error (JavaScript)
**Intended Behavior**: Fetch user data from an API endpoint and return the user's name transformed to uppercase.  
**Issue Type**: Syntax error — `await` used outside an `async` function, making the code invalid.  
**Context & Implementation**: `await fetch(...)` is called inside a regular (non-async) function. The enclosing function must be declared with the `async` keyword for `await` to be valid.

---

## Bug 6 – bug6.py | Logic Error / Infinite Loop (Python)
**Intended Behavior**: Find and return the first pair of consecutive elements in a list whose sum equals a given target value.  
**Issue Type**: Logic error — missing index increment inside the loop body causes an infinite loop.  
**Context & Implementation**: When no match is found, `i` is never incremented, so the loop repeatedly checks the same pair and never terminates. `i` must be incremented on every iteration regardless of whether a match is found.
