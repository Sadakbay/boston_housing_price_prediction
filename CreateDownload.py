import urllib.request

print('Beginning file download with urllib2...')

url = "https://raw.githubusercontent.com/bursteinalan/Data-Sets/master/Housing/House%20Prediction%20Data.csv"
urllib.request.urlretrieve(url, 'HousePrediction.csv')

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('HousePrediction.csv')

# in order to see some statistics of dataframe
df.describe()
# to see correlation between columns
correl = df.corr()
Corr_with_price = correl['SalePrice']
sorted_correl = correl.sort_values(by = ['SalePrice'])
sorted_correl['SalePrice']
df.MSZoning.value_counts()