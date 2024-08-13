import typer
import configparser
from pathlib import Path

from smart_shell import __app_name__, WRITE_ERROR, DIR_ERROR, FILE_ERROR, SUCCESS

CONFIG_DIR_PATH = Path(typer.get_app_dir(__app_name__))
CONFIG_FILE_PATH = CONFIG_DIR_PATH / "config.ini"

def config_app(port: int) -> int:
    """Configure the application."""
    if not isinstance(port, int):
        raise Exception("Port must be an integer.")
    config_code = _init_config_file()
    if config_code != SUCCESS:
        return config_code
    model_code = _config_server(port)
    if model_code != SUCCESS:
        return model_code
    return SUCCESS


def _init_config_file() -> int:
    try:
        CONFIG_DIR_PATH.mkdir(exist_ok= True) # no error if exists
    except OSError:
        return DIR_ERROR
    try:
        CONFIG_FILE_PATH.touch(exist_ok= True)
    except OSError:
        return FILE_ERROR
    return SUCCESS


def _config_server(port: int) -> int:
    config_parser = configparser.ConfigParser()
    config_parser["SERVER"] = {"server_port": port}
    try:
        with open(CONFIG_FILE_PATH, "w") as config_file:
            config_parser.write(config_file)
    except OSError:
        return WRITE_ERROR
    return SUCCESS