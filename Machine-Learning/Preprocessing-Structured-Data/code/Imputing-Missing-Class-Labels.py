import numpy as np
from sklearn.preprocessing import Imputer

X = np.array([[0, 2.10, 1.45], 
              [1, 1.18, 1.33], 
              [0, 1.22, 1.27],
              [0, -0.21, -1.19],
              [np.nan, 0.87, 1.31],
              [np.nan, -0.67, -0.22]])

imputer = Imputer(strategy='most_frequent', axis=0)
print(imputer.fit_transform(X))
