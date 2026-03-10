

# Bug Descriptions

## Bug 1 – bug1.py
**Intended Behavior:**
Return the last n items of a list.

**Issue Type:**
Off-by-one slicing error.

**Context & Implementation:**
The function returns n+1 items instead of n when n < len(items). The start index for slicing should be `len(items) - n` (not `len(items) - n - 1`).

---

## Bug 2 – bug2.js
**Intended Behavior:**
Remove duplicate numbers from an array and return them in ascending order.

**Issue Type:**
Logical error (incorrect condition in deduplication).

**Context & Implementation:**
The function only adds a number if it is already present in `result`, so unique values are never added. The condition should be inverted: add when NOT present (`!result.includes(numbers[i])`).

---

## Bug 3 – bug3.java
**Intended Behavior:**
Calculate the average length of non-null strings in a list, ignoring nulls.

**Issue Type:**
Runtime exception (NullPointerException).

**Context & Implementation:**
No null check before calling `str.length()`. Should skip nulls to avoid exception and only count non-null strings.

---

## Bug 4 – bug4.py
**Intended Behavior:**
Sum all values in a dictionary where the values are numbers stored as strings.

**Issue Type:**
Data type misuse (numeric handling error).

**Context & Implementation:**
Values are numeric strings, but `total` is initialized as a string and `+=` performs concatenation (e.g., "10" + "5" → "105"). `total` should be initialized as an integer (e.g., `0`), and each `value` should be converted to an integer (e.g., `int(value)`) before adding.

---

## Bug 5 – bug5.js
**Intended Behavior:**
Fetch user data from an API endpoint and return the user's name in uppercase using async/await.

**Issue Type:**
Syntax error (async/await misuse).

**Context & Implementation:**
`await` can only be used inside an `async` function. In the buggy code, `await fetch(...)` is inside a non-async function, causing a syntax error. Fix by declaring `async function fetchUserNameUpper(...) { ... }` and awaiting it from the caller (e.g., using an async IIFE or top-level await).

---

## Bug 6 – bug6.py
**Intended Behavior:**
Find the first pair of consecutive numbers in a list that sum to a target value.

**Issue Type:**
Logic error (infinite loop).

**Context & Implementation:**
The loop never increments the index when there is no match, so `i` stays the same and the `while` condition never changes (infinite loop). Fix by incrementing `i` on every iteration and only returning when a match is found.
