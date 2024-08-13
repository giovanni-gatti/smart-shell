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