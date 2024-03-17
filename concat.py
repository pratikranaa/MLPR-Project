import pandas as pd

# Read the two CSV files
df1 = pd.read_csv('normalized_english_kaggle.csv')
df2 = pd.read_csv('combined_file_italian.csv')

# Ensure columns are in the same order
df2 = df2[df1.columns]

# Concatenate the two dataframes vertically
combined_df = pd.concat([df1, df2], ignore_index=True)

# Write the combined data to a new CSV file
combined_df.to_csv('combined_file_all.csv', index=False)
