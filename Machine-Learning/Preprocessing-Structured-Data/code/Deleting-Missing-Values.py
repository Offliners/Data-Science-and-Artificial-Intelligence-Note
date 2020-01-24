import numpy as np

X = np.array([[1, 2], 
              [6, 3], 
              [8, 4], 
              [9, 5], 
              [np.nan, 4]])

print(X[~np.isnan(X).any(axis=1)])
