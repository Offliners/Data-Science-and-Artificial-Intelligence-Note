from sklearn import preprocessing
from sklearn.pipeline import Pipeline
import pandas as pd

raw_data = {'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'], 
            'last_name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze'], 
            'age': [42, 52, 36, 24, 73], 
            'city': ['San Francisco', 'Baltimore', 'Miami', 'Douglas', 'Boston']}

df = pd.DataFrame(raw_data, columns=['first_name', 'last_name', 'age', 'city'])
print(df)
print(pd.get_dummies(df['city']))

integerized_data = preprocessing.LabelEncoder().fit_transform(df['city'])
print(integerized_data)

print(preprocessing.OneHotEncoder().fit_transform(integerized_data.reshape(-1, 1)).toarray())
