import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("Dataset for Data Analytics - Sheet1.csv")

# ===== BASIC INFO =====
print("===== FIRST 5 ROWS =====")
print(df.head())

print("\n===== SHAPE (Rows & Columns) =====")
print(df.shape)

print("\n===== BASIC STATISTICS =====")
print(df.describe())

# ===== MEAN, MEDIAN, COUNT =====
print("\n===== MEAN UNIT PRICE =====")
print(df['UnitPrice'].mean())

print("\n===== MEDIAN TOTAL PRICE =====")
print(df['TotalPrice'].median())

print("\n===== ORDER STATUS COUNT =====")
print(df['OrderStatus'].value_counts())

print("\n===== MOST SOLD PRODUCTS =====")
print(df['Product'].value_counts())

print("\n===== TOTAL REVENUE =====")
print(df['TotalPrice'].sum())

# ===== OUTLIERS =====
print("\n===== HIGHEST VALUE ORDERS =====")
print(df[df['TotalPrice'] > df['TotalPrice'].quantile(0.95)])

# ===== CHARTS =====

# Chart 1 - Products sold
plt.figure(figsize=(10,6))
df['Product'].value_counts().plot(kind='bar', color='skyblue')
plt.title('Most Sold Products')
plt.xlabel('Product')
plt.ylabel('Count')
plt.tight_layout()
plt.show()

# Chart 2 - Order Status
plt.figure(figsize=(8,6))
df['OrderStatus'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title('Order Status Breakdown')
plt.show()

# Chart 3 - Total Price Distribution
plt.figure(figsize=(10,6))
sns.histplot(df['TotalPrice'], bins=30, color='green')
plt.title('Total Price Distribution')
plt.xlabel('Total Price')
plt.show()

print("\n===== EDA Complete! =====")