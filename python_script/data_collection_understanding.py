# %%
import pandas as pd

# Loading the dataset
file_path = "E:\\Superstore_Sales\\csv_files\\Superstore_Sales_Dataset.csv"
data = pd.read_csv(file_path)

# Displaying basic infromation about the dataset
print('Dataset Inofrmation: ')
data.info()

# Displaying the first few rows of the dataset
print('First 5 rows of the dataset: ')
print(data.head())

# checking for missing values
print('Missing Values: ')
print(data.isnull().sum())

# Descriptive statistics of the dataset
print('Descriptive statistics:')
print(data.describe())
# %%
