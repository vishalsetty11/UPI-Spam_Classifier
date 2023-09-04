import pandas as pd

# Define the CSV file path
csv_file_path = 'spam.csv'

# Read the CSV file into a DataFrame with 'latin-1' encoding
df = pd.read_csv(csv_file_path, encoding='latin-1')

# Add a new column 'v2' with default value 0
df['v2'] = 0

# Set 'v2' to 1 where 'spam' exists in 'v1'
df.loc[df['v1'] == 'spam', 'v2'] = 1

# Save the modified DataFrame back to the CSV file
df.to_csv(csv_file_path, index=False)

# Optionally, display the updated DataFrame
print(df)
