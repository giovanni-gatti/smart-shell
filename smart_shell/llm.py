import configparser
from pathlib import Path
import requests
import json
from typing import List, Dict
import typer

DEFAULT_PORT = 8080 # default port for the server


def get_server_port(config_file: Path) -> int:
    config_parser = configparser.ConfigParser()
    config_parser.read(config_file)
    return int(config_parser["SERVER"]["server_port"])


def get_response(
    server_port: int,
    messages: List[Dict[str, str]],
    temperature: float = 0.7,
    top_p: float = 0.9,
    max_tokens: int = 4096,
    stream: bool = True,
) -> str:
    headers = {"Content-Type": "application/json"}
    data = {
        "messages": messages,
        "temperature": temperature,
        "top_p": top_p,
        "max_tokens": max_tokens,
        "stream": stream,
    }
    # Send POST request to the server
    response = requests.post(
        f"http://localhost:{server_port}/v1/chat/completions",
        headers= headers,
        data= json.dumps(data),
        stream= stream,
    )
    response.raise_for_status()
    if stream:
        content = ""
        for line in response.iter_lines():
            if line:
                decoded_line = line.decode("utf-8").lstrip("data: ")
                try:
                    json_line = json.loads(decoded_line)
                    if "choices" in json_line and len(json_line["choices"]) > 0:
                        delta = json_line["choices"][0].get("delta", {})
                        content_piece = delta.get("content", "")
                        content += content_piece
                        # print(content_piece, end="", flush=True)
                        typer.secho(content_piece, fg= typer.colors.YELLOW, nl= False)
                except json.JSONDecodeError:
                    continue
        print()
        return content
    else:
        result = response.json()
        if "choices" in result and len(result["choices"]) > 0:
            return result["choices"][0]["message"]["content"]
        else:
            return ""


def start_chatbot(
    server_port: int,
    question: str,
    system_instructions: str = "",
    temperature: float = 0.7,
    top_p: float = 0.9,
    max_tokens: int = 4096,
    stream: bool = True,
):
    if question.lower() in ["exit", "quit"]:
        return
    messages = [{"role": "system", "content": system_instructions}]
    messages.append({"role": "user", "content": question})
    typer.secho(f"\nAssistant:", fg= typer.colors.GREEN, bold= True)
    #print("Assistant: ", end="")
    response = get_response(
        server_port, messages, temperature, top_p, max_tokens, stream
    )
    messages.append({"role": "assistant", "content": response})
    
    # while True:
    #     prompt = input("User: ")
    #     if prompt.lower() in ["exit", "quit"]:
    #         break
    #     messages.append({"role": "user", "content": prompt})
    #     print("Assistant: ", end="")
    #     response = get_response(
    #         server_port, messages, temperature, top_p, max_tokens, stream
    #     )
    #     messages.append({"role": "assistant", "content": response})



