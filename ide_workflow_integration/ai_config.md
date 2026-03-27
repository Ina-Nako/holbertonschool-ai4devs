# AI Workflow Configuration

## Objective

Set up AI-powered workflows in the IDE to improve coding speed and consistency.

## Applied Configuration Files

- `.copilot-settings.yaml` in project root

## Copilot/AI Setup

1. Install AI extensions in VS Code:
   - GitHub Copilot Chat
   - GitHub Copilot (if available in your environment)
2. Sign in via Command Palette: `GitHub Copilot: Sign In`.
3. Keep project-specific rules in `.copilot-settings.yaml` so AI responses follow repository conventions.
4. Use workflow prompts that map to the configured workflows (`code_review`, `doc_generator`).

## Language-Specific Rules

### Python
- Style guide: Black
- Type hints required
- Google-style docstrings
- Testing framework: pytest
- Guardrails: edge-case tests, avoid bare `except`, prefer small pure functions

### JavaScript
- Style guide: Airbnb
- Semicolons required
- Prefer `const`
- Enforce strict equality (`===`)
- Guardrails: validate external input, remove unused variables, provide explicit error messages

### Markdown
- ATX heading style (`#`, `##`, `###`)
- Maximum line length: 100
- Required sections for task documents: objective, steps, acceptance_criteria

## Specialized AI Workflows

### 1. Code Review Workflow
- Enabled for manual invocation
- Focus areas: security, performance, readability, regression risk
- Expected output sections: summary, findings, suggested fixes

Example prompt:

```text
Review this change using the repository code_review workflow.
Focus on security and regression risk first, then performance and readability.
Output: summary, findings, suggested fixes.
```

### 2. Documentation Generator Workflow
- Enabled for on-request use
- Targets: functions, endpoints, setup files
- Documentation constraints: include inputs/outputs and examples; keep sections concise

Example prompt:

```text
Use the doc_generator workflow to write docs for this endpoint.
Include inputs, outputs, and one usage example.
Keep each section under 200 words.
```

## Validation Checklist

- Root configuration file exists: `.copilot-settings.yaml`
- Language-specific rules are defined for Python and JavaScript
- At least one specialized workflow is enabled (`code_review`)
- Additional specialized workflow is enabled (`doc_generator`)