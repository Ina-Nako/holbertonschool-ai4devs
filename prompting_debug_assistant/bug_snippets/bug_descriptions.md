## Bug 1 – bug1.py
**Intended Behavior**: Calculate and print the average of a list of numbers.
**Issue Type**: Syntax Error.
**Notes**: The `print` statement is missing a closing parenthesis, leading to a `SyntaxError`.

## Bug 2 – bug2.js
**Intended Behavior**: Find the maximum value in an array of numbers.
**Issue Type**: Logical Error.
**Notes**: The `max` variable is initialized to `0`. If the array contains only negative numbers, it will incorrectly return `0` instead of the largest negative number. It should be initialized to the first element of the array or negative infinity.

## Bug 3 – bug3.java
**Intended Behavior**: Iterate through an array of integers and print each element.
**Issue Type**: Runtime Exception (ArrayIndexOutOfBoundsException).
**Notes**: The loop condition `i <= numbers.length` attempts to access an index one past the end of the array, causing an `ArrayIndexOutOfBoundsException` at runtime.

## Bug 4 – bug4.py
**Intended Behavior**: Return the first `n` elements of a given list.
**Issue Type**: Off-by-one / Loop Logic Issue.
**Notes**: The `range(n - 1)` in the loop causes it to iterate `n-1` times instead of `n` times. This results in one fewer element being returned than intended. If `n` is 0, it will also incorrectly return an empty list.

## Bug 5 – bug5.js
**Intended Behavior**: Add two numbers together and return their sum.
**Issue Type**: Misuse of Data Types / Type Coercion.
**Notes**: The `""` in `a + "" + b` explicitly converts the numbers to strings before concatenation, resulting in string concatenation instead of numerical addition.
