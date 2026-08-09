# deve configurar uma OPENROUTER_API_KEY no ambiente Colab

# Checa se tem a API KEY
openrouter_api_key = userdata.get('OPENROUTER_API_KEY')

# Se não solta um erro
if not openrouter_api_key:
  raise ValueError("OPENROUTER_API_KEY is not set in Colab secrets.")

def get_embeddings(text):
  response = requests.post(
      "https://openrouter.ai/api/v1/embeddings",
  headers={
    "Authorization": f"Bearer {openrouter_api_key}",
    "Content-Type": "application/json",
  },
  json={
    "model": "openai/text-embedding-3-small",
    "input": f"{text}"
  }
  )

  data = response.json()
  embedding = data["data"][0]["embedding"]

  print(f"Embedding dimension: {len(embedding)}")
  print(embedding)
  return embedding, data

