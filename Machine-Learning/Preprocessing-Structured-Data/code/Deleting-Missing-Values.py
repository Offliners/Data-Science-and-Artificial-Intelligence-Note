import numpy as np
import pandas as pd

X = np.array([[1, 2], 
              [6, 3], 
              [8, 4], 
              [9, 5], 
              [np.nan, 4]])

print(X[~np.isnan(X).any(axis=1)])

df = pd.DataFrame(X, columns=['feature_1', 'feature_2'])

print(df.dropna())
