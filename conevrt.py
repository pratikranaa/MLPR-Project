import pandas as pd

# Load the CSV file
df = pd.read_csv("parkinsons_fold.csv")

# Round all numerical columns to 2 decimal places
df = df.round(3)

# Save the rounded DataFrame back to a CSV file
df.to_csv('rounded_file.csv', index=False)