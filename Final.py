import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('results16-19.csv')

#Change the time format
df['date'] = pd.to_datetime(df['date'])

#First group data by item and zip code and then sum by item sold
grouped = df.groupby(['item_description','zip_code'])
item_sold = grouped['bottles_sold'].sum()
print("The most popular item sold based on zip code is:\n",item_sold.sort_values(ascending=False).head(1))

#Get sales per store.
grouped = df.groupby('store_number')
store_sales = grouped['sale_dollars'].sum()

store_sales['percent_sales'] = store_sales['sale_dollars'] / store_sales * 100


print(store_sales)


