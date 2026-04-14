# Pull Request: Add Repository Analytics & Progress Reporting

## Summary
This PR implements a "Bug Analytics" feature that programmatically scans the project structure. It calculates the completion rate of the Bug Bounty exercise by comparing the `bug_snippets/` and `bug_fixes/` directories and generates a Markdown report for the user.

## Changes
- **Added `bug_analyzer.py`**: The core logic for the reporting engine (~120 LOC).
- **Automation**: Implemented automated detection of "unfixed" snippets.
- **Reporting**: Added functionality to export statistics to `analytics_report.md`.
- **Logic**: Created a Python class `BugReportFeature` to handle data processing and formatting.

## Context
**LOC Count**: ~125 lines of Python code.
**Motivation**: As the number of buggy snippets grows, it becomes difficult to track which bugs have been successfully addressed. This feature provides a quick dashboard for the developer to see project health.

## Verification
- Ran `python3 bug_analyzer.py` in the terminal.
- Verified that `analytics_report.md` was created with correct percentages.
- Confirmed it correctly identifies missing fixed files if a snippet is added without a corresponding fix.
