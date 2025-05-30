import pandas as pd

# Load the dataset
df = pd.read_csv('iris.csv')

# Drop the first 10 rows
df = df.iloc[10:]

# Save back to the same file
df.to_csv('iris.csv', index=False)

print("Deleted first 10 rows from iris.csv")
