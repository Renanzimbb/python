import matplotlib.pyplot as plt

#gráfico de barras
meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Maio']
temp = [30,31,34,36,40]
plt.scatter(meses,temp, color='Green')
plt.xlabel("Meses do Ano")
plt.ylabel('Temperatura')
plt.title('Temperaturas do Ano')
plt.show()
