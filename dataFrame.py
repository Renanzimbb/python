import pandas as pd
#PANDAS é uma biblioteca para manipulação e análise de dados, escrita em Python.
#pd.read_csv('dsdsds.csv')
#pd.read_excel('vendas_julho.xlsx')

dados = [['Julio', 30], ['Maria', 22], ['Douglas', 12], ['Joana', 33], ['Tulio', 99]]
#df = pd.DataFrame(dados,columns=['Nome', 'Idade'])
planilha = pd.read_csv('dados_dengue.csv')
impressao = pd.DataFrame(planilha,columns=['casos', 'graves'])
#pivot_table troca o index
#print(pd.pivot_table(df, index=['ano']))
print(impressao)

print('--' * 20)
print('##' * 20)

dicionario = {'Nome' :['Maria', 'João', 'Pedro'],
              'Idade' : [10,20,30]}
df2 = pd.DataFrame(dicionario)
pd.pivot_table(df2, index=['Nome'])
print(df2)

print('--' * 20)
print('##' * 20)
print('info')

#Mostra as info do dataframe
#df.info()
print('--' * 20)
print('##' * 20)
print('qt linhas e colunas')

#Retorna a quantidade de linhas e colunas
print(df.shape)


print('--' * 20)
print('##' * 20)
print('medidas de tendência central - describe')

#Retorna medidas de tendência central
#print(df.describe())


print('--' * 20)
print('##' * 20)
print('primeiras linhas')

#Mostra as primeiras linhas
print(df.head(4))

print('--' * 20)
print('##' * 20)
print('transposição de dados')



#Transposição de dados
print(df.T)

print('--' * 20)
print('##' * 20)
print('loc de linha')

print(df.loc[0:7])

