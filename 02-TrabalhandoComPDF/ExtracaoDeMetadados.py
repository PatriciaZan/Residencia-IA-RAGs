import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

with open("./dados_saida/twitter_algoritmo.md", "r", encoding="utf-8") as file:
    content = file.read()

metadata_text = content[:2000]

response = requests.post(
    "https://openrouter.ai/api/v1/chat/completions",
    headers={
        "Authorization": f"Bearer {os.getenv('OPENROUTER_API_KEY')}",
        "Content-Type": "application/json",
    },
    json={
        "model": "deepseek/deepseek-chat-v3",
        "messages": [
            {
                "role": "user",
                "content": f"""
Extract the metadata from this academic paper.

Document:

{metadata_text}
"""
            }
        ],
        "response_format": {
            "type": "json_schema",
            "json_schema": {
                "name": "paper_metadata",
                "strict": True,
                "schema": {
                    "type": "object",
                    "properties": {
                        "titulo": {
                            "type": "string"
                        },
                        "autores": {
                            "type": "array",
                            "items": {
                                "type": "string"
                            }
                        },
                        "ano": {
                            "type": ["integer", "null"]
                        },
                        "idioma": {
                            "type": "number"
                        },
                        "topicos": {
                            "type": "array",
                            "items": {
                                "type": "string"
                            }
                        }
                    },
                    "required": [
                        "titulo",
                        "autores",
                        "ano"
                    ],
                    "additionalProperties": False
                }
            }
        }
    }
)
#print(response.status_code)
#print(response.text)


data = response.json()

metadata = json.loads(
    data["choices"][0]["message"]["content"]
)

print(metadata)
