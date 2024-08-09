from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
from sklearn.model_selection import train_test_split

#função para acurácia
from sklearn.metrics import accuracy_score

df = pd.read_csv('dados_dengue2.csv')

#KNN (k-Vizinhos) algoritmo de classificação - trabalha com vizinhança(k)
#qual o dado mais predominante dentro da vizinhança estabelecida
classificador = KNeighborsClassifier(n_neighbors=3)

#separar as features e a classe classificadora em variáveis
#f de features
f = df.drop('graves', axis = 1)
#c de clase
c = df['graves']

#fit função para fazer o treinamento / treinar o classificador
classificador.fit(f,c)
#função para predizer algum valor
#classificador.predict([[2018, 200]])

# cria variaveis(separa os dados de treino para modelo e teste
f_train, f_teste, c_train, c_teste = train_test_split(f,c, train_size=2/3)
classificador_melhorado = KNeighborsClassifier(n_neighbors=3)
classificador_melhorado.fit(f_train, c_train)
classificador_melhorado.predict(([[2019, 200]]))
print(accuracy_score(c_teste, classificador_melhorado.predict(f_teste)))