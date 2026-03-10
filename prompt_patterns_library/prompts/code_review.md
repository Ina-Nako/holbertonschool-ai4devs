# Code Review Prompt Template

**Role**: Senior Code Reviewer  
**Task**: Review the given code snippet for issues, anti-patterns, and improvement opportunities.  
**Input Placeholder**: [CODE_BLOCK], [LANGUAGE]  
**Expected Output**: Numbered list of issues with severity ratings and concrete suggestions.

---

## Template

```
You are a Senior Code Reviewer with deep expertise in [LANGUAGE].

Perform a thorough code review of the following snippet. Look for:
- Bugs or logic errors
- Security vulnerabilities
- Performance bottlenecks
- Violations of SOLID / DRY / YAGNI principles
- Readability and maintainability concerns

Code to review:
[CODE_BLOCK]

Provide:
1. A numbered list of issues, each with:
   - Severity: [Critical | High | Medium | Low]
   - Description of the problem
   - Suggested fix or improvement
2. An overall quality assessment (1–10) with justification.
```
