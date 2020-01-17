from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt

X,y = make_blobs(n_samples=200,
                 n_features=2,
                 centers=3,
                 cluster_std=0.5,
                 shuffle=True)

plt.scatter(X[:,0],X[:,1])
plt.show()
