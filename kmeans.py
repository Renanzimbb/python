import pandas as pd
from sklearn.cluster import KMeans

df = pd.read_csv('dados_dengue.csv')
f = df.drop('graves', axis=1)
KMeans = KMeans(n_clusters=3)
print(KMeans.fit(f))

