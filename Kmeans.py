import pandas as pd
import seaborn as sns
from sklearn.cluster import MiniBatchKMeans
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
if __name__ == "__main__":
    dataset = pd.read_csv('GIT.csv')
    #print(dataset.head(10))
    X = dataset.fillna(0)
    #Selecionamos 4 grupos
    kmeans = MiniBatchKMeans(n_clusters=3, batch_size=8).fit(X)
    print("Total de centros: " , len(kmeans.cluster_centers_))
    print("="*64)
    print(kmeans.predict(X))
    dataset['Toxicos'] = kmeans.predict(X)
    dataset.to_csv("GIT2.csv", index=False)
    print(dataset)
    sns.pairplot(dataset[['Total commits','Total commits per day','Accumulated commits','Committers','Committers Weight','Toxicos']],
             hue='Toxicos')
    plt.show()
    #implementacion_k_means