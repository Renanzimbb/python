import pandas as pd
#PANDAS é uma biblioteca para manipulação e análise de dados, escrita em Python.
#pd.read_csv('dsdsds.csv')
#pd.read_excel('vendas_julho.xlsx')

#dataFrame de lista
dados =  [['Julio', 30], ['Maria', 22], ['Jose', 12], ['Joana', 33], ['Tulio', 99]]
print (dados)
df = pd.DataFrame(dados,columns=['Nome', 'Idade'])
print (df)
print('--' * 20)

#dataframe de Dicionario
dicionario ={'Nome': ['Maria' , 'Jose', "Douglas"],
             'Idade': [10,20,30]}
df2 = pd.DataFrame(dicionario)
print(df2)
print('--' * 20)

#Lendo arquivos de dados
# pd.read_[extensão]
# pd.read_excel()
# pd.read csv('vendas.csv', set=';')
df3 = pd.read_csv('dados_dengue.csv')
print(df3)
print('--' * 20)
# Mostrar somente primeiras linhas
print(df3.head(3))
print('--' * 20)
# Transposição dos dados colunasx s linhas
print(df3.T)
print('--' * 20)
#Dimensões do DF - Retorna a quantidade de linhas e colunas
print(df.shape)
print('--' * 20)
#informações do dataframe
print(df.info)
print('--' * 20)
#Retorna medidas de tendência centralr
print(df.describe())
print('--' * 20)
#Filtrar por dado que qeu quero mostrar
print(df[(df['Nome']=='Maria')])
print(df[df['Idade']>50])
print('--' * 20)
#metodo loc, mostra de n linha ate n linha
print(df.loc[1:2])
print('--' * 20)
#adicionar coluna
df ['Sexo'] = 'Masculino'
df ['Comissão'] = df ['Idade'] * 3
print(df)
print('--' * 20)
#deletar coluna
del df['Sexo']
print(df)
print('--' * 20)
#deletar linha
df.drop(2)
print(df)
#Pivotando: Melhorar a vizualização dos dados
x = pd.pivot_table(df, index=['Nome'])
print(x)
#value counts
# Vai contar qtos registros aparecem com a loja: df['Loja'].value_counts()

#groupby
# vendas_loja = df[['Loja', 'Preço Unitário']].groupby('Loja').sum()