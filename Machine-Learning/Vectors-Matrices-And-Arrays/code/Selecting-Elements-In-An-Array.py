import numpy as np

vector = np.array([1, 2, 3, 4, 5, 6])

print(vector[1])

matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

print(matrix[1,1])

tensor = np.array([[[[1, 1], [1, 1]], [[2, 2], [2, 2]]],
                  [[[3, 3], [3, 3]], [[4, 4], [4, 4]]]])

print(tensor[1,1,1])
