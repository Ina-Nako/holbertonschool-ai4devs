# Bug Descriptions

## Bug 1 - bug1.py
**Intended Behavior**: Return the last n items of a list.  
**Issue Type**: Off-by-one error.  
**Notes**: Example: `last_n([1,2,3,4,5], 2)` should return `[4,5]` but returns `[3,4,5]` because the slice start index is computed one too far left (`len(items) - n - 1` instead of `len(items) - n`).

## Bug 2 - bug2.js
**Intended Behavior**: Remove duplicate numbers from an array and return them in ascending order.  
**Issue Type**: Logical error.  
**Notes**: The condition is inverted: it pushes a number only when it is already present in `result`, so nothing gets added from an empty start. Example: input `[3,1,2,3,2,4,1]` should return `[1,2,3,4]` but returns `[]`.

## Bug 3 - bug3.java
**Intended Behavior**: Calculate the average length of non-null strings in a list, ignoring nulls.  
**Issue Type**: Runtime exception (NullPointerException).  
**Notes**: No null check before calling `str.length()`. Example: `["hi", null, "world"]` should compute `(2 + 5) / 2 = 3.5`, but it throws `NullPointerException` when it hits the null element.

## Bug 4 - bug4.py
**Intended Behavior**: Calculate the sum of all values in a dictionary where the values are numbers stored as strings.  
**Issue Type**: Data type misuse (numeric handling error).  
**Notes**: `total` starts as a string, so `+=` concatenates instead of adding numerically. Example: `{"apples":"10","oranges":"5","pears":"2"}` should return `17` but returns `"1052"` (and returns a string instead of an int).

## Bug 5 - bug5.js
**Intended Behavior**: Fetch user data from an API endpoint and return the user's name in uppercase using `async/await`.  
**Issue Type**: Syntax error (async/await misuse).  
**Notes**: `await` must be used inside an `async` function. If `await` appears in a non-async function body, the file fails to parse.

## Bug 6 - bug6.py
**Intended Behavior**: Find the first pair of consecutive numbers in a list that sum to a target value.  
**Issue Type**: Logic error (infinite loop).  
**Notes**: The loop never increments the index when there is no match, so it can loop forever when no consecutive pair sums to `target`.