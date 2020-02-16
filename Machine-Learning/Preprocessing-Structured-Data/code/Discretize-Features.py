from sklearn.preprocessing import Binarizer
import numpy as np

age = np.array([[6],
                [12],
                [20],
                [36],
                [65]])

binarizer = Binarizer(18)

print(binarizer.fit_transform(age))

print(np.digitize(age, bins=[20,30,64]))
