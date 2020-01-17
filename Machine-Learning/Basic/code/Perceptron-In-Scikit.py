from sklearn import datasets
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Perceptron
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np

iris = datasets.load_iris()

X = iris.data
y = iris.target

print(X[:5])
print(y[:5])

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3)

sc = StandardScaler()
sc.fit(X_train)

X_train_std = sc.transform(X_train)
X_test_std = sc.transform(X_test)

ppn = Perceptron(n_iter=40, eta0=0.1, random_state=0)
ppn.fit(X_train_std, y_train)

y_pred = ppn.predict(X_test_std)

print(y_pred)
print(y_test)
print('Accutacy : %.2f' % accuracy_score(y_test, y_pred))
