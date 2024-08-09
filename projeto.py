# Importando os módulos
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import metrics
from sklearn.model_selection import train_test_split

#Conjunto de Dados do Repositório de Machine Learning da UCI / Kaggle
# https://www.kaggle.com/uciml/pima-indians-diabetes-database/data
# Carregando o dataset
print("===Carregando o dataset===")
df = pd.read_csv("pima-data.csv")

# Definindo as classes
diabetes_map = {True : 1, False : 0}
# Aplicando o mapeamento ao dataset
df['diabetes'] = df['diabetes'].map(diabetes_map)
# Verificando como os dados estão distribuídos
print()
print("===Verificando como os dados estão distribuídos===")
num_true = len(df.loc[df['diabetes'] == True])
num_false = len(df.loc[df['diabetes'] == False])
print("Número de Casos Verdadeiros: {0} ({1:2.2f}%)".format(num_true, (num_true/ (num_true + num_false)) * 100))
print("Número de Casos Falsos : {0} ({1:2.2f}%)".format(num_false, (num_false/ (num_true + num_false)) * 100))

# Seleção de variáveis preditoras (Feature Selection)
atributos = ['num_preg', 'glucose_conc', 'diastolic_bp', 'thickness', 'insulin', 'bmi', 'diab_pred', 'age']

# Variável a ser prevista
atrib_prev = ['diabetes']

# Criando objetos
X = df[atributos].values
Y = df[atrib_prev].values

# Definindo a taxa de split
split_test_size = 0.30

# Criando dados de treino e de teste
X_treino, X_teste, Y_treino, Y_teste = train_test_split(X,Y, test_size= split_test_size, random_state= 42)

# Imprimindo os resultados
print("{0:0.2f}% nos dados de treino".format((len(X_treino)/len(df.index)) * 100))
print("{0:0.2f}% nos dados de teste".format((len(X_teste)/len(df.index)) * 100))

#Versão do modelo usando Neural Networks MLPClassifier
from sklearn.neural_network import MLPClassifier
modelo_v7 = MLPClassifier(random_state=42)

# Treina o modelo
modelo_v7.fit(X_treino, Y_treino.ravel())
mlp_predict_train = modelo_v7.predict(X_treino)

mlp_predict_test = modelo_v7.predict(X_teste)

print("=========================================================")
print("Exatidão (Accuracy) com os dados de treino do modelo MLPClassifier : {0:.4f}".format(metrics.accuracy_score(Y_treino, mlp_predict_train)))
print("Exatidão (Accuracy) com os dados de teste do modelo MLPClassifier: {0:.4f}".format(metrics.accuracy_score(Y_teste, mlp_predict_test)))
print()
print("Confusion Matrix - Modelo MLPClassifier")
print("{0}".format(metrics.confusion_matrix(Y_teste, mlp_predict_test, labels = [1, 0])))
print()
print("Classification Report MLPClassifier")
print(metrics.classification_report(Y_teste, mlp_predict_test, labels = [1, 0]))
print("=======================================================")