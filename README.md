# Análise Preditiva para Recuperação de Crédito

## Sobre o Projeto

Este projeto tem como objetivo demonstrar a aplicação de técnicas de Análise de Dados e Machine Learning no contexto de Recuperação de Crédito.

A proposta consiste em analisar uma carteira de clientes inadimplentes e utilizar um modelo preditivo para estimar a probabilidade de pagamento de cada cliente, permitindo a priorização de esforços de cobrança e a tomada de decisões baseada em dados.

O projeto foi desenvolvido para fins educacionais e de portfólio, simulando um cenário encontrado em instituições financeiras, cooperativas de crédito, empresas de cobrança e departamentos financeiros.

---

## Objetivos

* Realizar a análise de uma carteira de crédito.
* Preparar dados para modelagem preditiva.
* Aplicar técnicas de Machine Learning para classificação.
* Estimar a probabilidade de recuperação de crédito.
* Gerar uma base enriquecida para utilização em dashboards e relatórios gerenciais.

---

## Tecnologias Utilizadas

* Python
* Pandas
* NumPy
* Scikit-Learn
* CSV

---

## Estrutura do Projeto

```text
.
├── base_recuperacao_credito.csv
├── analise_recuperacao_credito.py
├── clientes_com_score.csv
└── README.md
```

### Arquivos

#### `base_recuperacao_credito.csv`

Base de dados simulada contendo informações de clientes, dívidas e histórico de cobrança.

#### `analise_recuperacao_credito.py`

Script responsável por:

* Carregar os dados;
* Preparar as variáveis para modelagem;
* Treinar um modelo de Regressão Logística;
* Avaliar o desempenho do modelo;
* Gerar um score de probabilidade de pagamento para cada cliente.

#### `clientes_com_score.csv`

Arquivo gerado pelo modelo contendo a probabilidade estimada de pagamento para cada cliente.

---

## Metodologia

### 1. Carregamento dos Dados

Os dados são importados para um DataFrame utilizando a biblioteca Pandas.

### 2. Preparação dos Dados

As variáveis categóricas são transformadas em variáveis numéricas utilizando One-Hot Encoding através da função `get_dummies()`.

### 3. Divisão Treino/Teste

Os dados são divididos em:

* 80% para treinamento;
* 20% para teste.

### 4. Treinamento do Modelo

Foi utilizada a técnica de Regressão Logística para prever se um cliente possui maior ou menor probabilidade de realizar o pagamento da dívida.

### 5. Avaliação

O desempenho é analisado por meio de métricas como:

* Precision
* Recall
* F1-Score

### 6. Geração do Score

O modelo calcula uma probabilidade de pagamento para cada cliente, gerando um score que pode ser utilizado em processos de cobrança e priorização de contatos.

---

## Como Executar

### Instalar as dependências

```bash
pip install pandas numpy scikit-learn
```

### Executar o projeto

```bash
python analise_recuperacao_credito.py
```

Ao final da execução será gerado o arquivo:

```text
clientes_com_score.csv
```

---

## Finalidade Educacional

Este projeto possui finalidade exclusivamente educacional e de demonstração de portfólio.

Por esse motivo, o código-fonte contém comentários detalhados explicando cada etapa do processo, desde o carregamento dos dados até a geração das previsões. O objetivo é facilitar o aprendizado de estudantes e profissionais iniciantes em Ciência de Dados, Análise de Dados e Machine Learning.

Os dados utilizados são fictícios e não representam informações reais de clientes ou instituições financeiras.

---

## Possíveis Evoluções

* Criação de dashboard em Power BI.
* Utilização de modelos mais avançados (Random Forest, XGBoost).
* Segmentação automática de clientes.
* Análise de estratégias de cobrança.
* Desenvolvimento de score proprietário de recuperação de crédito.
* Integração com banco de dados SQL.

---

## Autor

**Iago Novaes**

Projeto desenvolvido como estudo aplicado de Análise de Dados, Machine Learning e Recuperação de Crédito.
