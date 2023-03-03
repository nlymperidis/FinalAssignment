import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('results16-19.csv')

# First group data by item and zip code and then sum by item sold
grouped = df.groupby(['item_description', 'zip_code'])
item_sold = grouped['bottles_sold'].sum()
print("The most popular item sold based on zip code is:\n", item_sold.sort_values(ascending=False).head(1))
print()

# Get sales per store.
grouped = df.groupby('store_number')
store_sales = grouped['sale_dollars'].sum().reset_index()

total_sales = store_sales['sale_dollars'].sum()
store_sales['percent_sales'] = store_sales['sale_dollars'] / total_sales * 100
print("The percentage of sales per store is:\n", round(store_sales, 3))

# Group the data by zip code and sum the bottles sold
bottles_sold_by_zip = df.groupby('zip_code')['bottles_sold'].sum().reset_index()

x = len(bottles_sold_by_zip)
plt.scatter(bottles_sold_by_zip['zip_code'], bottles_sold_by_zip['bottles_sold'], c=np.random.rand(x,3))
plt.title('Bottles Sold by Zip Code')
plt.xlabel('Zip Code')
plt.ylabel('Bottles Sold')
plt.show()