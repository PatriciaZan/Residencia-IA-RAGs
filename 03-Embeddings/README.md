# Aula 03 - Embeddings
### Aluna: Patrícia Zan de Oliveira
Esta atividade foi executada no Google Colab. <br/>
** ❗ É altamente recomendável executar no Google Colab!**

## 🛠 Para executar
1. Fazendo o download do arquivo ``colab.ipynb`` e importar no Google colab.
2. Configurando a sua ``OPENROUTER_API_KEY`` no ambiente colab na área de secrets.
3. Configurando os arquivos ``.md`` de teste dentro da pasta ``/content/sample_data/bioetica_e_ia.md`` estes que serão apagados após o termino da secção colab.

## Arquivos .py presentes

Estes arquivos presented dentro da pasta ``./src`` são de caracter exploratório e de salvamento, uma vez que o ambiente não está configurado para a execução da aplicação .py



## ✏ Atividades Propostas
### 1. Distância Euclidiana

Crie uma função chamada `distancia_euclidiana()` que receba dois embeddings e retorne a **distância euclidiana** entre eles.

A distância euclidiana é calculada considerando a diferença entre cada uma das dimensões dos dois vetores.

Sua função deve ser capaz de receber dois vetores de qualquer dimensão, desde que possuam o mesmo tamanho.

**Exemplo de uso:**
```
    distancia = distancia_euclidiana(embedding_a, embedding_b)
    print(distancia)
````


### 2. Distância de Cosseno

Agora crie uma função chamada `distancia_cosseno()` que receba os mesmos dois embeddings e retorne a **distância de cosseno** entre eles.

Para isso, utilize o conceito de similaridade de cosseno entre dois vetores.

**Exemplo de uso:**

```
    distancia = distancia_cosseno(embedding_a, embedding_b)
    print(distancia)
```

### Testes
- Criações de tabelas.
- Criação de gráficos.

## Busca Semântica Simples Manual (Embedding por Embedding)

A Busca Semântica substitui a busca simples por palavra-chave .

Nesta etapa:

1. Lemos os arquivos de markdown gerados na aula 2.
2. Separamos o texto linha por linha.
3. Geramos o embedding para cada linha.
4. Definimos uma pergunta (*query*) de busca. (O que é “**Autonomia e opacidade algorítmica**”?, O que é o diário de bordo da IA? e etc)
5. Geramos o embedding da query e calculamos a Similaridade de Cosseno contra cada trecho.
6. Retornamos o TOP 3 com maior score! 
7. Dividir os documentos agora por trechos maiores (parágrafo) e repetir a etapa anterior.
8. Dividir os documentos agora por trechos maiores (capitulos) e repetir a etapa anterior.

