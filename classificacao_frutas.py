from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC

##################      Pré-processamento     ###################
lisa = 1
irregular = 0
pera = 1
laranja = 0

pomar = [[80,lisa],[100,lisa],[120,lisa],[120,lisa], [140, lisa], [180,irregular],
         [210, irregular], [205, irregular],[214, irregular],[208, irregular]]
resultado = [pera,pera,pera, pera,pera,laranja,laranja,laranja,laranja,laranja]

###################       Mineração        #####################

############---------- Arvore de Decisão -----------############

#Gerar árvore de decisão
clf = DecisionTreeClassifier()
#Separa dados de treino(criação do modelo) e para testes futuros
frutas_treino, frutas_teste, resultado_treino, resultado_teste = train_test_split(pomar, resultado)

#classificador
clf = clf.fit(frutas_treino,resultado_treino)
frutas_predicao = clf.predict(frutas_teste)
frutas_acuracia = accuracy_score(resultado_teste, frutas_predicao)

peso = 220
# 1 para lisa e 0 para irregular
superficie = 0
resultado = clf.predict([[peso,superficie]])

############-------- Máquina de Vetor Suporte ------############
svm = SVC()
svm.fit(frutas_treino, resultado_treino)
svm_preditos = svm.predict(frutas_teste)
svm_acuracia = accuracy_score(svm_preditos, resultado_teste)

################      Pós-processamento     ####################

print(f'Acurácia da Árvode de Decisão {round(frutas_acuracia,5)}')
print("Acurácia SVM:", round(svm_acuracia, 5))

if resultado == 1:
    print('Pera')
else:
    print('Laranja')