import requests
import json
from typing import List, Dict
from rich import print as rprint
import pyperclip


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
                        if "`" not in content_piece:
                            rprint(f"[yellow]{content_piece}[/yellow]", end= "", flush= True)
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
) -> None:
    
    messages = [{"role": "system", "content": system_instructions}]
    messages.append({"role": "user", "content": question})
    rprint(f"[bold magenta]\n> Assistant: [/bold magenta]\n", end= "")

    response = get_response(
        server_port, messages, temperature, top_p, max_tokens, stream
    )
    messages.append({"role": "assistant", "content": response})
    
    while True:
        rprint(f"[bold deep_pink4]\n> User: [/bold deep_pink4]\n", end= "")
        prompt = input("")
        if prompt.lower() == "quit": # if the user wants to terminate the chat
            rprint(f"\n[light_coral]Terminated [bold]smart-shell[/bold] session![/light_coral]")
            break
        elif prompt == "": # if the user just presses Enter, copy the last language model response to clipboard
            pyperclip.copy(messages[-1]["content"].replace("`", "").strip())
            rprint(f"[light_coral]Command copied to the clipboard![/light_coral]")
            break
        messages.append({"role": "user", "content": prompt})
        rprint(f"[bold magenta]\n> Assistant: [/bold magenta]\n", end= "")
        response = get_response(
            server_port, messages, temperature, top_p, max_tokens, stream
        )
        messages.append({"role": "assistant", "content": response})



