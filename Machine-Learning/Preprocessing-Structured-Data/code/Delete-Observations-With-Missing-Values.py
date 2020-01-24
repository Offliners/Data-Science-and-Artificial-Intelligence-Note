import numpy as np

X = np.array([[1.1, 11.1], 
              [2.2, 22.2], 
              [3.3, 33.3], 
              [4.4, 44.4], 
              [np.nan, 55]])

print(X[~np.isnan(X).any(axis=1)])
