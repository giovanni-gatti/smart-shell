import typer
import configparser
from pathlib import Path
from smart_shell import __app_name__, __version__


def get_server_port(config_file: Path) -> int:
    """Get the server port from the config file."""
    config_parser = configparser.ConfigParser()
    config_parser.read(config_file)
    return int(config_parser["SERVER"]["server_port"])


def _version_callback(value: bool) -> None:
    """Show the application version."""
    if value:
        typer.secho(f"{__app_name__} v{__version__}")
        raise typer.Exit()