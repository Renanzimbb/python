from sklearn.datasets import load_digits
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
digitos = load_digits()

# Exercicio 01 - Carregadr dados da base load_digits. Informar a quantidade de dados.

# Existem 1797 imagens, sendo que cada uma tem uma dimensão 8 x 8 = 64
print("Shape dos dados de imagens:{}".format(digitos.data.shape))
# Apresentar o total de dados rotulados com inteiros de 0 a 9
print("Shape dos dados rotulados: {}".format(digitos.target.shape))

plt.figure(figsize=(14,4))
for index, (imagem,rotulo) in enumerate(zip(digitos.data[0:5],
                                            digitos.target[0:5])):
    plt.subplot(1,5,index + 1)
    plt.imshow(np.reshape(imagem, (8,8)),
           cmap=plt.cm.gray)
    plt.title('Treinamento: {}\n'.format(rotulo,fontsize = 15))


