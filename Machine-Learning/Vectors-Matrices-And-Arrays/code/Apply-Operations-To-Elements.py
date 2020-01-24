import numpy as np

matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

add_100 = lambda i : i + 100

vectorized_add_100 = np.vectorize(add_100)

print(vectorized_add_100(matrix))
