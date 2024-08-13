from typing import Optional
from pathlib import Path
import typer

from smart_shell import __app_name__, __version__, ERRORS, llm, server_config

app = typer.Typer()


@app.command()
def config(
    port: int = typer.Option(
        str(llm.DEFAULT_PORT),
        "--port",
        "-p",
        help= "Port number for the server.",
        show_default= True),
) -> None:
    """Configure the application."""
    app_config_error = server_config.config_app(port)
    if app_config_error:
        typer.secho(
            f'Creating config file failed with "{ERRORS[app_config_error]}"',
            fg= typer.colors.RED,
        )
        raise typer.Exit(1)
    else:
        typer.secho(f"The server port is: {port}", fg= typer.colors.GREEN)


def _version_callback(value: bool) -> None:
    if value:
        typer.secho(f"{__app_name__} v{__version__}")
        raise typer.Exit()
    

@app.command("q")
def ask(
    question: list[str] = typer.Argument(
        ..., 
        help= "The question to ask the model."),
) -> None:
    """Ask a question to the language model."""
    if server_config.CONFIG_FILE_PATH.exists():
        server_port = llm.get_server_port(server_config.CONFIG_FILE_PATH)
    else:
        typer.secho(
            'Config file not found. Please, run "smart_shell config"',
            fg= typer.colors.RED,
        )
        raise typer.Exit(1)
    question = " ".join(question)
    answer = llm.start_chatbot(server_port, question, system_instructions= "You are a terminal assistant. Turn the natural language instructions into a terminal command. By default always only output code, and in a code block. However, if the user is clearly asking a question then answer it very briefly and well.")
    typer.secho(answer, fg= typer.colors.YELLOW)
 
    
@app.callback()
def main(
    version: Optional[bool] = typer.Option(
        None, # default value
        "--version", 
        "-v",
        help= "Show the application version.",
        callback= _version_callback, 
        is_eager= True),
) -> None:
    return