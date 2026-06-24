# Importa a biblioteca Pandas, utilizada para manipular tabelas de dados
import pandas as pd

# Importa a função que divide os dados em treino e teste
from sklearn.model_selection import train_test_split

# Importa o algoritmo de Regressão Logística
# Apesar do nome, ele é usado para CLASSIFICAÇÃO (sim/não)
from sklearn.linear_model import LogisticRegression

# Importa uma função que gera métricas de avaliação do modelo
from sklearn.metrics import classification_report


# Lê o arquivo CSV e o transforma em um DataFrame (tabela do Pandas)
df = pd.read_csv("base_recuperacao_credito.csv")


# Cria a variável X (variáveis explicativas)
#
# Remove:
# - id_cliente (é apenas um identificador)
# - pagamento_realizado (é o resultado que queremos prever)
#
# get_dummies converte textos em números.
#
# Exemplo:
# WhatsApp -> 1
# Telefone -> 0
#
# Isso é necessário porque algoritmos não trabalham com texto.
X = pd.get_dummies(
    df.drop(columns=["id_cliente", "pagamento_realizado"]),
    drop_first=True
)


# Cria a variável y (alvo do modelo)
#
# O que queremos prever:
# 1 = cliente pagou
# 0 = cliente não pagou
y = df["pagamento_realizado"]


# Divide os dados em treino e teste
#
# X_train -> dados usados para ensinar o modelo
# X_test  -> dados usados para testar o modelo
#
# y_train -> respostas corretas do treino
# y_test  -> respostas corretas do teste
#
# test_size=0.2
# significa que:
# 80% dos dados serão usados para treino
# 20% para teste
#
# random_state=42
# garante que a divisão seja sempre igual
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# Cria o modelo de Regressão Logística
#
# max_iter=1000
# aumenta o número máximo de tentativas
# para encontrar a melhor solução matemática
modelo = LogisticRegression(max_iter=1000)


# Treina o modelo
#
# Aqui ocorre o aprendizado.
#
# O algoritmo analisa:
# renda
# idade
# valor da dívida
# dias de atraso
# canal de contato
#
# e tenta descobrir padrões que indicam
# se um cliente tende a pagar ou não.
modelo.fit(X_train, y_train)


# Faz previsões usando os dados de teste
#
# O modelo responde:
#
# 1 = vai pagar
# 0 = não vai pagar
pred = modelo.predict(X_test)


# Exibe métricas de desempenho
#
# Precision:
# Das previsões positivas, quantas estavam corretas?
#
# Recall:
# Dos clientes que realmente pagaram,
# quantos o modelo conseguiu identificar?
#
# F1-score:
# Média entre precision e recall.
#
# Support:
# Quantidade de exemplos de cada classe.
print(classification_report(y_test, pred))


# Calcula a probabilidade de pagamento
#
# predict_proba retorna duas colunas:
#
# Coluna 0:
# Probabilidade de NÃO pagar
#
# Coluna 1:
# Probabilidade de pagar
#
# [:,1] significa:
# "pegue a segunda coluna para todas as linhas"
df["probabilidade_pagamento"] = modelo.predict_proba(X)[:,1]


# Salva o resultado em um novo CSV
#
# Agora cada cliente terá:
#
# id_cliente
# renda
# dívida
# ...
# probabilidade_pagamento
#
# Exemplo:
# 0.91 = 91% de chance de pagar
# 0.23 = 23% de chance de pagar
df.to_csv("clientes_com_score.csv", index=False)


# Mensagem informando que o arquivo foi criado
print("Arquivo clientes_com_score.csv gerado.")