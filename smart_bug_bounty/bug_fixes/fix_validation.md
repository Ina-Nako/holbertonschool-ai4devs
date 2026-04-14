# Fix Validation Report

## bug1.py
- **Original Issue**: Incorrect slicing returned the lowest scores.
- **Fix Applied**: Adjusted slice from `[:n]` to `[-n:]`.
- **Test Results**: Passed. Input `[10, 50, 20, 80, 90]` now correctly returns `[50, 80, 90]`.

## bug2.js
- **Original Issue**: Off-by-one error caused `NaN` result.
- **Fix Applied**: Changed loop condition to `i < prices.length`.
- **Test Results**: Passed. The function now correctly returns the sum `19.49` instead of `NaN`.

## bug3.java
- **Original Issue**: Reference equality check failed for string content.
- **Fix Applied**: Replaced `==` with `.equals()`.
- **Test Results**: Passed. Console now correctly prints "Access Granted" for matching strings.

## bug4.js
- **Original Issue**: Closure/Scoping issue caused all timers to print the number 3.
- **Fix Applied**: Swapped `var` for `let` to ensure each iteration has its own scope.
- **Test Results**: Passed. Output is now the expected sequence: 0, 1, 2.
