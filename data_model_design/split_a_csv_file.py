import pandas as pd

# Loading the dataset
file_path = "E:\\Superstore_Sales\\csv_files\\Superstore_Sales_Dataset_Transformed.csv"
df = pd.read_csv(file_path)

# Create a customer table
customers = df[['Customer ID', 'Customer Name', 'Segment', 'Country', 'City', 'State', 'Postal Code', 'Region']].drop_duplicates()
customers.to_csv("customers.csv", index=False)

# Create a products table
products = df[['Product ID', 'Product Name', 'Category', 'Sub-Category']].drop_duplicates()
products.to_csv("products.csv", index=False)

# Create an order table
orders = df[['Order ID', 'Order Date', 'Ship Date', 'Ship Mode', 'Customer ID']].drop_duplicates()
orders.to_csv("orders.csv", index=False)

# Create a sales table
sales = df[['Order ID', 'Product ID', 'Sales', 'Order_Year', 'Order_Month', 'Order_Day', 'Order_Weekday', 'Shipping_Delay', 'Log_Sales', 'Scaled_Sales']].drop_duplicates()
sales.to_csv("sales.csv", index=False)


