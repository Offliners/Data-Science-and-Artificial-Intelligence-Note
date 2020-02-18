import numpy as np
import pandas as pd
from sklearn.preprocessing import OneHotEncoder

x = np.array([['Texas'], 
              ['California'], 
              ['Texas'], 
              ['Delaware'], 
              ['Texas']])

one_hot = OneHotEncoder()
one_hot.fit_transform(x)

print(one_hot.categories_)
print(pd.get_dummies(x[:, 0]))
