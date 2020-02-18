from sklearn import preprocessing
import numpy as np

x = np.array([[-500.5], 
              [-100.1], 
              [0], 
              [100.1], 
              [900.9]])

minmax_scale = preprocessing.MinMaxScaler(feature_range=(0,1))
x_scale = minmax_scale.fit_transform(x)
print(x_scale)
