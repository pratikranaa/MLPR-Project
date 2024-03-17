# import pandas as pd

# # Read the CSV file
# df = pd.read_csv('combined_file_all.csv')

# # Identify rows where all values are zero except for the 'status' column
# mask = (df.drop(columns=['status']) == 0).all(axis=1)

# # Keep rows where 'status' column is not zero or all other columns are not zero
# mask = mask | (df['status'] != 0)

# # Filter the dataframe based on the mask
# filtered_df = df[mask]

# # Write the filtered data back to a new CSV file
# filtered_df.to_csv('filtered_file.csv', index=False)


import pandas as pd

# Read the CSV file
df = pd.read_csv('combined_file_all.csv')

# Calculate the number of zeros in each column
zeros_per_column = (df == 0).sum()

# Print the number of zeros in each column
for column, zeros in zeros_per_column.items():
    print(f"Column '{column}': {zeros}")


# Drop the 'PPE' column
df = df.drop('PPE', axis=1)

# Write the modified DataFrame to a new CSV file
df.to_csv('file_without_PPE.csv', index=False)
