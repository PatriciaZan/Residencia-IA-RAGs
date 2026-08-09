

# --- Configuração da API ---
openrouter_api_key = userdata.get('OPENROUTER_API_KEY')
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
    return embedding, data


def calcular_euclidiana(vetor1, vetor2):
    soma_quadrados = sum((a - b) ** 2 for a, b in zip(vetor1, vetor2))
    return math.sqrt(soma_quadrados)

def calcular_cosseno(vetor1, vetor2):
    produto_escalar = sum(a * b for a, b in zip(vetor1, vetor2))
    magnitude1 = math.sqrt(sum(a ** 2 for a in vetor1))
    magnitude2 = math.sqrt(sum(b ** 2 for b in vetor2))

    if magnitude1 == 0 or magnitude2 == 0:
        return 1.0

    similaridade = produto_escalar / (magnitude1 * magnitude2)
    return 1.0 - similaridade


# Mapeamento de cada palavra com seu tema correspondente
dados_categorias = {
    "animal": ["gato", "felino", "cachorro"],
    "veiculo": ["carro", "caminhão", "moto"],
    "fruta": ["banana", "maçã", "goiaba"]
}

# 1. Obter primeiro os embeddings
banco_temas = {}
for tema in dados_categorias.keys():
    print(f"Buscando embedding do tema: {tema}...")
    embedding_tema, _ = get_embeddings(tema)
    banco_temas[tema] = embedding_tema

# 2. Processar cada palavra e calcular as métricas
lista_resultados = []

for tema, palavras in dados_categorias.items():
    vetor_tema = banco_temas[tema]

    for palavra in palavras:
        print(f"Processando palavra: {palavra}...")
        vetor_palavra, _ = get_embeddings(palavra)

        dist_euclidiana = calcular_euclidiana(vetor_palavra, vetor_tema)
        dist_cosseno = calcular_cosseno(vetor_palavra, vetor_tema)

        lista_resultados.append({
            "Tema": tema,
            "Palavra": palavra,
            "Dimensão Embedding": len(vetor_palavra),
            "Distância Euclidiana": round(dist_euclidiana, 4),
            "Distância de Cosseno": round(dist_cosseno, 4)
        })

# Geração da Tabela
df = pd.DataFrame(lista_resultados)

# Exibe a tabela formatada no ambiente do Colab
print("\n--- TABELA DE DISTÂNCIAS POR TEMA ---")
display(df)

# OUTPUT OBTIDO COLAB ________________________________________________

# Buscando embedding do tema: animal...
# Buscando embedding do tema: veiculo...
# Buscando embedding do tema: fruta...
# Processando palavra: gato...
# Processando palavra: felino...
# Processando palavra: cachorro...
# Processando palavra: carro...
# Processando palavra: caminhão...
# Processando palavra: moto...
# Processando palavra: banana...
# Processando palavra: maçã...
# Processando palavra: goiaba...
#

# --- TABELA DE DISTÂNCIAS POR TEMA ---

#  	    Tema 	    Palavra 	Dimensão Embedding 	Distância Euclidiana 	Distância de Cosseno
# 0 	animal 	    gato 	    1536 	            1.0468 	                    0.5476
# 1 	animal 	    felino 	    1536 	            1.0057 	                    0.5055
# 2 	animal 	    cachorro 	1536 	            1.0932 	                    0.5976
# 3 	veiculo 	carro 	    1536 	            0.8512 	                    0.3622
# 4 	veiculo 	caminhão 	1536 	            0.9081 	                    0.4123
# 5 	veiculo 	moto 	    1536 	            1.0438 	                    0.5449
# 6 	fruta 	    banana 	    1536 	            1.0790 	                    0.5824
# 7 	fruta 	    maçã 	    1536 	            0.9676 	                    0.4682
# 8 	fruta 	    goiaba 	    1536 	            1.0506 	                    0.5523