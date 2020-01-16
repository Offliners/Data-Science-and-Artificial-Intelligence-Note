import pandas as pd

data = {'Platoon': ['A','A','A','A','A','A','B','B','B','B','B','C','C','C','C','C'],
        'Casualties': [1,4,5,7,5,5,6,1,4,5,6,7,4,6,4,6]}

df = pd.DataFrame(data)
print(df)

print(df.groupby('Platoon')['Casualties'].apply(lambda x:x.rolling(center=False,window=2).mean()))
