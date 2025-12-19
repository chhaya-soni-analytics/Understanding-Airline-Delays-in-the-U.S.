# -*- coding: utf-8 -*-
"""
Created on Thu Dec 11 16:49:44 2025

@author: WIN10
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv("C:/Users/WIN10/Downloads/Amazon.csv")

df.head()

df.info()

df.isnull() 

df.isnull().sum() 

df.duplicated().sum()

print(df.columns)

df["sales"] = df ["Quantity"] * df ["UnitPrice"]

print(df)

df['OrderDate'] = pd.to_datetime(df['OrderDate'], format='%Y-%m-%d')
print(df.dtypes)

df['Year'] = df['OrderDate'].dt.year
df['Month'] = df['OrderDate'].dt.month
df['Day'] = df['OrderDate'].dt.day

print(df.head())

df['YearMonth'] = df['OrderDate'].dt.to_period('M')  # for grouping

print(df[['OrderDate','Year','Month','sales']].head())


print(df)
print(df.dtypes)
total_sales = df['sales'].sum()
num_orders = df.shape[0]
avg_order_value = df['sales'].mean()
top_country = df.groupby('Country')['sales'].sum().sort_values(ascending=False).head(1)

print("Total Sales:", total_sales)
print("Number of Orders:", num_orders)
print("Average Order Value:", avg_order_value)
print("Top country by Sales:\n", top_country) 

# step6_save_cleaned.py
df.to_csv("Amazon_cleaned.csv", index=False)
print("Saved cleaned dataset as Amazon_cleaned.csv")



# step8_1_monthly_trend.py
monthly = df.groupby('YearMonth')['sales'].sum().reset_index()
monthly['YearMonthStr'] = monthly['YearMonth'].astype(str)

plt.figure(figsize=(10,4))
plt.plot(monthly['YearMonthStr'], monthly['sales'], marker='o')
plt.xticks(rotation=45)
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("sales")
plt.tight_layout()
plt.show()


# step8_2_top_products.py
top_products = df.groupby('ProductName')['sales'].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(10,5))
top_products.plot(kind='bar')
plt.title("Top 10 Products by sales")
plt.xlabel("Product")
plt.ylabel("sales")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# step8_3_category_sales.py
if 'Category' in df.columns:
    cat_sales = df.groupby('Category')['sales'].sum().sort_values(ascending=False).head(10)
    plt.figure(figsize=(10,5))
    cat_sales.plot(kind='bar')
    plt.title("Top 10 Categories by Sales")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()
    
# step8_4_country_sales.py
if 'Country' in df.columns:
    country_sales = df.groupby('Country')['sales'].sum().sort_values(ascending=False).head(10)
    plt.figure(figsize=(8,4))
    country_sales.plot(kind='bar')
    plt.title("Top Countries by Sales")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()    
    
    
#step8_5_sales_dist.py
plt.figure(figsize=(8,4))
plt.hist(df['sales'].dropna(), bins=50)
plt.title("Sales Distribution")
plt.xlabel("sales")
plt.ylabel("Count")
plt.tight_layout()
plt.show()    


top_customers = df.groupby('CustomerID')['sales'].sum().sort_values(ascending=False).head(10)
print(top_customers)

payment_method = df["PaymentMethod"].value_counts()
print(payment_method) 

sizes = [35038,20024,15066,15017,9927,4928] 
labels = ["Credit Card", "Debit Card","UPI","Amazon Pay","Net Bnaking","Cash on Delivery"]
colors = ["blue","red","pink","grey","yellow"]  
plt.figure(figsize=(6,6))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)

plt.title("Payment Method")
plt.show() 

status = df['OrderStatus'].value_counts(normalize=True) * 100
print(status)

# step10_insights.py
total_sales = df['sales'].sum()
aov = df['sales'].mean()
top_month = monthly.loc[monthly['sales'].idxmax()]
top_product = df.groupby('ProductName')['sales'].sum().idxmax()
delivered_pct = (df['OrderStatus']=='Delivered').mean() * 100

print("Total Sales:", total_sales)
print("Average Order Value:", aov)
print("Top month:", top_month['YearMonth'])
print("Top product:", top_product)
print("Delivered %:", delivered_pct)
