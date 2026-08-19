# **Sistema de Análise de Desempenho e Prontuário Fisiológico Privado de uma Equipe Profissional ou Atleta Pessoal**

## Parte 1 - Identificação dos problemas

## _1.1 Descrição do problema_

Vindo da junção com um projeto pessoal "ProCore" que estou desenvolvendo envolvendo "Atividades fisicas para treino estruturado".  
Em um futuro a implementação de treinadores e seus atletas ou times.

Utilizando documentos de treinos estruturados criados pelo treinador ou atleta e documentações de "diários" geradas pelo app e atletas com descrição rica de cada atividade e blocos de treinos, podendo assim cruzar informações de cenários de sucesso, fadiga, lesão.

Pergunta exemplo - "Entre os dias 15/02/26 á 10/03/26 quais treinos eu realizei?"
Resposta exemplo - "Você realizou os treinos de intervalo,endurance (lista os dias e treinos com metadados do treino)."

### **- Qual é o problema que você deseja resolver?**

A possibilidade de identificar padrões de sucesso, fadiga, lesões com base em dados/docs de "diários" de treinos passados.
Por meio da utilização de relatórios gerados pelo app que serão armazenados em PDF, podendo ser semanas, mensal, bloco, ano.

### **- Quem utilizaria a aplicação? Descreva o usuário concretamente: cargo, contexto de uso, nível técnico.**

<!-- prettier-ignore -->
| Cargo                 | Nível Técnico | Contexto          |
| --------------------- | ------------- | ----------------  |
| Atletas Amadores      | Baixo         | Pessoas que buscam entender melhor a relação fadiga X volume treino |
| Atletas Profissionais | Médio         | Atletas que buscam entender a relação fadiga X Carga X Lesões e ao planejamento estruturado de blocos de treino |
| Treinadores           | Alto          | Profissionais que desejam ter maior controle sobre seus atletas, entendendo melhor a relação das cargas e blocos de treinos com a fadiga e lesões apresentadas por cada integrante, melhorando assim de forma individual cada bloco de treino para que se adapte a cada atleta. |

### **- Que tipo de informação o usuário gostaria de consultar?**

Existe algum padrão entre entre carags de treinos elevadas e o maior consumo de carboidratos com fadiga durante o dia entre os dias 15/06/26 até 15/07/26?

Existe algum padrão de treinos realizados no ultimo mês com aumento da fadiga acumulada?
Quais treinos realizei nos ultimos 15 dias com maior score?

2. Relação Fatiga X Treinos realizados.
3. Relação Melhoria X Treinos Realizados.
4. Com o tempo e dados a possibilidade de construção de tipos de treinos corretos.

### **- De onde vêm essas informações?**

Banco de dados da aplicação que irão gerar Documentos "Diarios" dos últimos 15/30dias.

1. Kilometragem (xml)
2. Tempo de treino (xml)
3. Zonas (xml)
4. Tempo acumulado em Zonas (xml)
5. Descrição de sentimentos da atividade (preenchimento do usuário)
6. Dados metereologicos (api)
7. Gerado a cada 7/15/mês decorrido/bloco de treino. (app)
8. Descrição do usuário, idade,peso,altura,zonas,genero. (preenchimento do usuário)
9. score
10. Fadiga
11. Análise IA/LLM (ainda a definir)

### **- Por que utilizar um LLM sozinho não seria suficiente?**

- As informações obtidas de treinos são pessoais, estas que serão geradas por métricas.
- As informações de tipos de treinos construidas por Treinadores geralmente são feitas especialmente para cada atleta.
- Fazer a correlação Treino X Treino Executado X Resultados acabam sendo muitas informações para um LLM comum.

### **- Como o usuário vai utilizar o sistema? (API, aplicativo, interface web?)**

- Interface Web.
- Atualmente uma demo teste de processamento de dados existe com ReactJS, NodeJS, Python, supabase.

### **- Escreva também **três perguntas reais** que um usuário faria ao sistema. Perguntas concretas, do jeito que a pessoa falaria - não títulos de tópico.**

- Me retorne os treinos com maior score de fadiga dos ultimso 30 dias.
- Me retorne os treinos que realizei entre os dias 12/05/26 até 30/05/26.
- Me retorne os tipos de treinos que mais realizei nos últimos 30 dias.
- Me retorne meu plano de recuperação pós lesão na panturrilha.
- Quais atletas tiveram maior score acumulado nos últimos 30 dias?

## _1.2 Por que RAG?_

### **- Por que RAG é adequado para esse problema?**

- Para o consumo de dados de treinos pessoais de cada atleta e treinador, gerando resumos valiosos de consulta futura.

### **- Que tipo de conhecimento precisa ser fornecido ao modelo?**

Dados dos treinos.

- Diário de blocos (gerado pela aplicação).
- De atletas: Zonas, peso, altura, genêro, relátorio produzino pelo atleta(por atividade, semana, mês).
- De treino: Km, Altimetria, tempo, watts, cardio, score, descrição de como se sentiu, tipo treino.
- De tipo Treino: nome, tipo, zona esperada, repetições.
- Planos de treinos(Blocos) e recuperação pós prova/lesão.

### **- Esse conhecimento muda com que frequência? (diariamente, mensalmente, quase nunca?)**

- O conhecimento se agrega como um diário.
- Ele pode adicionar planos de recuperação e treinos para consulta.

### **- Existe necessidade de utilizar documentos privados ou específicos da organização?**

- Sim, documentos detalhando tipo de treino, detalhes do atleta, detalhes de atividades, diários de treinos.

### **- Que problemas poderiam ocorrer se o LLM respondesse apenas com seu conhecimento pré-treinado? Dê um exemplo concreto de resposta errada que ele daria no seu cenário.**

"Great effort today! You maintained a solid, controlled pace during the middle 3km and spent most of your time in heart rate zone 3. Your relative effort was slightly higher than your 30-day average, showing good endurance buildup. Keep this up for your next steady session!"

Não nescessariamente errada, porém é vaga, eu testei pessoalmente a IA do Strava (Athlete Intelligence) e rapidamente reparei que as respostas geradas são extremamente genéricas e não agregam em nada para identificar padrões de fadiga ou melhora. Não contribui em nada para melhor estruturar os treinos e quase nunca relaciona sua atividade com o treino que realizou(tempo,endurance,intervals, etc...)

- Também não criam históricos que podem ser usados para consulta.
- E não cria um banco de dados sobre planos de treinos/recuperação pessoais.

## _1.3 Limitações - quando RAG não é a resposta_

Em quais situações RAG **não** seria a melhor solução para esse problema?  
Considere e comente ao menos três alternativas:

### **-Busca tradicional por palavra-chave;**

Quando o treinador/atleta só quer fazer a busca por palavras chaves, como:

- Teste de FTP.s
- Como calcular zonas de treino?
- Oque é um treino de intervalo?

### **-Banco de dados estruturado e consultas SQL;**

Quando o treinador/atleta quer saber de métricas como:

- Distância/tempo na semana/mês
- Score
- Tempo em cada zona
- Tipo de treino em qual dia

### **-Regras determinísticas**

Protocolos de segurança de saúde e alertas de overtraining óbvios não devem depender de uma IA, mas sim de analise estatistica pelo próprio sistema.

### **-Utilização direta de uma API;**

Quando usar em vez do RAG: Para buscar dados em tempo real que mudam o tempo todo (como a previsão do tempo para o treino externo de ciclismo de hoje, ou buscar dados brutos direto da API do Garmin/Strava), consome a API diretamente, sem precisar indexar isso em uma base de vetores.

### **-Combinação de alguma dessas técnicas com RAG.**

Um banco SQL para guardar os números das métricas do atleta + um RAG para buscar as descrições ricas, feedbacks textuais do treinador e artigos científicos de periodização.

### **Responda também:**

- Existe alguma pergunta, dentro do seu próprio cenário, que RAG responderia **mal** e um banco de dados relacional responderia bem? Qual, e por quê?
  Qual é a soma total de quilômetros percorridos pelo atleta X em todos os treinos do mês de maio de 2026?  
  Qual foi a média exata da frequência cardíaca máxima nos treinos intervalados de terça-feira?

- O que aconteceria se a pergunta do usuário exigisse **contar**, **somar** ou **ordenar** informação espalhada por muitos documentos?
  Para tarefas de contagem, soma e ordenação em larga escala, o correto arquiteturalmente é extrair os dados para tabelas estruturadas (SQL) e deixar o banco de dados fazer o trabalho pesado, usando o RAG apenas para a parte de consulta.

## _Parte 2 - Organização dos documentos_

**1. Defina quais documentos serão utilizados.**

1. PDFs

**2. Qual o volume aproximado?**

1. Um novo documento a cada: 7/15/30dias/Por bloco/Por criação

**3. Qual o tamanho típico de cada documento? (Paginas, kbs)**

1. 200kbs.
2. 3 até 20 páginas.

**4. Com que frequência novos documentos entram? Documentos antigos são atualizados ou substituídos?**

1. Cada 15 dias.
2. Documentos antigos serão mantidos.

**5. Estrutura V.1**

```
    documentos/
    ├── userData/
    ├── tipoTreino/
    ├── diarioSemanal/
    ├── diarioMensal/
    ├── diarioBloco/
    ├── relatórioMensal/
    ├── documentosTreinos/
    ├── documentosRecuperacao/
    └── outros/

```

**6. Perguntas**

- Existe documento que **não deve** entrar na base? (informação sigilosa, dado pessoal, versão obsoleta) Como você impediria a entrada?
  Ainda devo definir
- Como você lidaria com **versões** do mesmo documento? Se a política de férias mudou em 2026, o sistema pode recuperar a versão de 2024 e responder errado.
  Arquivos antigos podem estar ligados diretamente em como um treino foi executado e seu resultado.  
  Logo arquivos antigos são a base para consultas.
  Porém arquivos de detalhes de treinos/recuperação podem ser atualizados com novos, porém é importante manter os antigos para consulta. Assim estabelecer um sistema de identificação de arquivos, versões.

## _Parte 3 - Pipeline de ingestão_

Projete o processo que transforma os documentos originais em informação pesquisave

```
Documentos
    ↓
Extração
    ↓
Limpeza / normalização (principalmente se o documento chegar poluido demais)
    ↓
Metadados (Lembram dos output estruturados do llm?)
    ↓
Chunking / Splitting
    ↓
Embeddings
    ↓
Banco vetorial (até agora trabalhamos com uma lista de vetores/embeddings que estamos fazendo a pesquisa na mão)
```

**1. Documentos serão gerados padronizados pelo App**

- Planos de treinos
- Relatórios quinzenais/mensais/blocos
- Informações do User

### 3.1 Extração

- Como o texto seria extraído?
  Docling para markdown

- Como você trataria PDFs com texto selecionável?
  Não teria

- E PDFs digitalizados (imagem escaneada, sem camada de texto)?
  Não teria
- Como trataria tabelas? (é importante manter?)
  Não teria
- Como trataria imagens? (posso descartar? quais informações elas tem?)
  Não teria
- Como trataria documentos multimodais?(multimodais = texto + imagem, audio + video, texto + video e etc)
  Não teria

Explique quais problemas podem surgir durante a extração. Se você já enfrentou algum deles nas atividades anteriores, cite o caso concreto.
Os arquivos pdf já seriam padronizados para evitar erros. Mas a atenção com imagens/tabelas e gráficos é nescessária.

### 3.2 Limpeza e normalização

- O que precisa ser removido? (cabeçalhos e rodapés repetidos, numeração de página, marcas d'água, sumário, referências)
  Nada
- O que precisa ser padronizado? (acentuação, quebras de linha, espaçamento, codificação)
  Nada
- Que informação você corre o risco de **perder** ao limpar demais?
  Nada
  Inicialmente não serão carregados Documentos não criados no app

### 3.3 Frequência de ingestão

- O pipeline roda uma vez, sob demanda, ou de forma agendada? Com que frequência chegam novos documentos?
  De forma agendada, podendo ser de 7/15/30 dias
  Sob demanda, quando o usuário quer fazer upload de documentos de treinos/recuperação.
- Quando um documento é atualizado, você reprocessa **só ele** ou a base inteira? Como sabe qual reprocessar?
  Não teriam documentos sofrendo atualizações.
  Documentação irá sofre uma implementação de versões.

## _Parte 4 - Metadados_

### 4.1 Metadados do documento

```json
  {
    "document_id": "001",
    "title": "Diário Fisiológico 01/08/2026|15/08/2026",
    "type": "Week/month"
    "created_at": "15/08/2026TimeStamp",
    "athlete": "Patrícia Zan"
    "isTrainingBlock": True/False,
    "block": "Endurance",
    "numberActivities"; 30,
    "success": True/False,
    "finalFatigue": 1234,
    "totalScore": 2940,
    "week": [
      {
        "number": 01,
        "fatigue": 25,
        "score": 100,
        "distance": 250,
        "time": 545,
        "text": ""

      }
    ]
  }
```

### 4.2 Metadados do chunk

```json
  {
    "document_id": "001",
    "chunk_id": "001-05",
    "page": 1,
    "section": "weekNumber",
    "success": True/False,
    "document_type": "diary",
    "text": "..."
  }
```

- Quais metadados você usaria para **filtrar** a busca? Dê um exemplo de pergunta em que o filtro é indispensável.
  1. created_at
     "Dos meus treinos entre dias 15/05 até 15/06 quais foram os que geraram maior fadiga?

- Quais metadados você usaria para **citar a fonte** ao usuário? O que exatamente apareceria na tela junto da resposta?
  1. title
  2. success
  3. created_at

- Que metadado seria caríssimo de acrescentar depois que a base já estivesse indexada? Por quê?  
  Dados de distribuição de zonas por semana/atividade. z1 - 20min/z2- 40min etc...  
  Uma vez que precisaria reprocessar todos os relatórios.

- Como você vai extrair esses metadados
  Extração de arquivos xml com pyhton e criação de arquivos PDF com alguma biblioteca ou LLM.  
  Preenchimento por parte do usuário.

### Parte 5 - Chunking / Splitting

**Devo testar para voltar e atualizar este arquivo corretamente**
**Explique e justifique:**

- Qual estratégia de splitting você utilizaria?
  Chunking Semantico  
  Cada dia conterá um treino com metadados e descrição do usuário, logo separar os chunks p equenos perderá contexto, e muito grandes irá abranger um contexto grande?  
  Assim separar em semantico manterá uma ideia por dia. (revisar)
- Qual tamanho aproximado dos chunks?
  200/300 char
- Utilizaria overlap? Quanto?
- A divisão seria por caracteres, palavras, sentenças, parágrafos ou seções?
- Utilizaria um splitter recursivo?
- Utilizaria uma estratégia **específica para cada tipo de documento**? Um contrato e uma transcrição de call center pedem o mesmo tratamento?
  Talvez, uma vez que a estrutura dos "diários" e dos docuemntos de treinos e recuperaçã osão outros.

**Responder:**

- O que pode acontecer se os chunks forem muito pequenos?  
  Perda de contexto
- O que pode acontecer se os chunks forem muito grandes?  
  Misturar tipos de dados, metadados, descrições.
- Como você trataria uma **tabela** na hora de dividir? Uma tabela cortada ao meio ainda significa alguma coisa? e uma imagem?  
  Deverão ser extraidas para arquivos separados e referenciadas.
- Como saber se a sua escolha de chunking foi boa? Que evidência você juntaria para provar isso?  
  Não sei, devo testar e analisar

### Parte 6 - Embeddings

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

- Considerou algum modelo alternativo e descartou? Qual, e por quê?
  text-embedding-3-large foi descartado para esta fase inicial por ser financeiramente mais custoso.

- Se o cenário envolve documentos sigilosos, isso muda sua escolha entre modelo local e API? Como?
  Caso a política de privacidade da equipe exija isolamento absoluto e soberania de dados on-premise, a melhor alternativa seria migrar para um modelo open-source executado localmente, como o BGE-M3 (1024 dimensões, gratuito e executado via infraestrutura própria).

- O tamanho máximo de entrada do modelo tem relação com a sua decisão de chunking da Parte 5? Explique.
  O limite de 8.191 tokens do modelo é generiso, permitindo que relatórios quinzenais ou mensais inteiros sejam processados sem truncamentos drásticos. No entanto, a estratégia de chunking da Parte 5 continua essencial para fatiar o texto em seções menores

### Arquitetura final

### 1. Um diagrama do sistema completo, do documento original até a resposta ao usuário. Pode ser desenho, ferramenta de diagramação ou ASCII - o que importa é estar legível e completo.

<!-- prettier-ignore -->
```
[ Documentos Originais ] (App / JSON / XML / Relatórios PDF)  
         │  
         ▼  
[ Pipeline de Ingestão ]  
         ├── 1. Extração (Docling -> Markdown)  
         ├── 2. Limpeza e Normalização  
         ├── 3. Enriquecimento de Metadados (created_at, success, athlete, etc.)  
         └── 4. Chunking / Divisão por Blocos / Semanas  
         │  
         ├──► [ Banco Relacional (SQL / Supabase) ] <─── (Dados Estruturados: Métricas numéricas,
         │                                              Kilometragem, Tempo, Zonas, Scores)
         │
         ▼
[ Embeddings & Indexação ]
         ├── Geração de Embeddings (ex: text-embedding-3-small)
         └── Armazenamento em [ Banco Vetorial ]
         ========================================================================
         [ FLUXO DE CONSULTA DO USUÁRIO ]
         ========================================================================
         │
         ▼
[ Interface Web (ReactJS) ] ── (Pergunta do Usuário: Ex: "Quais treinos geraram fadiga acima de 50 pontos?")
         │
         ▼
[ Orquestrador / Backend (Node.js / Python) ]
         ├── Roteamento da Consulta (Híbrido: SQL para métricas + RAG para descrições ricas)
         ├── Aplicação de Filtros de Metadados (ex: created_at, athlete)
         │
         ├────────────────────────────────────────┐
         ▼                                        ▼
[ Banco Relacional ]                     [ Banco Vetorial ]
(Busca exata de números/somas)           (Busca semântica de trechos relevantes)
         │                                        │
         └───────────────────┬────────────────────┘
                             │ (Contexto Combinado + Dados Brutos + Pergunta)
                             ▼
                 [ Modelo de Linguagem (LLM) ]
                             │
                             ▼
                 [ Resposta Estruturada ] ──► (Exibida na Interface Web com Citação de Fontes)
```

### 2. Uma tabela de decisões, reunindo tudo:

<!-- prettier-ignore -->
| Etapa     | Decisão                                                                               | Justificativa em uma linha  |
| --------- | ------------------------------------------------------------------------------------  | ----------------------------|
| Extração  | Docling para converter documentos padronizados em Markdown.                           | Garante consistência estrutural e leitura fluida sem ruídos de arquivos não padronizados.|
| Limpeza   | Limpeza mínima ou nula para documentos gerados nativamente pela aplicação.            | Evita o risco de descartar informações contextuais valiosas geradas pelo app.|
| Chunking  | Divisão baseada em blocos lógicos (semanas/atividades/relatórios quinzenais).         | Mantém a coesão temporal e contextual dos diários fisiológicos do atleta.|
| Metadados | Inclusão de carimbos temporais, status de sucesso, identificadores e métricas-chave.  | Permite filtragem precisa por datas, atletas e períodos de treino antes da busca vetorial.|
| Embeddings| Uso do modelo text-embedding-3-small (ou alternativa local como BGE-M3).              | Oferece alto desempenho semântico com excelente custo-benefício e suporte a textos longos.|

### 4. Riscos e limitações da sua própria proposta. O que você sabe que essa arquitetura não resolve bem?

Ela não retorna a certeza da relação lesão X treino, não retorna formas de correção.Estes deve mser feitas analises pelo usuário/treinador ou uma LLM.
