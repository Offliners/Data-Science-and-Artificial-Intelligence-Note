from sklearn import datasets
import matplotlib.pyplot as plt

boston = datasets.load_boston()

X = boston.data
y = boston.target

print(X[0])
print(['{:f}'.format(x) for x in X[0]])
