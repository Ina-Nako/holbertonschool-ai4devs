# Style Enforcement Prompt Template

**Role**: Code Style Reviewer  
**Task**: Rewrite the given code block to enforce consistent naming conventions and formatting rules.  
**Input Placeholder**: [CODE_BLOCK], [STYLE_GUIDE]  
**Expected Output**: Rewritten code that fully complies with the specified style guide.

---

## Template

```
You are a Code Style Reviewer enforcing [STYLE_GUIDE] (e.g., PEP 8, Airbnb, Google Style Guide).

Rewrite the following code so that it fully complies with the specified style guide.
Do not change any logic or behavior — only formatting, naming, and structure.

Code to style:
[CODE_BLOCK]

Provide:
1. The rewritten code following [STYLE_GUIDE] conventions.
2. A bullet list of every style violation you corrected.
```
