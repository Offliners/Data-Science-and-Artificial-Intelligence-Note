import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd

text_data = np.array(['I love Brazil. Brazil!',
                      'Sweden is best',
                      'Germany beats both'])

count = CountVectorizer()
bag_of_words = count.fit_transform(text_data)

print(bag_of_words.toarray())

feature_names = count.get_feature_names()

print(feature_names)

df = pd.DataFrame(bag_of_words.toarray(), columns=feature_names)
print(df)
