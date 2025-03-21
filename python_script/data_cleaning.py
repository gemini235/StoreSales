# %%

import pandas as pd

# Loading the dataset
file_path = "E:\\Superstore_Sales\\csv_files\\Superstore_Sales_Dataset.csv"
data = pd.read_csv(file_path)

# Drop the 'Row ID' column
if 'Row ID' in data.columns:
    data = data.drop(columns=['Row ID'])
else:
    print('Row ID column not found')
    
# Convert 'Postal Code' to string
if 'Postal Code' in data.columns:
    data['Postal Code'] = data['Postal Code'].astype(str)
else:
    print('Postal Code column not found')
    

"""
# Show head of the cleaned DataFrame
# print('Cleaned DataFrame head: ')
# print(data.head())

# check the data types to confirm our changes
# print('Data types after cleaning: ')
# print(data.dtypes)
"""
# Handle missing values in postal code
missing_postal = data[data['Postal Code'] == 'Nall']
# print(f'Number of rows with missing Postal Code: {len(missing_postal)}')

# Convert date columns to datetime format
data['Order Date'] = pd.to_datetime(data['Order Date'], format='%d/%m/%Y', errors='coerce')
data['Ship Date'] = pd.to_datetime(data['Ship Date'], format='%d/%m/%Y', errors='coerce')

"""
# Cheack if date conversion worked
print('Data conversion check: ')
print(data[['Order Date', 'Ship Date']].head())
"""

# Save the cleaned dataset
data.to_csv('Superstore_Sales_Dataset_Cleaned.csv', index=False)

# %%
