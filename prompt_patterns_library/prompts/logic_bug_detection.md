# Logic Bug Detection Prompt Template

**Role**: QA Engineer  
**Task**: Identify logic bugs such as off-by-one errors, incorrect conditions, or flawed algorithms.  
**Input Placeholder**: [CODE_BLOCK], [LANGUAGE], [FAILING_TEST_CASE]  
**Expected Output**: Annotated code highlighting faulty logic with a corrected version.

---

## Template

```
You are a QA Engineer specializing in [LANGUAGE].

The following function produces incorrect output for the given test case.

Function:
[CODE_BLOCK]

Failing test case (input → expected output → actual output):
[FAILING_TEST_CASE]

Provide:
1. An annotated version of the code that highlights the exact line(s) containing the logic bug.
2. A clear explanation of why the logic is wrong.
3. The corrected code.
4. Confirmation that the fix resolves the failing test case.
```
