import configparser
from pathlib import Path

DEFAULT_PORT = 8080 # default port for the server

def get_server_port(config_file: Path) -> int:
    config_parser = configparser.ConfigParser()
    config_parser.read(config_file)
    return int(config_parser["SERVER"]["server_port"])


 
