import pandas as pd

# Read the CSV file
df = pd.read_csv("parkinsons_fold.csv")

# Normalize numerical columns except 'Person' and 'Wav file'
numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
df[numeric_cols] = df[numeric_cols].apply(lambda x: (x - x.min()) / (x.max() - x.min()) if x.name not in ['Person', 'Wav file', 'status', 'rep'] else x)

# Write the normalized data back to a new CSV file
df.to_csv('normalized_english_kaggle.csv', index=False)
