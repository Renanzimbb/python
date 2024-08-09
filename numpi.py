import numpy as np
#NUMPY é especialista em trabalhar com array.
#Permite trabalhar com mais de 3 dimensões
#consegue processar muitos números. Muito utilizado em big data, na aritmética computacional, computação matemática.
#Consegue fazer cálculos absurdos dentro dos vetores, matrizes..

# ndarray(array de várias dimensões)

#array de 1 dimensão
numeros = np.array([1,2,3,4,5,6,7,8,9,10])

#array de 2 dimensões
x = np.array([[1,2,3,4,5],[6,7,8,9,'0']])

print(x[1,3])
print(type(x))
print(numeros.ndim)
print(numeros.mean())
print(numeros.sum())

#array de 3 dimensões
cubo = np.array([[[1,3,4,5],[1,3,4,5],[1,3,4,5]]])
numeros_tri = np.array([[[2,34,5,7,3,5,87,43]], [[2,4,56,4,8,24,3,64,]], [[13,321,312,42,23,34,23,31]]])
print('--'*30)
print(numeros_tri)

#soma todos os valores do array
print(numeros_tri.sum())
#media
print(numeros_tri.mean())
#maior valor
print(numeros_tri.max())
#menor valor
print(numeros_tri.min)

print('--'*30)
#função zeros preencha com zeros o array
numeros2 = np.zeros(shape=4)
print(numeros2)
#função zeros preencha com 1(um) o array
#cria 4 dimensoes com 4 colunas e 4 colunas
numeros3 = np.ones(shape=(4,4,4))

#empity pega valores aleatorios
numeros3 = np.empty(shape=(4,4,4))
print(numeros3)
#.shape mostra a estrutura, linhasxcolunas
print('--'*30)
print(numeros3.shape)
# .size mostra o tamanho da matriz(quantos valores há dentro)
print(cubo.size)
# .ndim mostra o número de dimensoes
print(cubo.ndim)

#concatena arrays
ab= np.concatenate()
print(ab)

#funcao arrange (arange(start,stop,step)
#mesmo funcionamento do   in range

y = np.array([[1, 2], [2, 2], [3, 3]])
d = np.median(y, axis=0)
print(d)

