
import os
import re
import pandas as pd
from langchain_text_splitters import (
    CharacterTextSplitter,
    RecursiveCharacterTextSplitter,
    MarkdownHeaderTextSplitter
)

# 1. Busca dinamicamente o arquivo dentro de AULA_04/markdown/
diretorio_atual = os.path.dirname(os.path.abspath(_file_))
caminho_arquivo = os.path.join(diretorio_atual, "markdown", "bioetica_e_ia.md")

if not os.path.exists(caminho_arquivo):
    print(f"❌ Erro: O arquivo não foi encontrado no caminho: {caminho_arquivo}")
    exit()

with open(caminho_arquivo, "r", encoding="utf-8") as f:
    texto_bioetica = f.read()

print(f"-> Arquivo 'bioetica_e_ia.md' carregado com sucesso! Total: {len(texto_bioetica)} caracteres.\n")

# 2. Execução dos 10 testes de chunking da aula
resultados = {}

# Teste 1: Fixo, 200 caracteres, sem overlap
sp1 = CharacterTextSplitter(chunk_size=200, chunk_overlap=0, separator="")
resultados[1] = ("Fixo, 200, sem overlap", "tamanho (extremo baixo)", sp1.split_text(texto_bioetica))

# Teste 2: Fixo, 500 caracteres, sem overlap
sp2 = CharacterTextSplitter(chunk_size=500, chunk_overlap=0, separator="")
resultados[2] = ("Fixo, 500, sem overlap", "tamanho", sp2.split_text(texto_bioetica))

# Teste 3: Fixo, 1000 caracteres, sem overlap
sp3 = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0, separator="")
resultados[3] = ("Fixo, 1000, sem overlap", "tamanho", sp3.split_text(texto_bioetica))

# Teste 4: Fixo, 2000 caracteres, sem overlap
sp4 = CharacterTextSplitter(chunk_size=2000, chunk_overlap=0, separator="")
resultados[4] = ("Fixo, 2000, sem overlap", "tamanho (extremo alto)", sp4.split_text(texto_bioetica))

# Teste 5: Fixo, 500, overlap 50 (10%)
sp5 = CharacterTextSplitter(chunk_size=500, chunk_overlap=50, separator="")
resultados[5] = ("Fixo, 500, overlap 50 (10%)", "overlap leve", sp5.split_text(texto_bioetica))

# Teste 6: Fixo, 500, overlap 200 (40%)
sp6 = CharacterTextSplitter(chunk_size=500, chunk_overlap=200, separator="")
resultados[6] = ("Fixo, 500, overlap 200 (40%)", "overlap pesado", sp6.split_text(texto_bioetica))

# Teste 7: Por parágrafo
chunks_p = [p.strip() for p in texto_bioetica.split("\n\n") if p.strip()]
resultados[7] = ("Por parágrafo", "estrutura natural", chunks_p)

# Teste 8: Por sentença, agrupando 3
sentencas = re.split(r'(?<=[.!?])\s+', texto_bioetica.replace("\n", " "))
chunks_sent = [" ".join(sentencas[i:i+3]).strip() for i in range(0, len(sentencas), 3) if " ".join(sentencas[i:i+3]).strip()]
resultados[8] = ("Por sentença, agrupando 3", "estrutura natural", chunks_sent)

# Teste 9: Recursivo (separadores hierárquicos)
sp9 = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50, separators=["\n\n", "\n", " ", ""])
resultados[9] = ("Recursivo (separadores hierárquicos)", "estratégia composta", sp9.split_text(texto_bioetica))

# Teste 10: Por seção / heading do Markdown
headers = [("#", "Header 1"), ("##", "Header 2"), ("###", "Header 3")]
sp10 = MarkdownHeaderTextSplitter(headers_to_split_on=headers)
docs_md = sp10.split_text(texto_bioetica)
chunks_md = [doc.page_content for doc in docs_md]
resultados[10] = ("Por seção / heading do Markdown", "estrutura semântica", chunks_md)

# 3. Monta e exibe a tabela de resultados no terminal
tabela = []
for test_id, (estrategia, variavel, chunks) in resultados.items():
    tam_medio = sum(len(c) for c in chunks) / len(chunks) if chunks else 0
    tabela.append({
        "Teste": test_id,
        "Estratégia": estrategia,
        "Variável Isolada": variavel,
        "Qtd Chunks": len(chunks),
        "Tam. Médio": round(tam_medio, 1)
    })

df = pd.DataFrame(tabela)

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

print("=== TABELA COMPARATIVA DE ESTRATÉGIAS DE CHUNKING ===")
print(df.to_string(index=False))

# 4. Salva o resultado em um arquivo CSV na mesma pasta
caminho_saida = os.path.join(diretorio_atual, "resultado_chunking.csv")
df.to_csv(caminho_saida, index=False, encoding="utf-8-sig")

print(f"\n✅ Arquivo gerado com sucesso em: {caminho_saida}")

# 5. Exibe uma amostra do 1º chunk de cada teste para ver como o texto foi cortado
print("\n" + "="*80)
print("DIFERENÇA DAS DIVISÕES (AMOSTRA DO 1º CHUNK DE CADA TESTE)")
print("="*80)

for test_id, (estrategia, variavel, chunks) in resultados.items():
    primeiro_chunk = chunks[0] if chunks else "Vazio"
    # Limpa quebras de linha excessivas para exibição limpa
    trecho_limpo = primeiro_chunk.replace('\n', ' ')[:120]
    print(f"\n[Teste {test_id} - {estrategia}]")
    print(f"  -> Qtd Chunks: {len(chunks)}")
    print(f"  -> Amostra: \"{trecho_limpo}...\"")