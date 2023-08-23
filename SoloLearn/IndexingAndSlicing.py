import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = {
    'sport': ["Soccer", "Tennis", "Soccer", "Hockey"],
    'players': [5, 4, 8, 20]
}
df = pd.DataFrame(data)
df.groupby('sport')['players'].sum().plot(kind="pie")
plt.show()

data = np.arange(1, 100)

print(data[(data%3==0) & (data%5==0)])




data = np.array([120, 98, 150, 65, 42, 100, 190, 220, 140, 110, 88, 89, 100, 120, 50, 180, 155, 42, 89, 77, 200, 190, 125, 98, 77, 40, 39, 59, 30, 67])

average = np.mean(data)
exceeded = data[(data>average)]
print(np.size(exceeded))

print(average)


x = np.arange(1,5)
x = x*2
print(x[:3])


data = np.array([150000, 125000, 320000, 540000, 200000, 120000, 160000, 230000, 280000, 290000, 300000, 500000, 420000, 100000, 150000, 280000])

average = np.mean(data)
std = np.std(data)
within = data[(data < (average + std)) & (data > (average - std))]
print((np.size(within) / np.size(data)) * 100)







data = {
   'name': ['James', 'Billy', 'Bob', 'Amy', 'Tom'],
   'number': ['1234', '5678', '2222', '1111', '0909']
}

df = pd.DataFrame(data, index = data['name'])
x = input()
print(df.loc[x])


data = {
    "date": ['2022-10-01', '2022-10-02'],
    "state": ['SC', 'NC'],
    "deaths": [50, 3],
    "cases": [200, 300]
}

df = pd.DataFrame(data)

df.drop('state', axis=1, inplace=True)
df.set_index('date', inplace=True)

print(df)

df['ratio'] = df['deaths'] / df['cases']

print(df['ratio'])

max_day = df[(df['ratio'] == df['ratio'].max())]

print(max_day)



