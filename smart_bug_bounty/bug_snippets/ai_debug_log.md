# AI Debug Log

## bug1.py
- **AI Explanation**: The code sorts ascending but slices from the start, returning the lowest scores.
- **Suggested Fix**: Use `return scores[-n:]` or sort with `reverse=True`.
- **Confidence**: High

## bug2.js
- **AI Explanation**: The loop runs one time too many (`<=`), hitting an undefined array index and resulting in `NaN`.
- **Suggested Fix**: Change the condition to `i < prices.length`.
- **Confidence**: High

## bug3.java
- **AI Explanation**: In Java, `==` on Strings checks if they are the same object in memory, not if they have the same characters.
- **Suggested Fix**: Use `input.equals("SECRET")`.
- **Confidence**: High

## bug4.js
- **AI Explanation**: `var` does not have block scope. The loop finishes before the `setTimeout` triggers, so all logs see the final value of `i`.
- **Suggested Fix**: Replace `var` with `let` to create a fresh scope for each iteration.
- **Confidence**: High
