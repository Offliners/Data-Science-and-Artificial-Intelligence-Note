import pandas as pd
from sklearn.datasets import make_regression

features, output, coef = make_regression(n_samples=100,
                                         n_features=3,
                                         n_informative=2,
                                         n_targets=1,
                                         noise=0.0,
                                         coef=True)

print(pd.DataFrame(features, columns=['Store 1', 'Store 2', 'Store 3']).head())
print(pd.DataFrame(output, columns=['Sales']).head())
print(pd.DataFrame(coef, columns=['True Coefficient Values']))
