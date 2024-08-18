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

5. Build the `.whl` file:
```console
$ poetry build
```
6. Finally, install the package globally:
```console
$ pipx install /path/to/your/.whl/file
```

### Model Selection
**SmartShell** uses the LLaMA.cpp local [HTTP server](https://github.com/ggerganov/llama.cpp/blob/master/examples/server/README.md) to run inference with open-source LLMs. Install `llama.cpp` following the instructions [here](https://github.com/ggerganov/llama.cpp).

The [Example](#example) section shows how to run the LLama 3 8B Instruct model.

### Basic Usage
Simply type `smart-shell q` followed by your question.

See [this page](smart_shell/README.md) for a complete list of available commands to call the CLI tool.

## Example
This example shows how to set up **SmartShell** with [Meta's LLama 3 8B](https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct) model for demonstration purposes.

1. Navigate to your local `llama.cpp` cloned folder and run:
```console
$ python -m pip install -r requirements.txt
```

2. Download the model:
```console
$ huggingface-cli download meta-llama/Meta-Llama-3-8B-Instruct --exclude "original/*"  --local-dir models/Meta-Llama-3-8B-Instruct
```

3. Convert the model to `.GGUF` format for LLaMA.cpp:
```console
$ python convert_hf_to_gguf.py models/Meta-Llama-3-8B-Instruct
```

4. (Optional) Quantize the model to reduce hardware requirements following the steps [here](https://github.com/ggerganov/llama.cpp/blob/master/examples/quantize/README.md).

5. Start the LLaMA.cpp server:
```console
$ ./llama-server -m models/path/to/your/model.gguf --port 8080
```

6. Configure the local server port:
```console
$ smart-shell config <your-local-port-number>
```
Make sure that the port number is the same one you used to initialize the server above.

7. Now you are ready to use **SmartShell** with LLama 3 8B!
Run:
```console
$ smart-shell q <your-question>
```

## Future Work
- Add more configuration and customization options, e.g., system prompt.
- Improve UI and markdown formatting.

## References
- [Typer](https://typer.tiangolo.com/tutorial/package/)
- [Rich](https://rich.readthedocs.io/en/stable/index.html)
- [LLaMA.cpp](https://github.com/ggerganov/llama.cpp)
- [HuggingFace](https://huggingface.co/models)

