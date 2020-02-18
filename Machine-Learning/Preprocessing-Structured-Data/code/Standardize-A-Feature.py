from sklearn import preprocessing
import numpy as np

x = np.array([[-500.5], 
              [-100.1], 
              [0], 
              [100.1], 
              [900.9]])

scaler = preprocessing.StandardScaler()
standardized = scaler.fit_transform(x)
print(standardized)
