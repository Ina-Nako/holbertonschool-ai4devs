# Bug Descriptions & Analysis

## Bug 1 – bug1.py
**Intended Behavior**: Return the last `n` items from a list, with validation.

**Issue Type**: Off-by-one error and boundary condition.

**Notes**: 
- The function correctly handles most cases, but the boundary check `n > len(items)` returns an empty list when `n` equals `len(items)`, which should return the entire list.
- Expected: `get_last_n_items([1,2,3,4,5], 5)` → `[1,2,3,4,5]`
- Actual: Returns `[]`

**Error Category**: Logic error

**Hint**: Reconsider the validation condition. Should `n == len(items)` be allowed?

---

## Bug 2 – bug2.js
**Intended Behavior**: Asynchronously fetch user data from an API and log it.

**Issue Type**: Missing `await` keyword on Promise.

**Notes**: 
- Line 4: `const data = response.json();` returns a Promise, not the actual JSON object.
- The code tries to access `data.name` and `data.email` on a Promise, causing `undefined` output.
- Should be: `const data = await response.json();`

**Error Category**: Runtime/logical error (no exception thrown, but incorrect behavior).

**Hint**: When calling an async function that returns a Promise, remember to `await` it.

---

## Bug 3 – bug3.py
**Intended Behavior**: Calculate average of numbers, filtering out values above a threshold.

**Issue Type**: Runtime exception (ZeroDivisionError) and missing input validation.

**Notes**: 
- If `filter_outliers(scores, 50)` is called with all values filtered out, `filtered` becomes empty.
- `calculate_average([])` attempts division by zero: `total / count` where `count = 0`.
- Raises: `ZeroDivisionError: division by zero`

**Error Category**: Runtime exception and missing edge case handling.

**Hint**: Add validation to check if the list is empty before dividing.

---

## Bug 4 – bug4.java
**Intended Behavior**: Initialize a stock array with provided values and calculate totals.

**Issue Type**: Off-by-one error in loop boundary.

**Notes**: 
- Line 5: `for (int i = 0; i <= values.length; i++)` uses `<=` instead of `<`.
- This causes an `ArrayIndexOutOfBoundsException` when accessing `stock[values.length]`.
- The `stock` array has size 10, and `values.length` is 5, so `stock[5]` is valid—but `values[5]` doesn't exist!

**Error Category**: Off-by-one error leading to runtime exception.

**Hint**: Use `i < values.length` to avoid accessing beyond the array bounds.