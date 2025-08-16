import pandas as pd

# Read data
df = pd.read_csv("data.csv")

# Clean data
df = df.dropna()
df = df.drop_duplicates()

# Save cleaned data
df.to_csv("cleaned_data.csv", index=False)

print("✅ Data cleaned and saved to cleaned_data.csv")
