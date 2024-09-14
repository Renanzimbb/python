# Implementar uma solução em Python para estudar o comportamento de uma série  temporal com Regressão Linear
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
import pandas as pd


teste = pd.read_csv('rani3.csv', sep=",")

x = teste[['Abertura']]
y = teste[['Fechamento']]

model = LinearRegression().fit(X=x,y=y)

# Predict a Response and print it:

abertura_hoje = [[8.88]]
preco = model.predict(abertura_hoje)
print(preco)
