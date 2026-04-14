# Bug Descriptions

## bug1.py
- **Intended Behavior**: Sort a list of scores in ascending order and return the top $n$ (highest) scores.
- **Current Issue**: While the list is sorted correctly, the slice `[:n]` returns the $n$ smallest values from the start of the list instead of the $n$ largest values from the end.

## bug2.js
- **Intended Behavior**: Iterate through an array of numeric prices and calculate their total sum.
- **Current Issue**: An "off-by-one" error occurs in the loop condition `i <= prices.length`. Since array indexing is zero-based, the final iteration attempts to access an index that does not exist, resulting in `undefined` being added to the total.

## bug3.java
- **Intended Behavior**: Compare a user-provided string against a hardcoded "SECRET" string to authorize access.
- **Current Issue**: The code uses the `==` operator, which in Java compares the memory addresses (reference equality) of objects. Since strings are objects, it should use the `.equals()` method to compare the actual text content.

## bug4.js
- **Intended Behavior**: Loop from 0 to 2 and print each number to the console after a 100ms delay.
- **Current Issue**: The variable `i` is declared with `var`, which is function-scoped. Because `setTimeout` is asynchronous, the loop finishes before the first callback runs. By then, the single instance of `i` has been incremented to 3, causing the program to print "Counting: 3" three times.
