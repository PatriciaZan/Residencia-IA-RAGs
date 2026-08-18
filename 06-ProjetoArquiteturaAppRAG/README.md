# Projeto e Arquitetura de uma Aplicação RAG | 14/08 - 17/08

Aluna: Patrícia Zan de Oliveira

## 🛠 Como navegar neste repositório

A leitura dos dois cenarios pode ser feita nas pastas correspondentes e arquivos README.md

- `01-Cenario_AnaliseDesempenho`: Sistema de Análise de Desempenho e Prontuário Fisiológico Privado de uma Equipe Profissional ou Atleta Pessoal
- `02-Cenario_ContingenciaMunicipal`: Análise de Alertas de Defesa Civil e Planos de Contingência Municipais

## Comparação entre os dois cenários

### Em que pontos as decisões foram diferentes? Por quê?

1. Estrutura de metadados
   Em quanto o cenario ContingenciaMunicipal teve como foco em rastreabilidade institucional e validade legal o cenario AnaliseDesempenho teve em correlação e acesso temporal.

2. Tratamento de Dados de Entrada
   O cenario ContingenciaMunicipal teve a prioridade da preservação da integridade da informação oficial contida em documentos complexos. Já AnaliseDesempenho o foco era o armazenamento de dados brutos e históricos para acesso posterior do usuário ou analise com histórico para LLMs

### Em que pontos foram iguais? Isso é sinal de boa prática geral ou de você ter repetido a decisão sem pensar?

- Arquitetura Híbrida (SQL + RAG): Ambos usam SQL para dados numéricos (somas, médias, métricas) e RAG para o contexto qualitativo (notas, relatórios, diretrizes).
- Uso de Splitter Recursivo: Ambos utilizam essa técnica para respeitar a hierarquia do texto.
- Foco em Filtros por Metadados: Ambos usam metadados para restringir a busca antes da vetorização.

### Se você tivesse que construir apenas um dos dois, qual escolheria, e por quê?

1. Sistema de Análise de Desempenho e Prontuário Fisiológico Privado de uma Equipe Profissional ou Atleta Pessoal

A junção de um projeto em andamento, além de ter um input de dados quase diário que me possibilitaria revisar e melhorar as técnicas de RAG.

Penso também que o segundo cenário "Análise de Alertas de Defesa Civil e Planos de Contingência Municipais" pode ter alguns impedimentos jurídicos que evitariam de proceguir com o uso de dados.
