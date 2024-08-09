import pandas as pd
import matplotlib.pyplot as plt

dados = pd.read_csv('dados_dengue.csv')
ano = dados['ano']
casos = dados['casos', 'graves']
#print(dados)
pd.DataFrame(dados, index=ano, columns=casos)

graves = dados['graves']
plt.bar(ano,casos)
plt.bar(ano,graves, color='Red')
plt.xlabel('Ano')
plt.ylabel('Número de Casos')
plt.show()

# Gráfico de dispersão
#plt.scatter