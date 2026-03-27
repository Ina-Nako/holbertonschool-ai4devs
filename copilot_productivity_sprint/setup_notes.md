# Setup Notes

## Objective

Prepare the IDE and AI coding assistant for testing in the `copilot_productivity_sprint` exercise.

## IDE And Tool Versions

- OS: Linux 5.15.167.4-microsoft-standard-WSL2
- IDE: Visual Studio Code Remote CLI 1.113.0
- Git: 2.43.0

## Copilot Extension Installation

The following installation commands were used from the VS Code terminal:

```bash
code --install-extension GitHub.copilot
code --install-extension GitHub.copilot-chat
```

Equivalent UI installation path:

1. Open Extensions with `Ctrl+Shift+X`.
2. Install `GitHub Copilot` (publisher: GitHub).
3. Install `GitHub Copilot Chat` (publisher: GitHub).

## Authentication And Enablement

1. Open Command Palette with `Ctrl+Shift+P`.
2. Run `GitHub Copilot: Sign In`.
3. Complete GitHub browser authentication.
4. Run `GitHub Copilot: Enable`.
5. Run `GitHub Copilot Chat: Focus on Chat View` to confirm chat is available.

## Final Verification

Commands used for verification:

```bash
code --version
git --version
code --list-extensions --show-versions | grep -Ei 'github\.copilot|github\.copilot-chat'
```

Verified extension output in this environment:

```text
github.copilot-chat@0.41.2
```

Installed/verified extension versions:

- GitHub Copilot Chat: 0.41.2
- GitHub Copilot (core): install command executed; not listed separately by `code --list-extensions` in this environment.

## Functional Test

1. Open any source file.
2. Type a short comment describing desired code.
3. Confirm inline suggestion appears.
4. Open Copilot Chat and ask a simple code question to confirm response generation.