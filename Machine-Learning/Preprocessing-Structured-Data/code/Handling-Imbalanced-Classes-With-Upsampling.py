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

i_class0_upsampled = np.random.choice(i_class0, size=n_class1, replace=True)
print(np.concatenate((y[i_class0_upsampled], y[i_class1])))
