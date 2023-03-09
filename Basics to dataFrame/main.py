import pandas as pd
import numpy as np

dataset = pd.read_csv('data.csv')

df = pd.DataFrame()

df['Name'] = ['Steven Smith', 'John Smith']
df['Age'] = [26, 25]

df['Country'] = ['Aus', 'Ind']

df.to_excel("new.xlsx")

# for index, row in df.iterrows():
#     print(index, row)

new_row = pd.Series(['Angela', 28, 'Sri'])

# print(df)

# Boshini korsatadi datasetni
# print(dataset.head())

# Oxirini ko'rsatadi datasetni
# print(dataset.tail())

# nechta row va colni chiqaradi
print(dataset.shape)
