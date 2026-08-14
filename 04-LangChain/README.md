# Aula 04 - 10/08/26

Aluna: Patrícia Zan de Oliveira. <br>
Este markdown contém as 15 respostas obrigatórias dos exercicios.

## 04-LangChain: Experimentos de Chunking para RAG

Este repositório contém uma série de experimentos focados na segmentação de documentos (_chunking_) utilizando LangChain. O objetivo principal foi avaliar como diferentes estratégias de divisão de texto impactam a estrutura, a preservação de contexto e a eficácia na recuperação de informações para sistemas de RAG (Retrieval-Augmented Generation).

As atividades foram realizadas em ambiente colab.

- Arquivo de geração de chunks `01_chunking.ipynb`
- Arquivo de geração de embeddings `02_Embeddings.ipynb`

```
 Objetivo geral do desafio:

        PDF
         ↓
        Extração do conteúdo
         ↓
        Markdown
         ↓
        Chunking
         ↓
        Embeddings
         ↓
        JSON
```

É recomendavél baixar os arquivos `.ipynb` que deseja testar e executalos pelo ambiente colab.

## 🛠 Como navegar neste repositório

- `/json_saida`: Contém os dados JSON brutos dos testes.
- `/imagens`: Contém os gráficos e tabelas comparativas dos resultados.
- `01_chunking.ipynb`: Código para gerar chunks, jupyter ou colab.
- `02_Embeddings.ipynb`: Código para gerar embeddings, jupyter ou colab.

## 📊 Visão Geral dos Testes

Foram realizadas 10 estratégias distintas de _chunking_, testadas em 12 documentos acadêmicos. Os dados detalhados (quantidades de _chunks_, tamanhos médios, máximos e mínimos) estão disponíveis na pasta `/json_saida`.

_Nota: Os arquivos `.json` contêm os logs brutos e os prints dentro de `./Tabelas` ilustram as tabelas comparativas dos 10 resultados obtidos por estratégia._

Os testes:

## 🔍 Análise Comparativa Obrigatoria (Resultados)

A análise de comportamento dos 10 testes foi feita com base no arquivo `escrita_academica_ia`. Todos os arquivos foram visualizados, porém a comparação dos testes foi padronizada utilizando este documento como referência.

Abaixo, apresento as conclusões obtidas após a análise dos 10 testes realizados:

### 1. Qual estratégia gerou mais chunks?

**Teste 1 (Fixo - 200 caracteres com overlap)**

- Apresentou o maior volume de fragmentos, variando de um máximo de 1542 (_gpt3_language_models_) para um mínimo de 212 (_escrita_academica_ia_). Esta estratégia resultou em um tamanho extremamente baixo por _chunk_.

### 2. Qual gerou menos chunks?

**Por Sentença (sentenças agrupadas por 3)**

- Manteve a estrutura mais natural, apresentando o menor número de fragmentos. Variou de 5 (_escrita_academica_ia_) a 29 (_gpt3_language_models_) chunks.

### 3. Como o tamanho dos chunks variou?

- Nos testes fixos o tamanho estava controlado, assim quanto maior o chunk, menor o numero de chunks gerados.
- Nos testes 5 e 6 a média se manteve em 500 caracteres, mas houve um aumento do número de chunks devido ao overlap.
- O tamanho do chunk impacta diretamente nas unidades recuperavéis, porém não significa melhor contexto.

### 4. Qual estratégia preservou melhor a estrutura dos documentos?

**Teste 10 - Markdown / estrutura semântica**

- Ele utilizou os cabeçalhos `#, ## e ###` como referência para dividir o documento e gerou menos chunks fragmentados.
- Para preservar a organização logica o **_MarkdownHeaderTextSplitter_** é o mais adequado.

### 5. Como tabelas foram tratadas?

- A conversão dos PDFs para markdown utilizando o Docling preservou as tabelas, transformando em tabelas Markdown, ou seja, texto estruturado.
  Exemplo do arquivo `escrita_academica_ia`:

```
        | Fase | Foco Principal | Objetivo |
        |------|----------------|----------|
        | Pré-escrita | ... | ... |
        | Escrita | ... | ... |
```

**Problema**

- Fazer uma divisão por caracteres pode/irá quebrar essa estrutura.
- Cabeçalho em um Chunk e linha em outra.
- Chunking de Overlap e de sentenças irão apresentar muitos problemas/ perda de contexto/ quebras.

**Melhor estratégia chunking para tabelas**

- Recursiva - Recursive Splitter
- Markdown - _MarkdownHeaderTextSplitter_

### 6. Como imagens foram tratadas?

**As imagens não foram preservadas como conteúdo visual dentro dos chunks.**

Este foi um dos problemas que tentei resolver na conversão de PDFs para Markdown, mas não obtive um sucesso satisfatório. Algumas imagens tiveram suas legendas transcritas.

- Transcrição de imagens retornou apenas `<!-- image -->`
- Legendas/Fontes e datas de imagens quando disponiveis foram mantidas e preservadas.

Assim uma analize não consegue compreender o conteúdo visual das imagens, apenas suas descrições.

### 7. Quais informações foram perdidas durante a conversão PDF → Markdown?

1. Imagens.
2. A Formatação original dos PDFs.
3. Alguns ícones foram transcrevidos como código html.
4. Perda de palavras quando a separação de chunks era de tamanho reduzido.
5. Icones, imagens em tabelas.

### 8. O chunking por caracteres fragmentou conceitos ou estruturas importantes?

**Sim**

- Quanto menor o número de caracteres aceito em um chunk maior a probabilidade de corte de palavras e posteriormente pior o resultado do contexto.
- Quanto maior o número de caracteres menor a probabilidade da perda de contexto

### 9. O chunking por parágrafo produziu chunks muito grandes?

**Não**

Levando em consideração a analise dos resultados do documento `escrita_academica_ia`:

- Possui 123 chunks
- média de 339,69 caracteres
- mínimo de 1
- máximo de 499

Os chunks não ficaram grandes, ficando inferiores a 500 caracteres, porém pode produzir chunks execisavente pequenos.

### 10. O chunking por sentença conseguiu preservar melhor o contexto?

**Talvez**

Levando em consideração a analise dos resultados do documento `escrita_academica_ia`:

- somente 4 chunks;
- média de 10.804,5 caracteres;
- mínimo de 10.018;
- máximo de 11.395.

Com o resultado obtido irei revisar como o teste 8 está implementado, pois não faz sentido possuir tantos caracteres por sentença.

### 11. O Recursive Splitter apresentou vantagens?

**Sim**

Levando em consideração a analise dos resultados do documento `escrita_academica_ia`:

- Gerou 125 chunks
- média de 349,04 caracteres
- máximo de 499
- mínimo de 1

Ele conseguiu produzir chunks menores sem depender de uma _posiçaõ_ fixa, além de gerar uma separação hierárquica.
Assim ele encontra a melhor forma de dividir, diminundo quebras de palavras.

### 12. O Markdown Splitter conseguiu preservar a estrutura semântica?

**Sim**

- Utilizou os marcadores `#, ##, ##` e preservou a estrutura hierárquica, dando mais contexto
- Porém os chunks ficam grandes

### 13. Qual estratégia parece mais adequada para um sistema de RAG?

**Recursive**
A estratégia recursive apresenta uma quantia de chunks e tamanhos equilibrados, tornando uma escolha interessante para fazer um RAG, ainda não realizei a leitura do resultado dos embeddings para testar se estou com algum sentido.

Seria interessante separar por **Markdonw** antes? Assim estruturaria em _tópicos_ e depois dentro de cada tópico aplicaria uma estratégia recursiva para reduzir o tamanho dos chunks.

### 14. Quais estratégias devem ser descartadas?

**Teste 1 - 200 caracteres**
Muita perca de contexto e palavras divididas.

**Teste 8 - 3 sentenças\***
Poucos chunks com muitos caracteres, algo ta errado ou é assim mesmo?

**Teste 6 - overlap 200**
Muito overlap gera muitos chunks com muitas palavras reptidas.

**Teste 4 - 2000 carateres**
Muitos caracteres para poucos chunks.

### 15. Quais estratégias utilizar nos próximos experimentos?

Complementar o markdown com a recursividade para ver como uma estrutura hierarquica se comportaria na preservação do contexto.
