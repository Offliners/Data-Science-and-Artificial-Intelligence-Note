from sklearn.datasets import make_classification
import pandas as pd

feature, output = make_classification(n_samples=100,
                                      n_features=10,
                                      n_informative=5,
                                      n_redundant=5,
                                      n_classes=3,
                                      weights=[.2, .3, .8])

print(pd.DataFrame(feature).head())
print(pd.DataFrame(output).head())
