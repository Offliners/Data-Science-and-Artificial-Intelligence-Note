from sklearn import datasets
import matplotlib.pyplot as plt

digits = datasets.load_digits()

X = digits.data
y = digits.target

print(X[0])
print(digits.images[0])

plt.gray()
plt.matshow(digits.images[0])
plt.show()
