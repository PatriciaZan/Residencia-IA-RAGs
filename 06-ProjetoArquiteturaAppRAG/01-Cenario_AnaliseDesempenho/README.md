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

### _Quais metadados você usaria para filtrar a busca? Dê um exemplo de pergunta em que o filtro é indispensável._

`"document_type"`, `"created_at"`, `"category"`.

"Quais trenos realizei entre os dias 15/06 até 30/06(`"created_at"`) seguindo o plano de treino de recuperação?(`"category"` e `"document_type"`)"

### _Quais metadados você usaria para citar a fonte ao usuário? O que exatamente apareceria na tela junto da resposta?_

Dependendo se a resposta for para:

- consultar sobre seus planos de treinos ou recuperação -> `"title"`, ``created_at"`
- Consultar atividades -> `"activity_id"`,`"created_at"`

### _Que metadado seria caríssimo de acrescentar depois que a base já estivesse indexada? Por quê?_

Metadados detalhando o pré/intra e pós treinos.
Seria uma métrica valiosa para determinar a causa de fatiga desnecessaria Porém deve ser implementada na aplicação.

### _Como você vai extrair esses metadados_

Extração dos PDFs por chunking,embeddings etc..
Metricas por extração em python dos gpxs/xml

## Parte 5 - Chunking / Splitting

Ajuda da IA para definir melhor estratégia.
**Devo testar e validar se estas opções são as melhores para o chunking dos documentos, métricas não sofreriam este processo**

### _Qual estratégia de splitting você utilizaria?_

Chunking Semantico

### _Qual tamanho aproximado dos chunks?_

200/300 char

### _Utilizaria overlap? Quanto?_

Sim, de 10%

### _A divisão seria por caracteres, palavras, sentenças, parágrafos ou seções?_

Parágrafos ou setenças.

### _Utilizaria um splitter recursivo?_

Tentaria, para manter melhor o contexto.

### _Utilizaria uma estratégia específica para cada tipo de documento? Um contrato e uma transcrição de call center pedem o mesmo tratamento?_

Esta estratégia seria para os documentos de treinos,recuperação e histórico médico. Já os documentos de diários talvez sejam melhores em chunks de parágrafos.

---

**Responder:**

### _O que pode acontecer se os chunks forem muito pequenos?_

Perda de contexto

### _O que pode acontecer se os chunks forem muito grandes?_

Muita coisa para a LLM processar

### _Como você trataria uma **tabela** na hora de dividir? Uma tabela cortada ao meio ainda significa alguma coisa? e uma imagem?_

Extração separada, referenciando quando nescessário.

### _Como saber se a sua escolha de chunking foi boa? Que evidência você juntaria para provar isso?_

Faria perguntas sobre um documento e processaria perguntas obvias para a LLM, assim saberia se houve uma perda expreciva de contexto.

## Parte 6 - Embeddings

**Requisitei ajuda de IA para melhor responder**

<!-- prettier-ignore -->
| Item | Resposta|
| ---                             | ----------|
| Modelo escolhido                | Text-embedding-3-small (ou alternativa open source local como BGE-M3) | 
| Dimensão do embedding           | 1536 dimensões (ajustável) |
| Suporta português?              | sim |
| É multilíngue?                  | Sim |
| Tamanho máximo de entrada       | 8.191 tokens |
| É open source?                  | Não (Proprietário via API) | 
| Pode ser executado localmente?  | Não (Disponível via nuvem/API) |
| Possui API?                     | Sim |
| Custo aproximado                | $0.02 por 1 milhão de tokens | 
| Fonte da informação (link)      | OpenAI API Pricing & Documentation / Crazyrouter Guide |

### _Considerou algum modelo alternativo e descartou? Qual, e por quê?_

text-embedding-3-large foi descartado para esta fase inicial por ser financeiramente mais custoso.

### _Se o cenário envolve documentos sigilosos, isso muda sua escolha entre modelo local e API? Como?_

Caso a política de privacidade da equipe exija isolamento absoluto e soberania de dados on-premise, a melhor alternativa seria migrar para um modelo open-source executado localmente, como o BGE-M3 (1024 dimensões, gratuito e executado via infraestrutura própria).

### _O tamanho máximo de entrada do modelo tem relação com a sua decisão de chunking da Parte 5? Explique._

O limite de 8.191 tokens do modelo é generiso, permitindo que relatórios quinzenais ou mensais inteiros sejam processados sem truncamentos drásticos. No entanto, a estratégia de chunking da Parte 5 continua essencial para fatiar o texto em seções menores

## Parte 7 - Arquitetura final

### _Um diagrama do sistema completo, do documento original até a resposta ao usuário. Pode ser desenho, ferramenta de diagramação ou ASCII - o que importa é estar legível e completo._

```
[ Fontes de Dados ]
  ├── Documentos (PDF, MD) ──► [ Extração ] (Docling + OCR para Imagens/Tabelas)
  └── Atividades (XML/GPX) ──► [ Processamento Python ] ──► [ Banco Relacional (Supabase/PostgreSQL) ]
                                                                      │
 [ Limpeza e Normalização ]                                           │
  ├── Remoção de ruídos (sumários, marcas d'água)                      │
  └── Padronização de codificação                                    ▼
                                                          [ Metadados & Armazenamento ]
 [ Chunking / Splitting ]                                  ├── Metadados de Atividade (activity_id, score, fatiga...)
  ├── Chunking semântico (200/300 chars)                   └── Metadados de Documento (document_id, user_id, tipo...)
  └── Overlap de 10% (parágrafos/sentenças)                           │
         │                                                            │
         ▼                                                            ▼
 [ Geração de Embeddings ]                                    [ Consulta Híbrida / Reta ]
  └── Text-embedding-3-small (ou BGE-M3)                      ├── Filtros SQL por data/categoria (Supabase)
         │                                                    └── Busca Vetorial por Similaridade
         ▼                                                            │
 [ Banco Vetorial ] <─────────────────────────────────────────────────┘
         │
         ▼
 [ Recuperação (Retrieval) ] ──(Top-K Chunks + Dados SQL Relacionais)
         │
         ▼
 [ LLM / Geração de Resposta ] ──(Contexto Pessoal, Histórico de Lesões e Métricas)
         │
         ▼
 [ Interface Web (ReactJS) ] ──► Exibição da Resposta e Citação de Fontes ao Atleta/Usuário
```

### _Uma tabela de decisões, reunindo tudo_

<!-- prettier-ignore -->
| Etapa      |	Decisão |	Justificativa em uma linha |
| ---------- | --------- | ---------------------------- |
| Extração   | Docling + LLM para descrições visuais | Garante a extração estruturada de textos, tabelas e conversão inteligente de imagens e PDFs complexos.| 
| Limpeza    | Remoção de marcas d'água, sumários e padronização de codificação | Elimina ruídos desnecessários preservando as métricas de cardio e as referências essenciais do usuário.| 
| Chunking   | Chunking semântico (200 a 300 caracteres com 10% de overlap) | Evita a perda de contexto pessoal ao fatiar documentos por parágrafos/sentenças de tamanho ideal. |
| Metadados  | Estruturação detalhada (user_id, document_type, created_at, score, etc.) | Permite filtros SQL e vetoriais rigorosos para consultas por períodos, categorias de lesão e tipos de treino.|
| Embeddings | text-embedding-3-small (ou open source local como BGE-M3)| Oferece alta precisão multilíngue em português com ótimo custo-benefício e flexibilidade de privacidade.|

### _Riscos e limitações da sua própria proposta. O que você sabe que essa arquitetura não resolve bem?_

1. Detecção de padrões antes de uma lesão acontencer.

- Ele consegue resgatar o histórico, porém não consegue fazer uma predição com estes dados de forma exata.
