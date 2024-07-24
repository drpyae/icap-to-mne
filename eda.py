import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
file_path = '/Users/holmes/Desktop/icap/Prevention_Data.xlsx'
df = pd.read_excel(file_path)

# Display the first few rows of the dataset to understand its structure
print("First few rows of the dataset:")
print(data.head(), '\n')

# Display data types
print(df.dtypes)

# Summary statistics for numerical and categorical columns
summary_stats = data.describe(include='all')
# Display the summary statistics
print("Summary Statistics Overview:")
print(summary_stats)

# Additional specific statistics
print("\nAdditional Information:")
# Count of unique values in 'id'
unique_ids = data['id'].nunique()
print(f"Number of unique IDs: {unique_ids}")

# Check for missing values
print(df.isnull().sum())

# Frequency count for categorical variables
categorical_cols = ['msm', 'fsw', 'pwid', 'tg', 'other', 'hiv_edu', 'cdm_lu', 'hts_info', 'sti_info', 'prep_pep']
frequency_counts = {col: df[col].value_counts() for col in categorical_cols}

print("\nFrequency Counts for Categorical Variables:")
for col, counts in frequency_counts.items():
    print(f"\n{col}:")
    print(counts)

# Unique values in the 'id' column
unique_ids = df['id'].nunique()
print(f"\nUnique IDs: {unique_ids}")

# Date range of the data
date_range = (df['date_reach'].min(), df['date_reach'].max())
print(f"\nDate Range: {date_range[0]} to {date_range[1]}")


# Set up the style of the visualization
sns.set(style="whitegrid")

# Calculate category counts
categories = ['msm', 'fsw', 'pwid', 'tg', 'other']
category_counts = df[categories].sum()

# Create a bar plot for the category distribution
plt.figure(figsize=(10, 6))
sns.barplot(x=category_counts.index, y=category_counts.values, palette='viridis')
plt.title('Distribution of Participants by Category', fontsize=16)
plt.xlabel('Category', fontsize=14)
plt.ylabel('Number of Participants', fontsize=14)
plt.xticks(rotation=45)
plt.show()

# Calculate the proportion of participants receiving each type of information
info_services = ['hiv_edu', 'cdm_lu', 'hts_info', 'sti_info', 'prep_pep']
info_coverage = df[info_services].mean() * 100

# Create a bar plot for the information coverage
plt.figure(figsize=(10, 6))
sns.barplot(x=info_coverage.index, y=info_coverage.values, palette='coolwarm')
plt.title('Information Coverage Across Services', fontsize=16)
plt.xlabel('Service Type', fontsize=14)
plt.ylabel('Coverage (%)', fontsize=14)
plt.ylim(90, 105)  # Set y-limit to highlight coverage
plt.xticks(rotation=45)
plt.show()


# Define the required columns for prevention reach
required_services = ['hiv_edu', 'cdm_lu', 'hts_info', 'sti_info', 'prep_pep']

# Calculate the number of clients counted as prevention reach
prevention_reach_count = df[required_services].all(axis=1).sum()

# Display the result
print(f"Number of clients counted as prevention reach: {prevention_reach_count}")

total_clients = len(df)
prevention_reach_percentage = (prevention_reach_count / total_clients) * 100
print(f"Percentage of clients counted as prevention reach: {prevention_reach_percentage:.2f}%")

clients_not_reached = df[~data[required_services].all(axis=1)]
print("Clients not counted as prevention reach:")
print(clients_not_reached)

# Identify which service is most often missing
missing_services_counts = clients_not_reached[required_services].eq(0).sum()
print("Missing services count:")
print(missing_services_counts)
