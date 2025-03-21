# %%

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler

# Load the cleaned dataset
df = pd.read_csv("E:\\Superstore_Sales\\csv_files\\Superstore_Sales_Dataset_Cleaned.csv")

# Check if date columns are already converted; if not, convert them
if not np.issubdtype(df['Order Date'].dtype, np.datetime64):
    # print('Converting Order Date to datetime')
    df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')
    
if not np.issubdtype(df['Ship Date'].dtype, np.datetime64):
    # print("Converting Ship Date to datetime...")
    df['Ship Date'] = pd.to_datetime(df['Ship Date'], errors='coerce')
    
# Extract new data features
df['Order_Year'] = df['Order Date'].dt.year
df['Order_Month'] = df['Order Date'].dt.month
df['Order_Day'] = df['Order Date'].dt.day
df['Order_Weekday'] = df['Order Date'].dt.dayofweek

# Calculate Shipping Delay in days
print('Calculating shipping delay...')
df['Shipping_Delay'] = (df['Ship Date'] - df['Order Date']).dt.days

# Log-transform sales to reduce skewness
print('Applying log transformation to Sales...')
df['Log_Sales'] = np.log(df['Sales'] + 1)

# Scale Sales using MinMax scaling
print("Scaling Sales column...")
scaler = MinMaxScaler()
df['Scaled_Sales'] = scaler.fit_transform(df[['Sales']])

# Display a sample of the transformed data
print("\
Transformed dataset sample:")
print(df[['Order Date', 'Ship Date', 'Order_Year', 'Order_Month', 'Order_Day', 'Order_Weekday', 'Shipping_Delay', 'Sales', 'Log_Sales', 'Scaled_Sales']].head())

# plot the distribution of Shipping Delay
print("Plotting shipping delay distribution...")
fig, ax = plt.subplots(figsize=(9, 6))
sns.histplot(df['Shipping_Delay'], kde=True, color='#766CDB', ax=ax)
ax.set_title('Distribution of Shipping Delay', pad=15)
ax.set_xlabel('Shipping Delay (days)', labelpad=10)
ax.set_ylabel('Frequency', labelpad=10)
ax.set_axisbelow(True)
plt.grid(axis='y', linestyle='--', alpha=0.7, color='#E0E0E0')
plt.tight_layout()
plt.savefig('revised_shipping_delay_distribution.png')
plt.show()

# Save the transformed dataset
df.to_csv('Superstore_Sales_Dataset_Transformed_Revised.csv', index=False)
# %%
