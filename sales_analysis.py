# sales_analysis.py
# Week 3 - Sales Data Analysis using Pandas

import pandas as pd

# Load the dataset
df = pd.read_csv('sales_data.csv')

print("=== Sales Data Analysis Report ===\n")

# 1. Basic Information
print("1. Dataset Overview:")
print(f"Total Rows: {df.shape[0]}")
print(f"Total Columns: {df.shape[1]}")
print(f"Columns: {list(df.columns)}\n")

# 2. First few rows
print("2. First 5 Sales Records:")
print(df.head())
print()

# 3. Summary Statistics
print("3. Summary Statistics:")
print(df.describe())
print()

# 4. Key Metrics
total_revenue = df['Total_Sales'].sum()
avg_sales = df['Total_Sales'].mean()
best_product = df.loc[df['Total_Sales'].idxmax(), 'Product']
total_products_sold = df['Quantity'].sum()

print("4. Key Insights:")
print(f"Total Revenue Generated     : ₹{total_revenue:,.2f}")
print(f"Average Sales per Transaction: ₹{avg_sales:,.2f}")
print(f"Best Selling Product        : {best_product}")
print(f"Total Items Sold            : {total_products_sold}\n")

# 5. Product-wise Analysis
print("5. Product-wise Sales:")
product_sales = df.groupby('Product')['Total_Sales'].sum().sort_values(ascending=False)
print(product_sales)