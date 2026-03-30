import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv(r"C:\Users\ACER\Downloads\retail_sales_dataset.csv")

# Basic exploration
print(df.head())
print(df.info())
print(df.describe())
print(df.isnull().sum())
print("Duplicate rows:", df.duplicated().sum())
print(df.columns)

# Convert date column
df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.month

# Value counts
print(df['Product Category'].value_counts())
print(df['Gender'].value_counts())

# Total sales
print("Total Sales:", df['Total Amount'].sum())

# Sales by gender
plt.figure(figsize=(6,4))
sns.barplot(x=df['Gender'].value_counts().index,
            y=df['Gender'].value_counts().values)
plt.title("Number of Purchases by Gender")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.show()

# Purchases by product category
plt.figure(figsize=(8,5))
df['Product Category'].value_counts().plot(kind='bar')
plt.title("Purchases by Product Category")
plt.xlabel("Product Category")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.show()

# Age distribution
plt.figure(figsize=(8,5))
sns.histplot(df['Age'], bins=10, kde=True)
plt.title("Customer Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

# Total amount spent by gender
plt.figure(figsize=(6,4))
sns.barplot(x='Gender', y='Total Amount', data=df, estimator=sum)
plt.title("Total Sales Amount by Gender")
plt.xlabel("Gender")
plt.ylabel("Total Amount")
plt.show()

# Monthly sales trend
monthly_sales = df.groupby('Month')['Total Amount'].sum()
plt.figure(figsize=(8,5))
monthly_sales.plot(marker='o')
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.grid(True)
plt.show()

# High-value customers
high_value = df.groupby('Customer ID')['Total Amount'].sum().sort_values(ascending=False)
print("Top 10 High-Value Customers:")
print(high_value.head(10))

# Top customer chart
plt.figure(figsize=(10,5))
high_value.head(10).plot(kind='bar')
plt.title("Top 10 High-Value Customers")
plt.xlabel("Customer ID")
plt.ylabel("Total Amount Spent")
plt.xticks(rotation=45)
plt.show()
