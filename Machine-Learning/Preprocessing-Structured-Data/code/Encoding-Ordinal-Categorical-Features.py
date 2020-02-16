import pandas as pd

df = pd.DataFrame({'Score' : ['Low', 'Low', 'Medium', 'Medium', 'High']})

print(df)

scale_mapper = {'Low' : 1,
                'Medium' : 2,
                'High' : 3}

df['Scale'] = df['Score'].replace(scale_mapper)

print(df)
