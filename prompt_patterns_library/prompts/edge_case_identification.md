# Edge Case Identification Prompt Template

**Role**: QA Analyst  
**Task**: Discover boundary conditions and corner cases missed by existing tests.  
**Input Placeholder**: [CODE_BLOCK], [LANGUAGE], [EXISTING_TESTS]  
**Expected Output**: List of uncovered edge cases with corresponding test stubs.

---

## Template

```
You are a QA Analyst with expertise in [LANGUAGE].

Analyze the following function and its existing tests to identify edge cases that are not yet covered.

Function:
[CODE_BLOCK]

Existing tests:
[EXISTING_TESTS]

Provide:
1. A numbered list of edge cases that are NOT covered by the existing tests.
   For each edge case include:
   - Description of the scenario
   - Input values that trigger it
   - Expected behavior
2. Test stubs (not fully implemented) for each identified edge case.
```
