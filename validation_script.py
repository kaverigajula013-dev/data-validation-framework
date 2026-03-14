import pandas as pd

# load dataset
data = pd.read_csv("dataset.csv")

print("Dataset shape:", data.shape)

# check missing values
print("\nMissing values:")
print(data.isnull().sum())

# check duplicate rows
duplicates = data.duplicated().sum()
print("\nDuplicate rows:", duplicates)

# remove duplicates
data_clean = data.drop_duplicates()

print("\nClean dataset shape:", data_clean.shape)

print("\nData validation completed.")
