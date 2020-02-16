import numpy as np
import pandas as pd
from sklearn.preprocessing import Imputer

df = pd.DataFrame()

df['x0'] = [0.3051,0.4949,0.6974,0.3769,0.2231,0.341,0.4436,0.5897,0.6308,0.5]
df['x1'] = [np.nan,0.2654,0.2615,0.5846,0.4615,0.8308,0.4962,0.3269,0.5346,0.6731]

print(df)

mean_imputer = Imputer(missing_values='NaN',strategy='mean',axis=0)
mean_imputer = mean_imputer.fit(df)

imputed_df = mean_imputer.transform(df.values)
print(imputed_df)
