import pandas as pd

df = pd.read_csv("data/superstore.csv", encoding="latin1")

print(df.head())
print("\n--- DATA INFO ---")
print(df.info())

print("\n--- STATISTICAL SUMMARY ---")
print(df.describe())

df['Order Date'] = pd.to_datetime(df['Order Date'])
region_sales = df.groupby('Region')['Sales'].sum()
print("\n--- SALES BY REGION ---")
print(region_sales)

import matplotlib.pyplot as plt

region_sales.plot(kind='bar', title='Sales by Region')
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.show()

category_profit = df.groupby('Category')['Profit'].sum()
print("\n--- PROFIT BY CATEGORY ---")
print(category_profit)

category_profit.plot(kind='bar', title='Profit by Category')
plt.xlabel("Category")
plt.ylabel("Total Profit")
plt.show()

df['Month'] = df['Order Date'].dt.month
monthly_sales = df.groupby('Month')['Sales'].sum()

print("\n--- MONTHLY SALES TREND ---")
print(monthly_sales)

monthly_sales.plot(kind='line', title='Monthly Sales Trend')
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.show()

top_customers = (
    df.groupby('Customer Name')['Sales']
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\n--- TOP 10 CUSTOMERS ---")
print(top_customers)


loss_products = df.groupby('Sub-Category')['Profit'].sum()
loss_products = loss_products[loss_products < 0]

print("\n--- LOSS MAKING SUB-CATEGORIES ---")
print(loss_products)
