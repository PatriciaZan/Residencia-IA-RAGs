# **Análise de Alertas de Defesa Civil e Planos de Contingência Municipais**

## Parte 1 - Identificação dos problemas

Ajudar na previsão de eventos climáticos que afetem o munocipío e acesso a documentos de ajuda/ações após acontecimentos.

Ajudar as prefeituras por meio de mapeamentos de áreas de risco e histórico de danos com o histórico de acumulados de chuva ou ventos, acionando os planos de contingência e retornos de instruções e coordenação dos órgãos competentes com mais agilidade.

## _1.1 Descrição do problema_

### **- Qual é o problema que você deseja resolver?**

A lentidão e a dificuldade na consulta descentralizada de documentos complexos e planos de ação durante eventos climáticos extremos. O objetivo é resolver a descoordenação e a demora no cruzamento de dados de previsão meteorológica (acumulados de chuva e ventos) com as diretrizes oficiais de resposta (planos de contingência e mapeamento de áreas de risco), permitindo uma reação mais rápida para salvar vidas e mitigar danos.

### **- Quem utilizaria a aplicação? Descreva o usuário concretamente: cargo, contexto de uso, nível técnico.**

<!-- prettier-ignore -->
| Cargo                                                                                                                                                 | NívelTécnico                                                           | Contexto                                                      |
| ----------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- | ------------------------------------------------------------- |
| Gestores públicos municipais, operadores e coordenadores da Defesa Civil, agentes de trânsito, equipes de assistência social e bombeiros civis locais | Nível variado de informatica para usar um sistema com interface básico | Ambiente de alta pressão e estresse durante crises climáticas |

### **- Que tipo de informação o usuário gostaria de consultar?**

- Planos de contingência municipais e protocolos específicos de atendimento.
- Diretrizes de rotas de fuga, localização e status de abertura de abrigos de emergência.
- Mapeamentos detalhados de áreas de risco e histórico de vulnerabilidade por bairro.
- Séries históricas de acumulados de chuva, rajadas de vento e dados de impacto passado.

### **- De onde vêm essas informações?**

Base de dados internas de prefeituras e órgãos competentes.

- Documentos institucionais em PDF, decretos e manuais da Defesa Civil local.

### **- Por que utilizar um LLM sozinho não seria suficiente?**

- Não possui acesso nativo aos documentos internos, legislações específicas, diretrizes locais de cada município e planos de ação restritos daquela localidade.
- Além de uma LLM estar sujeita a alucinações, oque não é ideal pra planos de fuga ou protocolos de ajuda.

### **- Como o usuário vai utilizar o sistema? (API, aplicativo, interface web?)**

- Será usado por uma interface web.
- Aplicativo app.

## _1.2 Por que RAG?_

### **- Por que RAG é adequado para esse problema?**

- Une o conhecimento de um base de documentação restrita com a linguagem natural.
- Buscar exatamente o que dizem os decretos, as leis de proteção civil e as diretrizes oficiais cadastradas, garantindo confiabilidade nas orientações fornecidas aos operadores públicos.

### **- Que tipo de conhecimento precisa ser fornecido ao modelo?**

Devem ser fornecidos documentos operacionais e geográficos restritos, tais como:

- Manuais de planos de contingência municipais e fluxos de acionamento de emergência.
- Mapeamentos detalhados de áreas de risco, zonas de inundação e histórico de vulnerabilidade por bairro.
- Decretos, legislações locais e diretrizes de atuação dos órgãos competentes (Bombeiros, Defesa Civil, Assistência Social).

### **- Esse conhecimento muda com que frequência? (diariamente, mensalmente, quase nunca?)**

É uma frequência variável.

- Os planos de contingência estruturais e mapeamentos de risco mudam quase nunca, mas pdoem sofrer revisões em épocas de chuvas.
- No entanto, dados operacionais complementares, relatórios de ocorrências e contatos de plantão podem sofrer alterações mensalmente ou semanalmente.

### **- Existe necessidade de utilizar documentos privados ou específicos da organização?**

Sim

- Cada município possui suas próprias leis, planos de contingência, rotas de fuga específicas e uma geografia única que não constam em bases de dados públicas gerais da internet. O uso de documentos privados e locais é o núcleo da aplicação.

### **- Que problemas poderiam ocorrer se o LLM respondesse apenas com seu conhecimento **pré-treinado? **Dê um exemplo concreto de resposta errada** que ele daria no seu cenário.

Se o LLM respondesse sozinho, ele daria orientações genéricas, desatualizadas ou perigosamente incorretas, pois desconhece a realidade geográfica e institucional daquele município específico.

- Exemplo concreto de resposta errada:
  Pergunta: O rio transbordou no bairro Vila Nova. Para qual abrigo municipal devemos evacuar os moradores e qual rota de fuga usar segundo nosso plano?
  Resposta errada: Procure um ginásio municipal ou escola próxima e siga para as partes altas da cidade"

## _1.3 Limitações - quando RAG não é a resposta_

Em quais situações RAG não seria a melhor solução para esse problema?

- busca tradicional por palavra-chave;
  Se o operador da Defesa Civil precisa apenas buscar um termo exato ou um contato publico de emergência, como "Qual é o número de telefone da central da Polícia Militar?".
- banco de dados estruturado e consultas SQL;
  Para dados numéricos, métricas de estações meteorológicas em tempo real e séries temporais estruturadas (ex: "Qual foi o volume exato de chuva registrado na estação pluviométrica do Bairro Centro entre 14h e 15h?")
- regras determinísticas;
  Em protocolos críticos de disparo automático de sirenes ou alertas de evacuação de emergência (ex: "Se o nível do rio ultrapassar o limite crítico de 4 metros, acionar automaticamente o alarme sonoro na comunidade")
- utilização direta de uma API;
  Para capturar dados externos que mudam a cada segundo direto de fontes oficiais em tempo real (como a previsão do tempo atualizada diretamente da API do INMET ou de radares meteorológicos de satélite)
- combinação de alguma dessas técnicas com RAG.
  um banco SQL para guardar as leituras numéricas das chuvas e o cadastro das famílias em risco + regras determinísticas para os gatilhos automáticos de alerta + RAG para buscar o contexto textual dos planos de contingência, diretrizes de abrigos e manuais de ação dos órgãos competentes.

**Existe alguma pergunta, dentro do seu próprio cenário, que RAG responderia mal e um banco de dados relacional responderia bem? Qual, e por quê?**
Sim
Pergunta :Qual é a soma total do volume de chuva acumulado em todas as estações do município no trimestre passado?
Um banco relacional seria muito mais rápido e preciso para esta resposta;

**O que aconteceria se a pergunta do usuário exigisse contar, somar ou ordenar informação espalhada por muitos documentos?**
Pergunta: "Some a capacidade de lotação de todos os abrigos de emergência descritos nos planos de contingência dos 10 distritos da cidade"
Pode ocorrer a perda de contexto, soma errada.

## Parte 2 - Organização dos documentos

### **- Quais tipos de arquivo existirão? (PDF, DOCX, HTML, Markdown, páginas web, planilhas, imagens, áudios, vídeos, outros)**

- PDFs e DOCX : Planos de contingência municipais, decretos de homologação de situação de emergência, manuais de procedimentos da Defesa Civil e relatórios técnicos.
- Planilhas (XLSX, CSV): contatos de órgãos de apoio, inventário de abrigos municipais e histórico descritivo de ocorrências
- APIs/Json: Boletins meteorológicos
- Dados geográficos(GeoJSON): mapeamento de áreas de risco

### **- Qual o volume aproximado? (dezenas, centenas, milhares de documentos?)**

Dezenas a centenas de documentos por município

### **- Qual o tamanho típico de cada documento? (Paginas, kbs)**

Os planos de contingência e manuais técnicos costumam ser densos, variando de 20 a 150 páginas (alguns megabytes por arquivo PDF).

### **- Com que frequência novos documentos entram? Documentos antigos são atualizados ou substituídos?**

Baixa frequência no dia a dia, mas pontual durante eventos climáticos severos

**Proponha uma organização de pastas que faça sentido para o problema escolhido:**

```
documentos/
├── planos_contingencia/
├── mapeamento_risco/
├── diretrizes_legais/
├── recursos_apoio/
└── historico_eventos/
```

**Justifique a estrutura: por que essa divisão e não outra? A organização escolhida deve ter relação com como o usuário pensa a informação, e com os filtros que você vai querer aplicar mais tarde.**

1. Você pode filtrar por diretórios. Se a pergunta é sobre onde evacuar, o sistema deve priorizar 01_planos_contingencia e 04_recursos_apoio. Se a pergunta é sobre legalidade, ele busca em 03_diretrizes_legais.
2. O operador pensa em Ação (Plano), Local (Área de risco) ou Meio (Abrigo/Contato). A estrutura espelha essas necessidades.

### - Existe documento que **não deve** entrar na base? (informação sigilosa, dado pessoal, versão obsoleta) Como você impediria a entrada?

- Dados de pessoas
- Documentos antigos
- Documentos sigilosos, aqueles que nem todos os servidores poderiam ter acesso.

A entrada seria impedida ao não fazer um upload automático, axistindo um processo de aprovação

### - Como você lidaria com **versões** do mesmo documento? Se a política de férias mudou em 2026, o sistema pode recuperar a versão de 2024 e responder errado.

1. Adição de metadados nos documentos, ano, versão, status, data de vigencia. Assim pode ser usado um filtro ao fazer a pesquisa.
2. Janela de contexto.

## _Parte 3 - Pipeline de ingestão_

Projete o processo que transforma os documentos originais em informação pesquisavel.

### **3.1 Extração**

**- Como o texto seria extraído?**

- Usando bibliotecas em Python como PyMuPDF ou pdfplumber para textos e ferramentas de OCR para camadas visuais.
- Como os documentos variam desde PDFs modernos até cópias digitalizadas de decretos antigos, o pipeline precisa detectar o tipo de arquivo logo na entrada para direcionar para o extrator correto.

**- Como você trataria PDFs com texto selecionável?**

- Utilizar bibliotecas de extração direta de texto estruturado (como PyMuPDF ou pdfplumber).
- O extrator precisa isolar o corpo de texto principal e descartar ruídos repetitivos que poluem o vetor.

**- E PDFs digitalizados (imagem escaneada, sem camada de texto)?**

- O documento passa por um motor de OCR (Reconhecimento Óptico de Caracteres) antes de ir para o banco. Ferramentas como Tesseract OCR ou soluções baseadas em visão computacional

**- Como trataria tabelas? (é importante manter?)**

- Mantendo, preservando, são importantes.
- Utilizar extratores especializados em tabelas (como pdfplumber ou ferramentas baseadas em IA como Marker ou Unstructured)

  **- Como trataria imagens? (posso descartar? quais informações elas tem?)**

- Geralmente importantes, por conter mapas.

- Utilizar um modelo multimodal (como o GPT-4o mini, Claude 3.5 Sonnet ou modelos open-source de visão) para gerar uma descrição textual detalhada (captioning) da imagem. O texto gerado (ex: "Mapa indicando que a rota de fuga da Rua X deve seguir em direção à Escola Municipal Y" ) é o que será indexado no RAG.

  **- Como trataria documentos multimodais?(multimodais = texto + imagem, audio + video, texto + video e etc)**

- O documento multimodal é fatiado mantendo a proximidade contextual. Quando o extrator encontra uma imagem ou gráfico em meio a um parágrafo explicativo sobre o transbordamento de um rio, o texto gerado pela descrição da imagem é inserido imediatamente abaixo ou acima do texto correspondente, preservando a coesão que o operador precisa na hora da crise.

**- Explique quais problemas podem surgir durante a extração**

1. Quebra de layout em colunas | Usar ferramentas de layout-aware parsing (como LayoutParser ou parsers baseados em IA)
2. Perda de formatação de listas e tópicos: | Passos de evacuação numerados (1, 2, 3)
3. Tabelas complexas sem bordas visíveis| Tabelas mal formatadas em PDFs antigos viram blocos de texto ilegíveis onde os números de telefone se misturam com os nomes dos responsáveis pelos abrigos.

### **3.2 Limpeza e normalização**

**- O que precisa ser removido? (cabeçalhos e rodapés repetidos, numeração de página, marcas d'água, sumário, referências)**

1. Cabeçalhos e rodapés repetidos
2. Numeração de página dispersa
3. Marcas d'água
4. Sumário e índice remissivo
5. Referências bibliográficas e normativas longas e repetitivas

**- O que precisa ser padronizado? (acentuação, quebras de linha, espaçamento, codificação)**

6. Acentuação e codificação
7. Quebras de linha forçadas
8. Espaçamento excessivo e caracteres especiais
9. Padronização de termos críticos

**- Que informação você corre o risco de **perder** ao limpar demais?**

1. Dados numéricos e códigos de referência
2. Unidades de medida (mm/h)
3. Restrições e condicionais presentes nos rodapés

### **3.3 Frequência de ingestão**

**- O pipeline roda uma vez, sob demanda, ou de forma agendada? Com que frequência chegam novos documentos?**
O pipeline de ingestão deve operar de forma mista (agendada e sob demanda) devido à natureza dinâmica da Defesa Civil:

**- Quando um documento é atualizado, você reprocessa **só ele** ou a base inteira? Como sabe qual reprocessar?**
Reprocessamento direcionado (Apenas o documento alterado): Jamais reprocessa-se a base inteira,

1. Controle por Hash (MD5/SHA-256)
2. Controle por Metadados e ID Único

## _Parte 4 - Metadados_

Defina quais metadados seriam armazenados.

### **4.1 Metadados do documento**

```json
{
  "document_id": "doc_defesa_042",
  "title": "Plano de Contingência Municipal de Proteção e Defesa Civil - Edição 2026",
  "author": "Coordenadoria Municipal de Defesa Civil (COMPDEC)",
  "source": "/documentos/01_planos_contingencia/plano_2026.pdf",
  "document_type": "plano_contingencia",
  "created_at": "2026-01-15",
  "updated_at": "2026-03-10",
  "category": "operacional"
}
```

1. `document_id`: Identificador único essencial para rastreabilidade e para realizar exclusões em lote quando um documento precisar ser atualizado.

2. `title`: Crucial para referências textuais e para o operador identificar de qual plano ou manual a resposta se originou.

3. `author`: Identifica o órgão emissor oficial, garantindo a confiabilidade institucional da diretriz.

4. `source`: Indica o caminho físico ou lógico do arquivo original, permitindo auditoria humana rápida.

5. `document_type`: Permite classificar o arquivo (ex: plano de contingencia, decreto, mapa de risco), viabilizando filtros macro de escopo.

6. `created_at / updated_at`: Fundamentais para garantir a temporalidade da informação, evitando que o modelo recupere diretrizes caducas.

7. `category`: Agrupa o documento em macro-funções operacionais (ex: operacional, legal, geográfico).

### **4.2 Metadados do chunk**

```json
{
  "document_id": "doc_defesa_042",
  "chunk_id": "doc_defesa_042-015",
  "page": 15,
  "section": "Rotas de Fuga e Zonas de Evacuação - Bairro Vila Nova",
  "document_type": "plano_contingencia",
  "text": "..."
}
```

1. `document_id`: Relaciona diretamente o fragmento ao seu documento de origem.

2. `chunk_id`: Identifica o trecho exato vetorizado, facilitando o debug e a verificação de qual parte do texto gerou a resposta.

3. `page`: Informação indispensável para a citação de fonte, permitindo que o operador abra o PDF exatamente na página correta durante a crise.

4. `section`: Contextualiza semanticamente o trecho, ajudando o modelo a entender o subtema (ex: se o fragmento fala sobre abrigos ou rotas de fuga).

5. `document_type`: Herda a tipologia do documento para manter o escopo restrito nos filtros de busca.

6. `text`: O conteúdo textual efetivo vetorizado e disponibilizado para o LLM.

**- Quais metadados você usaria para **filtrar** a busca? Dê um exemplo de pergunta em que o filtro é indispensável.**

- Metadados de filtro: document_type, category e document_id
- Exemplo de pergunta indispensável: "Segundo o decreto oficial mais recente, qual é o protocolo de acionamento de alerta para o Bairro Centro?"

**- Quais metadados você usaria para **citar a fonte** ao usuário? O que exatamente apareceria na tela junto da resposta?**

- Metadados usados: title, page e section
- Junta a resposta da IA terá um secção de referência, como:
  Fonte consultada: Plano de Contingência Municipal - Edição 2026 (COMPDEC) | Seção: Rotas de Fuga e Zonas de Evacuação - Bairro Vila Nova | Página: 15

**- Que metadado seria caríssimo de acrescentar depois que a base já estivesse indexada? Por quê?**

- Metadados estruturais profundos ou derivativos de negócio (como uma classificação de nível de criticidade do risco por bairro ou tags de geolocalização por polígono que não estavam no texto original).
- Porque exigiria reprocessar, reescrever e re-vetorizar (gerando novas chamadas de API de embedding para) todos os chunks de todos os documentos já indexados na base, além de demandar um esforço manual ou computacional massivo para reclassificar o conteúdo que já está armazenado.

**- Como você vai extrair esses metadados**

- Metadados estruturais básicos (document_id, source, created_at, document_type): Extraídos de forma programática via código (Python) no momento da leitura do arquivo no sistema de arquivos ou por meio de regras de cadastro no painel de ingestão.

- Metadados contextuais internos (title, section, page): Extraídos diretamente durante o processo de parsing do PDF (usando bibliotecas como PyMuPDF para ler cabeçalhos, sumários e metadados nativos do documento, ou estruturados via chamadas controladas a LLMs leves / parsers inteligentes durante a limpeza inicial).

## _Parte 5 - Chunking / Splitting_

Defina como os documentos serão divididos.

- Ajuda da IA para melhor compreender e responder

**- Qual estratégia de splitting você utilizaria?**
Abordagem: Utilizar uma estratégia de Chunking Semântico combinado com um Splitter Recursivo baseado em tokens/caracteres (como o RecursiveCharacterTextSplitter do LangChain).

Por quê? Os planos de contingência, manuais e decretos possuem uma hierarquia natural muito clara (títulos, subtítulos, seções e parágrafos). O splitter recursivo tenta quebrar o texto primeiro em divisores lógicos maiores (quebras de parágrafo \n\n, depois quebras de linha \n, depois espaços), garantindo que um parágrafo conceitual sobre uma rota de fuga não seja cortado abruptamente no meio de uma frase.

**- Qual tamanho aproximado dos chunks?**

- Aproximadamente 2000 a 4000 caracteres

**- Utilizaria overlap? Quanto?**
Sim.

- Utilizaria um overlap (sobreposição) de aproximadamente 10% a 15% do tamanho do chunk (cerca de 100 a 150 tokens).

**- A divisão seria por caracteres, palavras, sentenças, parágrafos ou seções?**
A divisão é híbrida e hierárquica: prioriza-se quebras estruturais por seções e parágrafos lógicos, utilizando contagem de tokens para limitar o teto máximo de tamanho de cada fragmento.

**- Utilizaria um splitter recursivo?**
Sim.

- É a prática recomendada de mercado, pois ele avalia uma lista de separadores em ordem de prioridade (parágrafos, linhas, espaços) para que os blocos respeitem ao máximo a semântica natural da linguagem escrita nos manuais.

**- Utilizaria uma estratégia **específica para cada tipo de documento**? Um contrato e uma transcrição de call center pedem o mesmo tratamento?**
Não, o tratamento deve ser diferenciado.

- Decretos e Manuais Técnicos: Exigem divisões estritamente baseadas em seções, artigos e parágrafos normativos, pois o contexto legal e estrutural precisa ser preservado em blocos coesos.
- Relatórios de Ocorrências e Descrições Curtas: Podem usar tamanhos menores de chunks ou divisões baseadas em eventos/datas, dado que consistem em blocos informativos mais diretos.

**Responder:**

**- O que pode acontecer se os chunks forem muito pequenos?**

- O modelo perde o contexto global.

**- O que pode acontecer se os chunks forem muito grandes?**

- Ocorre a diluição da relevância.

**- Como você trataria uma **tabela** na hora de dividir? Uma tabela cortada ao meio ainda significa alguma coisa? e uma imagem?**

- As tabelas (como listas de abrigos e capacidades) nunca devem ser fatiadas no meio por um splitter de texto comum, pois isso destruiria a relação entre as colunas e as linhas.
- Como a imagem foi convertida em texto descritivo (captioning via modelo multimodal) na etapa de extração, esse texto descritivo é tratado como um parágrafo comum e inserido no fluxo de chunking próximo à sua menção no documento, garantindo que o contexto visual seja recuperado semanticamente.

**- Como saber se a sua escolha de chunking foi boa? Que evidência você juntaria para provar isso?**

- Testes de Recuperação (Hit Rate / Precision@K)
- Avaliação de Resposta (Faithfulness / Relevância)

## _Parte 6 - Embeddings_

<!-- prettier-ignore -->
| Item                            | Resposta                            |
| ---                             | ----------                          |
|Modelo escolhido                 | text-embedding-3-small (OpenAI)     |
|Dimensão do embedding            | 1536 dimensões (com suporte nativo a redução via parâmetro) |
|Suporta português?               | Sim                                 |
|É multilíngue?                   | Sim (suporta dezenas de línguas com forte desempenho no português) |
|Tamanho máximo de entrada        | 8191 tokens                         |
|É open source?                   | Não                                 |
|Pode ser executado localmente?   | Não (exige consumo via API proprietária) |
|Possui API?                      | Sim                                 |
|Custo aproximado                 | US$ 0,02 por 1 milhão de tokens     |
|Fonte da informação              | OpenAI API Docs - Vector Embeddings |

**por que esse modelo é adequado ao seu cenário?**
O modelo text-embedding-3-small se encaixa perfeitamente na análise de planos de contingência e alertas de Defesa Civil por aliar alta precisão semântica multibilíngue a um custo operacional extremamente baixo. Planos municipais usam termos técnicos específicos, nomes de bairros, siglas de órgãos (COMPDEC, INMET) e descrições geográficas complexas. O modelo possui excelente capacidade de mapear sinônimos e relações contextuais em português, garantindo que buscas por termos informais feitos por operadores sob estresse encontrem o parágrafo normativo correto nos manuais técnicos.

### **- Considerou algum modelo alternativo e descartou? Qual, e por quê?**

Descartados: text-embedding-3-large e modelos open-source locais como o intfloat/multilingual-e5-large

- text-embedding-3-large: Gerar vetores de 3072 dimensões, o que aumenta o consumo de armazenamento e o custo de computação sem trazer um ganho crítico de precisão para textos normativos diretos.
- Os modelos open-source locais foram secundarizados para este perfil de projeto caso a prefeitura não exija restrições severas de infraestrutura em nuvem, embora o E5-large seja uma excelente opção caso o projeto migre para 100% on-premise

### **- Se o cenário envolve documentos sigilosos, isso muda sua escolha entre modelo local e API? Como?**

Sim, muda completamente.

- Se os planos de contingência envolverem dados estratégicos de segurança nacional, infraestruturas críticas municipais sensíveis ou decretos sob sigilo restrito que não possam trafegar por servidores de terceiros (provedores de API em nuvem pública), a escolha obrigatoriamente se deslocaria para um modelo open-source executado localmente (como o multilingual-e5-large ou BGE-m3)

### **- O tamanho máximo de entrada do modelo tem relação com a sua decisão de chunking da Parte 5? Explique.**

Sim

- O modelo suporta até 8191 tokens por chamada de embedding. Como a estratégia de chunking definida na Parte 5 fixa os blocos entre 500 e 1000 tokens (com overlap de 10% a 15%), cada chunk fica muito abaixo do limite máximo do modelo. Isso garante que o vetor gerado represente uma unidade semântica coesa, sem risco de truncamento de texto e preservando a precisão cirúrgica na recuperação das rotas de fuga e abrigos.

## _Arquitetura final_

### **1. **Um diagrama** do sistema completo, do documento original até a resposta ao usuário. Pode ser desenho, ferramenta de diagramação ou ASCII - o que importa é estar legível e completo.**

<!-- prettier-ignore -->
```
+-------------------+       +---------------------+       +-----------------------+
|  Fontes de Dados  |       | Pipeline de Ingestão|       | Armazenamento & Base  |
|                   |       |                     |       |                       |
| - PDFs/Manuais    |------>| - Extração (OCR/PDF)|------>| - Banco Relacional    |
| - Mapas de Risco  |       | - Limpeza & Normal. |       | - Banco Vetorial      |
| - APIs Clima      |       | - Chunking Semântico|       |   (Embeddings)        |
+-------------------+       +---------------------+       +-----------------------+
                                                                      |
                                                                      v
+-------------------+       +---------------------+       +-----------------------+
| Resposta ao User  |       | Orquestração & LLM  |       | Fase de Recuperação   |
|                   |       |                     |       |                       |
| - Texto orientativo|<-----| - Prompt Especializ.|<-----| - Busca Híbrida       |
| - Fontes e Páginas|       | - Geração Final     |       | - Filtro de Metadados |
+-------------------+       +---------------------+       +-----------------------+
```

### **Uma tabela de decisões, reunindo tudo:**

<!-- prettier-ignore -->
| Etapa      | Decisão | Justificativa em uma linha |
| ---------- | ------- | -------------------------- |
| Extração   | Abordagem híbrida (PyMuPDF + OCR + Parser de Tabelas) | Garante a captura correta de textos corridos, tabelas de abrigos e mapas em PDFs complexos. |
| Limpeza    | Remoção de cabeçalhos, rodapés, sumários e conversão UTF-8 | Elimina ruídos repetitivos que poluem os vetores sem perder dados numéricos ou normativos críticos. |
| Chunking   | Splitter Recursivo estruturado por seções (500-1000 tokens com 10% overlap) | Mantém a coesão semântica de parágrafos e procedimentos de evacuação sem estourar o contexto. |
| Metadados  | Uso de IDs, tipos de documento, seções, páginas e datas de vigência |  Permite filtros de busca rigorosos e citação exata de fontes para auditoria em crises.|
| Embeddings | text-embedding-3-small (ou modelo multilíngue local equivalente) |Oferece alta precisão semântica para o vocabulário técnico e geográfico em português. |

### **Riscos e Limitações da Proposta**

1. Cálculos Quantitativos Complexos em Tempo Real:
2. Dados Geográficos Dinâmicos e Esp Laciais Brutos:
3. Lentidão de Processamento em Formatos Visuais Complexos
