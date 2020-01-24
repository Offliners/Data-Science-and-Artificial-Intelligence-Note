from sklearn import preprocessing 
import pandas as pd

raw_data = {'patient' : [1, 1, 1, 2, 2],
            'obs' : [1, 2, 3, 1, 2],
            'treatment' : [0, 1, 0, 1, 0],
            'score' : ['strong', 'weak', 'normal', 'weak', 'strong']}

df = pd.DataFrame(raw_data, columns=['patient', 'obs', 'treatment', 'score'])

le = preprocessing.LabelEncoder()

le.fit(df['score'])

print(list(le.classes_))

print(le.transform(df['score']))

print(list(le.inverse_transform([2, 2, 1])))
