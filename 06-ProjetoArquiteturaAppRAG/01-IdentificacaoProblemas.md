# Parte 1 - Identificação dos problemas

Aluna: Patrícia Zan de Oliveira

## Objetivo Atividade

Avaliar sua capacidade de compreender **quando, por que e como** utilizar RAG em uma aplicação real.

Você deverá escolher **2 cenários diferentes** nos quais uma arquitetura RAG poderia ser utilizada e projetar, para cada um, uma solução completa, desde a entrada dos documentos até a geração da resposta pelo modelo de linguagem.

Esta é uma atividade de **projeto**, não de implementação. Não é preciso escrever código. O que se espera é arquitetura, decisão e justificativa.

### Escolha dos cenários

Os dois cenários devem ser **substancialmente diferentes** entre si - não escolha "FAQ de uma loja de roupas" e "FAQ de uma loja de eletrônicos". Bons contrastes envolvem diferenças em tipo de documento, volume, frequência de atualização, criticidade do erro ou perfil do usuário.

Escolha cenários sobre os quais você tenha alguma familiaridade real. Um cenário que você conhece de perto produz decisões muito melhores que um cenário genérico.

---

## **1. Sistema de Análise de Desempenho e Prontuário Fisiológico Privado de uma Equipe Profissional ou Atleta Pessoal**

Vindo da junção com um projeto pessoal "ProCore" que estou desenvolvendo envolvendo "Atividades fisicas para treino estruturado".  
Em um futuro a implementação de treinadores e seus atletas ou times.

Utilizando documentos de treinos estruturados criados pelo treinador ou atleta e documentações geradas pelo app e atletas com descrição rica de cada atividade e blocos de treinos, podendo assim cruzar informações de cenários de sucesso, fadiga, lesão.

### **- Qual é o problema que você deseja resolver?**

Analise pessoal/profissional dos dados gerados pelo atleta na plataforma após atividades:

- Descrição da fadiga durante atividade.
- Descrição da alimentação.
- Descriição de sentimentos e fisiologia.
- Observações.

### **- Quem utilizaria a aplicação? Descreva o usuário concretamente: cargo, contexto de uso, nível técnico.**

<!-- prettier-ignore -->
| Cargo                 | Nível Técnico | Contexto          |
| --------------------- | ------------- | ----------------  |
| Atletas Amadores      | Baixo         | Pessoas que buscam entender melhor a relação fadiga X volume treino |
| Atletas Profissionais | Médio         | Atletas que buscam entender a relação fadiga X Carga X Lesões e ao planejamento estruturado de blocos de treino |
| Treinadores           | Alto          | Profissionais que desejam ter maior controle sobre seus atletas, entendendo melhor a relação das cargas e blocos de treinos com a fadiga e lesões apresentadas por cada integrante, melhorando assim de forma individual cada bloco de treino para que se adapte a cada atleta. |

### **- Que tipo de informação o usuário gostaria de consultar?**

1. Carga de Treinos.
2. Relação Fatiga X Treinos realizados.
3. Relação Melhoria X Treinos Realizados.
4. Com o tempo e dados a possibilidade de construção de tipos de treinos corretos.

### **- De onde vêm essas informações?**

Banco de dados da aplicação, dados como:

1. Kilometragem (xml)
2. Tempo de treino (xml)
3. Zonas (xml)
4. Tempo acumulado em Zonas (xml)
5. Descrição de sentimentos da atividade (preenchimento do usuário)
6. Dados metereologicos (api)
7. Gerado a cada 7/15/mês decorrido/bloco de treino. (app)
8. Descrição do usuário, idade,peso,altura,zonas,genero. (preenchimento do usuário)

### **- Por que utilizar um LLM sozinho não seria suficiente?**

- As informações obtidas de treinos são pessoais, estas que serão geradas por métricas.
- As informações de tipos de treinos construidas por Treinadores geralmente são feitas especialmente para cada atleta.
- Fazer a correlação Treino X Treino Executado X Resultados acabam sendo muitas informações para um LLM comum.

### **- Como o usuário vai utilizar o sistema? (API, aplicativo, interface web?)**

- Interface Web.
- Atualmente uma demo teste de processamento de dados existe com ReactJS, NodeJS, Python, supabase.

### **Escreva também **três perguntas reais** que um usuário faria ao sistema. Perguntas concretas, do jeito que a pessoa falaria - não títulos de tópico.**

1. Eu tenho o garmin, strava ou qualquer coisa, por que usaria isso?

- Aqui você terá métricas de "sentimentos" com descrições, levando ao melhor entedimento do sucesso ou fadiga, lesão.

2. Eu tenho 30 atletas, oque isso me beneficia?

- Métricas detalhadas do desempenho de cada indivíduo com base nos seuas dados, cruzando com os dados de seus tipos de treinos construídos, trazendo assim uma melhor chance de prevenção de lesões e fadiga.

3. Muita coisa para ficar escrevendo, porque eu perderia meu tempo?

- Quer treinar ou não? Quer saber se vai quebrar na fadiga antes de acontecer ou não? :D
- Metrícas são ótimas para entender como melhorar os treinos.

---

## **2. Análise de Alertas de Defesa Civil e Planos de Contingência Municipais**

Cruzar dados de previsão de volumes de chuvas, ventos com dados de Municípios como:

### **- Qual é o problema que você deseja resolver?**

Ajudar a defesa civil de cada município a cruzar as informações de volumes e situações de chuvas esperados com os dados mapeados de áreas de rios propensos a alagamentos ou possivéis danos por vento e granizo.
Além de buscar documentos de planos de contingência e ação para rápido deslocamento de ajuda as pessoas afetadas.

### **- Quem utilizaria a aplicação? Descreva o usuário concretamente: cargo, contexto de uso, nível técnico.**

<!-- prettier-ignore -->
| Cargo        | Nível Técnico | Contexto |
| ------------ | ------------- | ---|
| Defesa Civil | Alto          | Com o cruzamento dos dados e o alerta de áreas de risco fazendo assim uma preparação para possivéis emergências com documentações municipais |
| Bombeiros   | Médio         | Por meio das informações ativar medidas para preparo de ocorrências                                                                          |
| Cidadão      | Baixo         | Por meio de alertas recebidos com melhor detalhamento                                                                                        |

### **- Que tipo de informação o usuário gostaria de consultar?**

<!-- prettier-ignore -->
| Cargo        |Informação  |
| ------------ | -- |
| Defesa Civil | Alerta de correlação - Volume esperado para capacidade de locais(rios/lagos), para locais de risco de danos (bairros com árvores, casas com menor infraestrutura adequada) - Plano de ação para resgate e ajuda. |
| Bombeiros    | histórico de ocorrencias com medidas tomadas, molhorando o preparo e tempo de resposta |
| Cidadão      | Alertas para as areas que estão sob risco  |

### **- De onde vêm essas informações?**

Informações cadastradas pelas prefeituras e orgãos competentes.

### **- Por que utilizar um LLM sozinho não seria suficiente?**

As informações e documentações de áreas de risco geralmente são guardadas em banco de dados de competência dos orgãos responsáveis.  
As infomações de previsão do tempo são voláteis e mudam o tempo todo, assim teriam um sistema pronto para analisar o risco de alagamentos/desastres.

### **- Como o usuário vai utilizar o sistema? (API, aplicativo, interface web?)**

Sistema de alerta automático com a relação Previsão do tempo X Histórico X Dados áreas de risco X Dados de contingência.  
Sistema mobile?  
Alertas no celular.

### **Escreva também **três perguntas reais** que um usuário faria ao sistema. Perguntas concretas, do jeito que a pessoa falaria - não títulos de tópico.**

1. Eu já tenho planos de emergencia na cidade disse 'O senhor prefeito', somos competentes.

   Espero que sim, porém o cruzamento dos dados pode ajudar a formar uma equipe para alerta, resgate, ajuda muito mais rápida e INFORMADA com os planos existentes.

2. Mas minha cidade não tem um mapeamento de áreas de risco, e agora?  
   El niño batendo na porta e não investiu em uma documentação para proteger sua população?  
   Realizar uma documentação pode ser o primeiro passo para ter um plano e ajuda as pessoas.

3. Isso não assustaria as pessoas?  
   Não, ao contrário, alertas podem ser emitidos após aprovação.  
   Inicialmente os dados resultantes ficariam em mão de "oficiais" que farão a analise da previsão X realidade.  
   E o objetivo principal é cruzar os dados das previsões com a documentação de área de risco e documentação de prevenção/ação.
