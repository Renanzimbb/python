import matplotlib.pyplot as plt

#plt.plot([1,2,3,4], [5,6,7,8])
#plt.show()

x = [1,2,3,4,5,6]
y = [2,6,8,7,20,22]
y2 = [5,9,6,20,24,22]

plt.plot(x,y, '--', color='Green', label ='Maria')
plt.plot(x,y2, '--', color='Red', label ='João')
plt.legend()
plt.grid()
plt.scatter(x,y, color='Red')
plt.scatter(x,y2, color='Black')
# plt.axis([0,15,0,30])
plt.title('Exemplo de gráfico')
plt.xlabel('Ano')
plt.ylabel('Produtos')
plt.show()
