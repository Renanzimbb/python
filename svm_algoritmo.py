from sklearn.svm import SVC
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np
from sklearn.preprocessing import OneHotEncoder

df = pd.read_csv('dados_dengue2.csv')
f = df.drop('graves', axis =1)
c = df.graves

#selecionar somente os objetos categoricos de f
categoricos = f.select_dtypes(include='object')


###########-------- Função para fazer binarização ------############

onehot = OneHotEncoder(sparse=False, drop='first')
binarizados = onehot.fit_transform(categoricos)
juntos = np.append(f,binarizados, axis = 1)


f_train, f_teste, c_train, c_teste = train_test_split(f,c,train_size=2/3)

############-------- Máquina de Vetor Suporte ------############
svm = SVC()
svm.fit(f_train,c_train)
print(accuracy_score(c_teste,svm.predict(f_teste)))