# Aula 02 - Extração de PDF para Markdown & Metadados com LLM
### Aluna: Patrícia Zan

Este projeto automatiza o fluxo de conversão de artigos acadêmicos em formato PDF para Markdown ``(.md)`` utilizando a biblioteca Docling. 
Em seguida, utiliza a API do OpenRouter (com o modelo DeepSeek-Chat) para extrair metadados estruturados (Título, Autores, Ano, Idioma e Tópicos) em formato JSON.

## 🚀 Funcionalidades

- 🔄 Conversão de PDF para Markdown: Leitura em lote de arquivos PDF na pasta de entrada e exportação limpa em Markdown.

- 🧠 Extração de Metadados via LLM: Análise automática do conteúdo extraído para capturar informações vitais em formato JSON estruturado com validação de esquema (json_schema).

- 🧪 Script de Teste Integrado: Script rápido para validar se o ambiente do Docling foi configurado corretamente.
- 
## 📁 Estrutura do Projeto
```
.
├── dados_entrada/          # Coloque seus arquivos PDF aqui (.pdf)
├── dados_saida/            # Arquivos convertidos para Markdown (.md)
├── dados_json/             # Saídas com metadados extraídos em formato JSON (.json)
├── src/
│   └── DoclingConectionTest.py # Script de teste de carregamento do Docling
├── main.py                 # Script principal: converte PDFs -> Markdown
├── ExtracaoDeMetadados.py  # Script de extração de metadados via OpenRouter (LLM)
├── .env                    # Variáveis de ambiente (Chaves de API)
├── .gitignore              # Arquivos ignorados pelo Git
└── README.md               # Documentação do projeto

```

## 🛠️ Pré-requisitos e Instalação

**1. Requisitos** 
- Python 3.9+ instalado na máquina.
- Chave de API da OpenRouter.

**2. Clonar o Repositório e Configurar o Ambiente** 

```
# Clone o repositório
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio

# Crie e ative um ambiente virtual (recomendado)
python -m venv venv

# Windows:
venv\Scripts\activate

# Linux/macOS:
source venv/bin/activate
```

**3. Instalar Dependências** 

Instale os pacotes necessários:
```
pip install docling requests python-dotenv
```
Nota: Dependendo do seu sistema e das dependências de Deep Learning do Docling, certifique-se de que o torch seja instalado adequadamente.

**4. Configurar Variáveis de Ambiente** 

Crie um arquivo .env na raiz do projeto com a sua chave da OpenRouter:
```
OPENROUTER_API_KEY=sua_chave_openrouter_aqui
```

## 🛠 Como Iniciar e Usar

1. Validar o Docling (Opcional)

Antes de executar o fluxo principal, você pode testar se a biblioteca Docling está carregando corretamente
```
python src/DoclingConectionTest.py

Saída esperada: Docling loaded successfully!
```


2. Converter PDFs para Markdown
- Adicione os seus arquivos .pdf dentro do diretório ./dados_entrada/.
- Execute o script main.py:
```
python main.py

O script irá processar todos os PDFs da pasta dados_entrada e salvar os arquivos .md correspondentes dentro de dados_saida/.
```

3. Extrair Metadados 
Para processar a extração dos metadados a partir do arquivo .md gerado:
```
python ExtracaoDeMetadados.py

O script enviará os primeiros caracteres do documento para a LLM através do OpenRouter e retornará um JSON estruturado.
```


## 🎉 Exemplo de Saída (JSON)

A resposta da extração de metadados segue o seguinte formato:
```
{
  "titulo": "Entre o algoritmo e o Juramento de Hipócrates: bioética na era da inteligência artificial",
  "autores": [
    "Juracy Barbosa dos Santos",
    "Guilhermina Rego",
    "Rui Nunes"
  ],
  "ano": 2026,
  "idioma": "Português (com resumo em Espanhol)",
  "topicos": [
    "Bioética",
    "Inteligência artificial",
    "Ética médica",
    "Autonomia pessoal"
  ]
}
```