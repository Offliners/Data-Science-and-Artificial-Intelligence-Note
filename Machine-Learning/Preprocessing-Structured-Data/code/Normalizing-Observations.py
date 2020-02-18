from sklearn.preprocessing import Normalizer
import numpy as np

X = np.array([[0.5, 0.5], 
              [1.1, 3.4], 
              [1.5, 20.2], 
              [1.63, 34.4], 
              [10.9, 3.3]])

normalizer = Normalizer(norm='l2')
print(normalizer.transform(X))
