# Setup Notes

## Objective

Prepare the IDE and AI coding assistant for testing in the `copilot_productivity_sprint` exercise.

## Environment Detected

- OS: Linux 5.15.167.4-microsoft-standard-WSL2
- IDE: Visual Studio Code Remote CLI `1.113.0`
- Git: `2.43.0`
- GitHub Copilot extension: not detected at the time of verification
- GitHub Copilot Chat extension: not detected at the time of verification

## Setup Steps

1. Open the repository folder `holbertonschool-ai4devs` in Visual Studio Code.
2. Open the Extensions view with `Ctrl+Shift+X`.
3. Search for `GitHub Copilot` and install the extension published by GitHub.
4. Search for `GitHub Copilot Chat` and install the extension published by GitHub.
5. Sign in with your GitHub account when prompted.
6. Authorize GitHub Copilot for your account and confirm that your subscription or access is active.
7. Open the Command Palette with `Ctrl+Shift+P`.
8. Run `GitHub Copilot: Sign In` if authentication did not complete automatically.
9. Run `GitHub Copilot: Enable` to ensure suggestions are active.
10. Optionally run `GitHub Copilot Chat: Focus on Chat View` to verify that chat is available in the IDE.
11. Open a source file and type a short function or comment prompt to confirm that inline suggestions appear.

## Version Check Commands

Use these commands in the VS Code terminal to verify installed versions:

```bash
code --version
git --version
code --list-extensions --show-versions
```

To filter Copilot extensions specifically:

```bash
code --list-extensions --show-versions | grep -E 'GitHub\.copilot|GitHub\.copilot-chat'
```

## Notes

- The current environment already has Visual Studio Code available.
- Git is installed and available.
- GitHub Copilot extensions were not detected during verification, so they still need to be installed in the IDE.
- After installation, rerun the extension version command above and update this file if exact extension versions are required for submission.