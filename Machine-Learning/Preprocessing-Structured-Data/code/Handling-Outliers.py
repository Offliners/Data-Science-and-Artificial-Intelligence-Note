import pandas as pd
import numpy as np

houses = pd.DataFrame()
houses['Price'] = [534433, 392333, 293222, 4322032]
houses['Bathrooms'] = [2, 3.5, 2, 116]
houses['Square_Feet'] = [1500, 2500, 1500, 48000]

print(houses)

print(houses[houses['Bathrooms'] < 20])

houses['Outlier'] = np.where(houses['Bathrooms'] < 20,0,1)

print(houses)

houses['Log_of_Square_Feet'] = [np.log(x) for x in houses['Square_Feet']]

print(houses)
