import pandas as pd

file_path = '/Users/holmes/Desktop/icap/life_expectancy_dataset.xlsx'
df = pd.read_excel(file_path, header=False)
df_wide = pd.DataFrame(df)
# Set 'Year' as the index
print(df_wide.head())
df_wide.set_index('Country', inplace=True)

# Convert from wide to long format
df_long = df_wide.reset_index().melt(id_vars='Country',var_name='Year',value_name='Life Expectancy')

print(df_long)

# Export to Excel
df_long.to_excel('long_format_life_expectancy.xlsx', index=False, engine='openpyxl')
