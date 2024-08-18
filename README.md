# SmartShell

AI-powered Shell Assistant.

_News: version 0.1.0 is now available cross-platform (only requires Python installation) using LLaMA.cpp HTTP Server for local inference._

<div align="center">
  <img src="assets/demo_gif.gif" alt="demo">
  <p><em>SmartShell running Meta's LLama 3 8B Instruct model on a MacBook Pro M3 Pro.</em></p>
</div>

## About
**SmartShell** is your ultimate command-line companion, delivering lightning-fast access to bash commands, Git tips, code snippets, and error output explanations. With SmartShell, there's no need to break your flow—just ask and get instant, accurate answers directly from your terminal. Simplify your workflow, reduce distractions, and keep coding with confidence.

### Features
- Generate shell commands and code snippets from natural language.
- Copy outputs directly to clipboard with one click.
- Intuitive interface.
- Support for open-source models using [LLaMA.cpp](https://github.com/ggerganov/llama.cpp).

## Getting Started
Follow these steps to install SmartShell globally on your system.

### Installation
1. Install the [Poetry](https://python-poetry.org/docs/) package manager.
2. (Optional, recommended) Create a virtual environment.
3. Clone this repo and navigate to the folder.
4. Run the following commands:
```console
$ poetry check
$ poetry install
```
(Make sure the command `check` returns the message `All set!`).


