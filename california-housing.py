from sklearn.datasets import fetch_california_housing
import pandas as pd

california = fetch_california_housing()
df = pd.DataFrame(california.data, columns=california.feature_names)
df.head()
df.describe()


bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
labels = ['0-10', '10-20', '20-30', '30-40', '40-50', '50-60', '60-70', '70-80', '80-90', '90-100']
df['HouseAgeClass'] = pd.cut(df['HouseAge'], bins=bins, labels=labels)
freq = df['HouseAgeClass'].value_counts()
total = len(df['HouseAgeClass'])
freq_rel = freq / total
print('Distribuição de Frequência por Classes da HouseAge:')
print(freq)
print('\nFrequência Relativa por Classes da HouseAge:')
print(freq_rel)