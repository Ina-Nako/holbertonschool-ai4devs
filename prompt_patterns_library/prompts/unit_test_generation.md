# Unit Test Generation Prompt Template

**Role**: Test Engineer  
**Task**: Create comprehensive unit tests covering happy paths and edge cases for the given function.  
**Input Placeholder**: [CODE_BLOCK], [LANGUAGE], [TEST_FRAMEWORK]  
**Expected Output**: A complete test file using the specified framework.

---

## Template

```
You are a Test Engineer specializing in [LANGUAGE] and [TEST_FRAMEWORK] (e.g., pytest, Jest, JUnit).

Generate a complete unit test file for the following function or module.
Cover:
- Happy path (expected normal usage)
- Boundary / edge cases (empty input, max values, zeros)
- Error cases (invalid types, exceptions raised)
- Any documented side effects

Function to test:
[CODE_BLOCK]

Provide:
1. A ready-to-run test file using [TEST_FRAMEWORK].
2. Each test must have a descriptive name explaining what scenario it covers.
3. Include setup/teardown if necessary.
```
