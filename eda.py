import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
file_path = '/Users/holmes/Desktop/icap/Prevention_Data.xlsx'
df = pd.read_excel(file_path)

# Display the first few rows
print(df.head())

# Display data types
print(df.dtypes)

# Display basic statistics
print(df.describe())

# Check for missing values
print(df.isnull().sum())


# Fill or drop missing values
#df = df.fillna(method='ffill')  # Example of forward filling
# df = df.dropna()  # Example of dropping rows with missing values

# Histogram for numerical columns
df.hist(figsize=(10, 8))
plt.show()

# Boxplot for numerical columns
df.plot(kind='box', subplots=True, layout=(2, 3), figsize=(10, 8))
plt.show()

