# LangChain: Documents | 12/08/26

Aluna: Patrícia Zan de Oliveira. <br>

## 🛠 Como navegar neste repositório

- `05_CriandoDocuments.ipynb`: Código resultante dos exercicios propostos.

## Criação do Document

Resultado:

```
documentos = [
    Document(
        page_content="O Avanço da inteligencia artificial na área da saúde e seu impacto",
        metadata={
            "fonte": "bioetica_e_ia.md",
            "pagina": 1,
            "tipo": "teoria",
            "tema": "inteligencia artificial",
            "autor": [
                "Juracy Barbosa dos Santos","Guilhermina Rego", "Rui Nunes"
            ]
        }
    ),

    Document(
        page_content="Limitações dos treinamentos e modelos de linguagens e perda de contexto",
        metadata={
            "fonte": "retrieval_augmented_generation.md",
            "pagina": 1,
            "tipo": "teoria",
            "tema": "perda de contexto",
            "autor": [
                "Aleksandra Piktus",
                "Fabio Petroni",
                "Vladimir Karpukhin",
                "aman Goyal",
                "Heinrich Küttler"
            ]
        }
    ),

    Document(
        page_content="Formas de treinamento de LLMS e melhores formas de manter contexto",
        metadata={
            "fonte": "scaling_laws_llm.md",
            "pagina": 4,
            "tipo": "arquitetura",
            "tema": "treinamentos",
            "autor": [
                "Johns Hopkins ",
                "Sam McCandlish"
            ]
        }
    ),

    Document(
        page_content="A tokenização transforma o texto em unidades que podem ser processadas pelo modelo.",
        metadata={
            "fonte": "retrieval_augmented_generation.md",
            "pagina": 4,
            "tipo": "teoria",
            "tema": "tokenização",
            "autor": [
                "Aleksandra Piktus",
                "Fabio Petroni",
                "Vladimir Karpukhin",
                "aman Goyal",
                "Heinrich Küttler"
            ]
        }
    ),

    Document(
        page_content="Chunks muito grandes podem dificultar a recuperação de informações específicas.",
        metadata={
            "fonte": "instruct_gpt.md",
            "pagina": 1,
            "tipo": "instrução",
            "tema": "Construção de chunkings",
            "autor": [
               "Long Ouyang",
               "Jeff Wu",
               "Xu Jiang",
               "Diogo Almeida "
            ]
        }
    )
]
```
