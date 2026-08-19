# **Análise de Desempenho e Prontuário Fisiológico**

Aluna: Patrícia Zan de Oliveira

## Parte 1 - Identificação dos problemas

## _**1.1 Descrição do problema**_

Vindo da junção com um projeto pessoal "ProCore" que estou desenvolvendo envolvendo "Atividades fisicas para treino estruturado".

Geração mais precisa de resumos de atividades individuais, semanais, quinzenais, mensais e por blocos de treinos montendo o contexto de treinos esperados de se realizar com oque foi possivél realizar.

### - _Qual é o problema que você deseja resolver?_

Possibilidade de cruzar dados de atividades com planos de treinos e recuperação personalizados do usuário, além de poder gerar pesquisar e resumos de: "Por que esta semana deu certo?", "Oque eu realizei dos dias 00/00 até 00/00 e construa um treino parecido"

### - _Quem utilizaria a aplicação?_

<!-- prettier-ignore -->
| Cargo     | Contexto uso          | Nível técnico |
| -----     | ------------          | ------------- |
| Atletas   | Melhora de desempenho | Médio|
| Pessoas em Recuperação | Traçar o melhor plano de esporte após uma lesão ou ploblema de saúde| Médio |

### - _Que tipo de informação o usuário gostaria de consultar?_

Informações de treinos e desempenho, cruzando seus histórico de saúde com os treinos que realiza ou deseja realizar.

### - _De onde vêm essas informações?_

As métricas e descrições das atividades vem do processamento de xmls e preenchimento por parte do usuário.

### - _Por que utilizar um LLM sozinho não seria suficiente?_

Pois o usuário pode fornecer documentações de seu histórico de saúde, treinos ou históricos de como se recuperou de uma determinada lesão, assim cruzando com as insformações de treinos e metricas para melhor construir e seus treinos.

### - _Como o usuário vai utilizar o sistema? (API, aplicativo, interface web?)_

Interface web. ReactJS

### - _Três exemplos de perguntas que o usuário faria ao sistema"_

**1. Pergunta exemplo 1:**
"Quais treinos de ciclismo são melhores de eu fazer nos proximos 15 dias para que eu me recupere da minha lesão lombar?"

**Resposta exemplo 2:**
"Com base em seus ultimso exames médicos os melhores treinos para se realizar são de recovery, evitando subidas e força, também é recomendado ###, com base em seus exames disponivéis também é recomendado repouso de ### com fisioterapia 2x na semana"

---

**2. Pergunta exemplo 2:**
"Qual foi meu desempenho nos treinos de intervalos no último bloco com o esperado no planejamento de treinos intervalados?"

**Resposta exemplo 2:**
"Com base nos seus últimos 5 treinos de intervalos realizados no ultimo bloco voc~e teve um desempenho superior ao programado para este bloco, com um maior volume de intervalos com maior tempo sugerido. Tendo obtido um score maior de resultado porém um maior acumulo de fadiga, atenção para surgimento de fadiga crônica se o o padrão for seguido, é sugerido a diminuição de treinos de intervalos durante a próxima semana e a adição de treinos de endurance e recovery para maximizar os ganhos de força."

---

**3.Pergunta exemplo 3:**
"Oque pode ter contribuido para minha atual lesão na panturrilha direita?"

**Resposta exemplo 3:**
"Sua carga de treino nos últimos 15 dias apresenta poucos dias de treinos nos primeiros 10 dias e um rápido aumento de volume de carga em subidas em 3 secções e 1 secção de intervalos junto com as altas temperaturas em dias e horários de treinos que podem ter contribuido para sua lesão. Recomenda-se o descanso ou atividades de baixa intensidade por períodos menores de tempo para uma melhor chance de recuperação. **_carrega documento de histórico de lesão na panturrilha do user e aresenta um plano de ação recomendado_**"

---

## _**1.2 Por que RAG?**_

### _Por que RAG é adequado para esse problema?_

O RAG se enquadra neste cenário para a junção de histórico de treinos, lesões, planos de recuperação e planos de treino, dando um melhor cantexto pessoal do usuário que não existe fora do banco de dados do aplicativo.

### _Que tipo de conhecimento precisa ser fornecido ao modelo?_

Documentações de planos médicos, lesões, recuperação e métricas de atividades e usuário.

### _Esse conhecimento muda com que frequência? (diariamente, mensalmente, quase nunca?)_

Esse conhecimento é constantemente construído na base de dados do aplicativo, formando um hist´rorico que pode ser acessado e revisitado.

### _Existe necessidade de utilizar documentos privados ou específicos da organização?_

Sim, históricos privados do usuário.

### _Que problemas poderiam ocorrer se o LLM respondesse apenas com seu conhecimento pré-treinado? Dê um exemplo concreto de resposta errada que ele daria no seu cenário._

A falta de contexto sobre o usuário seria o maior problema, a LLM sozinha pode criar um plano de treino para qualquer pessoa, mas a adição de contexto sobre doenças e lesões junto ao acompanhamento apenas um Rag seria capaz de contribuir.

"Um treino para oumentar sua capacidade anaeróbica pode ser fazer intervalos 3x por semana, 1x secções mais longas em zona dois e 3x levantar pesos"

---

## _**1.3 Limitações - quando RAG não é a resposta**_

Em quais situações RAG não seria a melhor solução para esse problema?

- Busca por históricos de treinos, sem a analise dos dados: "Quais treinos realizei ente os dias 10/06 até 30/06"
- Busca por soma de score de uma semana/mês
- Busca por tipos de treinos cadastrados.

### _Existe alguma pergunta, dentro do seu próprio cenário, que RAG responderia mal e um banco de dados relacional responderia bem? Qual, e por quê?_

Sim, soma entre valores para resumos semanais/mensais, escores,distancia,tempo etc...

### _O que aconteceria se a pergunta do usuário exigisse contar, somar ou ordenar informação espalhada por muitos documentos?_

Somas e ordenações podem ser feitas por um select bem construido no banco de dados.  
As informações de históricos médicos deverão ser amazenadas de forma organizada, mantendo documentos de temas próprios.

## Parte 2 - Organização dos documentos

Descreva:

### _Quais tipos de arquivo existirão? (PDF, DOCX, HTML, Markdown, páginas web, planilhas, imagens, áudios, vídeos, outros)_

- PDF
- Markdown
- Retornos JSON

### _Qual o volume aproximado? (dezenas, centenas, milhares de documentos?)_

- Dezenas de documentos.
- Milhares de atividades.

### _Qual o tamanho típico de cada documento? (Paginas, kbs)_

- 1 até 30 páginas.
- Resposta JSON podendo ter várias atividades.

### _Com que frequência novos documentos entram? Documentos antigos são atualizados ou substituídos?_

- Frequência diaria de Atividades (SQL).
- Documentos é váriavél.

_Proponha uma organização de pastas que faça sentido para o problema escolhido:_

```
    documentos/
    ├── bancoDeDados/
    ├── treinos/
    ├── historicoMedico/
    ├── historicoLesao/
    ├── relatorios/
    └── outros/
```

Esta organização permitiria a rapida navegação para documentos de interesse, separando históricos de diferentes categorias com os treinamentos contruidos pelo usuário.

### _Existe documento que não deve entrar na base? (informação sigilosa, dado pessoal, versão obsoleta) Como você impediria a entrada?_

A definir

### _Como você lidaria com versões do mesmo documento? Se a política de férias mudou em 2026, o sistema pode recuperar a versão de 2024 e responder errado._

Com o versionamento de documentos. Mantendo uma nomenclatura clara.

## Parte 3 - Pipeline de ingestão

Projete o processo que transforma os documentos originais em informação pesquisavel.

```
Para documentos upados pelo user:

    Documentos
        ↓
    Extração
        ↓
    Limpeza / normalização
        ↓
    Metadados
        ↓
    Chunking / Splitting
        ↓
    Embeddings
        ↓
    Banco vetorial
```

```
Para métricas do app:

       XML
        ↓
    Extração
        ↓
    Retorno FrontEnd
        ↓
    Preenchimento Descrição + dados pelo user
        ↓
    Salvamento no banco de dados (NodeJS+Supabase)
```

## _**3.1 Extração**_

### _Como o texto seria extraído?_

Docling.

### _Como você trataria PDFs com texto selecionável?_

A definir melhor metodo.

### _E PDFs digitalizados (imagem escaneada, sem camada de texto)?_

Extração de imagens e nromalização usando LLM para descrever a imagem, além de referênciar.

### _Como trataria tabelas? (é importante manter?)_

A definir melhor metodo.

### _Como trataria imagens? (posso descartar? quais informações elas tem?)_

Extração de imagens e nromalização usando LLM para descrever a imagem, além de referênciar.

### _Como trataria documentos multimodais?(multimodais = texto + imagem, audio + video, texto + video e etc)_

Extração de imagens e nromalização usando LLM para descrever a imagem, além de referênciar.  
A definir melhor forma.

Alguns problemas são: A imagem não ser corretamente extraida dos PDF, tabelas com formação errada.  
Ainda explorando a melhor forma de correção para estes casos.

### _Limpeza e normalização_

## _**3.2 Limpeza e normalização**_

### _O que precisa ser removido? (cabeçalhos e rodapés repetidos, numeração de página, marcas d'água, sumário, referências)_

- Marcas d'água.
- Sumário.
- A definir.

### _O que precisa ser padronizado? (acentuação, quebras de linha, espaçamento, codificação)_

- Codificação.
- A definir.

SQL/métricas

- Evitar retornar as atividadees por completo, mas sim partes importantes.

### _Que informação você corre o risco de **perder** ao limpar demais?_

- Perder referências de imagens.
- A definir.

SQL/métricas

- Métricas de cardío em atividades.

## _**3.3 Frequência de ingestão**_

### _O pipeline roda uma vez, sob demanda, ou de forma agendada? Com que frequência chegam novos documentos?_

Metricas por atividade irão executar a cada atividade cadastrada.
Upload de documentos pode variar bastante.

### _Quando um documento é atualizado, você reprocessa **só ele** ou a base inteira? Como sabe qual reprocessar?_

Só ele, por meio de versionamento dos documentos.

## Parte 4 - Metadados

## _**4.1 Metadados do documento**_

```json
Para documentos:
{
  "document_id": string,
  "created_at": timestamp,
  "title": string,
  "user_id": number,
  "document_type": string,
  "category": string
}
```

`"document_id"` -> identificação do documento.  
`"created_at"` -> Data de criação, caso o user deseje adicionar filtros ou definir documentos recentes.  
`"title"` -> Saber qual documento se trata.  
`"user_id"` -> Saber qual user está lincado o documento.  
`"document_type"` -> Qual tema se encaixa, lesão, exame, treino, resumos.  
`"category"` -> qual categoria, musculo, osso, pele | Intervals, Endurance | Resumo semana/mês/ano.

---

```json
Para métricas de atividades:
[
{
  "activity_id": number,
  "user_id": number,
  "created_at": timestamp,
  "title": string,
  "score": string,
  "fatique": number,
  "distance": numeber,
  "moving_time": number,
  "max_heartHate": number,
  "avr_heartHate": number,
  "training_type": string,
  "overviewIA" : string,
},
]
```

`"activity_id"` -> Identificar a atividade.  
`"user_id"` -> Identificar o user.  
`"created_at"` -> Para conseguir executar filtros.  
`"title"` -> Pode ser util.  
`"score"` -> Métrica.  
`"fatique"` -> Métrica.  
`"distance"` -> Métrica.  
`"moving_time"` -> Métrica.  
`"max_heartHate"` -> Métrica.  
`"avr_heartHate"` -> Métrica.  
`"training_type"` -> Métrica.  
`"overviewIA"` -> texto com o resumo da atividade da IA, compacta muita coisa aqui.

---

## _**4.2 Metadados do chunk**_

```json
A definir os resultados
{
  "document_id": string,
  "chunk_id": string,
  "page": number,
  "section": string,
  "document_type": string,
  "text": string,
  "has_image": boolean,
  "has_table": boolean
}
```

`"document_id"` -> Identificar o documento.  
`"chunk_id"` -> Identificar o chunk, facilita buscar os chunks ao "redor" para melhorar contexto.  
`"page"` -> Identificar página, ajuda a buscar chunks contidos.  
`"section"` -> Identificar uma secção, ajuda a melhorar contexto.  
`"document_type"` -> Identifica o tipo, facilita uma query de bsuca de texto.  
`"text"` -> texto contido no chunk.  
`"has_image"` > Para saber se tem imagem. Poderia ser um obj aqui?  
`"image_desc"` > Descrição da imagem ou conjunto dos chunks.  
`"has_table"` -> Para saber se tem uma tabela. obj?  
`"table"` -> conteúdo da table, chunk...

### \_\_
