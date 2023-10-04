import statsmodels.api as sm
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.preprocessing import scale

import researchpy as rp
from scipy import stats

bike_sharing_data = pd.read_csv('demos/datasets/day.csv')
print(bike_sharing_data.shape)
#print first 5 rows of data
print(bike_sharing_data.head())

#transform the data to only the columns we need
bike_sharing_data = bike_sharing_data[['season', 'mnth', 'holiday', 'workingday', 'weathersit', 'temp', 'cnt']]
bike_sharing_data.to_csv('demos/datasets/bike_sharing_data_processed.csv', index=False)

print(bike_sharing_data.head())
print(bike_sharing_data['season'].unique())
print(bike_sharing_data['workingday'].unique())
print(bike_sharing_data['holiday'].unique())
print(bike_sharing_data['weathersit'].unique())
print(bike_sharing_data['temp'].describe())
print(bike_sharing_data.shape)
print(bike_sharing_data.groupby('workingday')['cnt'].describe())
bike_sharing_data.boxplot(column=['cnt'], by='workingday', figsize=(10,8))

sample_01 = bike_sharing_data[(bike_sharing_data['workingday'] == 1)]
sample_02 = bike_sharing_data[(bike_sharing_data['workingday'] == 0)]
#in our data, we have more 'working days' than non-working days (workday==1):
print(sample_01.shape, sample_02.shape)
#for a t-test we need the sample size to be the same, so let's take a sample of just the first 231 days for each:
sample_01 = sample_01.sample(231)
print(sample_01.shape, sample_02.shape)