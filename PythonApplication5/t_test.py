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

#levene's test checks whether the variance of the two groups are the same, like
# the t-test but for variance rather than the mean
print(stats.levene(sample_01['cnt'], sample_02['cnt']))
diff = scale(np.array(sample_01['cnt']) - np.array(sample_02['cnt'], dtype=float))
#note here - need to only run the below line if you want to see the histogram, otherwise it is combined with the box plot above.
plt.hist(diff)

plt.figure(figsize=(10, 8))
stats.probplot(diff, plot=plt, dist='norm')
plt.show()
print(stats.shapiro(diff))
#perform t test
print(stats.ttest_ind(sample_01['cnt'], sample_02['cnt']))
##tried a few different fixes but nothing here works, commenting this one out for now:
#sample_01_df = pd.DataFrame({'cnt': sample_01.values.tolist()})
#sample_02_df = pd.DataFrame({'cnt': sample_02.values.tolist()})
#descriptives, results = rp.ttest(sample_01_df['cnt'], sample_02_df['cnt'])
#print(descriptives)
