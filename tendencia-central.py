import statistics

comprimento = [5,2,3,4,1]
print(comprimento)

# Média aritmética
soma = (sum(comprimento))
n = len(comprimento)
media = soma / n
print(media)

 # Média aritmética usando mean() da biblioteca statistics
media = statistics.mean(comprimento)
print(media)

# Valor máximo do vetor
minimo = min(comprimento)

# Valor mínimo do vetor
maximo = max(comprimento)

# MEDIANA
mediana = statistics.median(comprimento)

# MODA
moda = statistics.mode(comprimento)
print('Moda:', moda)

print("Valor Minimo:",minimo)
print("Valor Maximo:",maximo)
print("Mediana:",mediana)

grupo = ["Carlos", "Maria", "Silva", "Daniel", "Ana"]
lista = list(grupo)
print(lista)


# Função retorna TRUE OR FALSE para números pares
numeros = [1,2,3,4,5,6,7.8]
pares = [num % 2 == 0 for num in numeros]
print(pares)
