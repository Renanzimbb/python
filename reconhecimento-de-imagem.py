import modelo as modelo
import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

fashion_mnist = keras.datasets.fashion_mnist
(treinamento_imagens, treinamento_rotulos), (teste_imagens, teste_rotulos) = fashion_mnist.load_data()
nomes_classes = ['T- shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat','Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

print(f'(total de imagens, dimensão 1, dimensão 2)={treinamento_imagens.shape}')
print(f'rótulos={treinamento_rotulos} - São rotulados nas classes 0, 1, 2, 3, ...,9')
print(f'(total de imagens para teste, dimensão 1, dimensão 2)={teste_imagens.shape}')


plt.figure()
plt.imshow(treinamento_imagens[0])
plt.colorbar()
plt.grid(False)
plt.show()
print('Explicação: exibindo a primeira imagem da base. Os dados numéricos se referem aos Pixels de 0 a 255.')

treinamento_images = treinamento_imagens / 255.0
teste_imagens = teste_imagens / 255.0

plt.figure(figsize=(13,13))
for i in range(20):
 plt.subplot(5,5,i+1)
 plt.xticks([])
 plt.yticks([])
 plt.grid(False)
 plt.imshow(treinamento_imagens[i], cmap=plt.cm.binary)
 plt.xlabel(nomes_classes[treinamento_rotulos[i]])
plt.show()

modelo = keras.Sequential([
keras.layers.Flatten(input_shape=(28, 28)),
keras.layers.Dense(128, activation=tf.nn.relu),
keras.layers.Dense(10, activation=tf.nn.softmax)
])

modelo.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])
modelo.fit(treinamento_imagens, treinamento_rotulos, epochs=50)


modelo.fit(treinamento_imagens,
 treinamento_rotulos,
 epochs=50)

perda_teste, precisao_teste = modelo.evaluate(teste_imagens, teste_rotulos)
print('Precisão dos Testes:', precisao_teste)


predicoes = modelo.predict(teste_imagens)

predicoes[0]

melhor_classificacao=np.argmax(predicoes[0])
print(f'Posição do melhor resultado da primeira imagem de teste: {melhor_classificacao}')

plt.figure(figsize=(14,4))
plt.imshow(np.reshape(teste_imagens[melhor_classificacao], (28,28)), cmap=plt.cm.gray)
plt.title(nomes_classes[teste_rotulos[melhor_classificacao]])
