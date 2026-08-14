import os
from dotenv import load_dotenv
from openai import OpenAI

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

client = OpenAI(
    api_key=os.getenv("API_KEY")
)

# Usa o modelo definido no .env ou um valor padrão
modelo = os.getenv("OPENAI_MODEL", "gpt-5.4-mini")

response = client.chat.completions.create(
    model=modelo,
    messages=[
        {"role": "user", "content": "Qual a capital do Brasil?"}
    ],
    store=True,
)

print(response.choices[0].message.content)