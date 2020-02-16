import numpy as np
from sklearn.datasets import load_iris

iris = load_iris()

X = iris.data
y = iris.target

X = X[40: ,:]
y = y[40:]

y = np.where((y == 0), 0, 1)
print(y)

i_class0 = np.where(y == 0)[0]
i_class1 = np.where(y == 1)[0]

n_class0 = len(i_class0)
n_class1 = len(i_class1)

i_class1_downsampled = np.random.choice(i_class1, size=n_class0, replace=False)
print(np.hstack((y[i_class0], y[i_class1_downsampled])))
