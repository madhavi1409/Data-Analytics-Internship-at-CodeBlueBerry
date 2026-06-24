import pandas as pd
df = pd.read_csv("students.csv")
print("First 5 Rows:")
print(df.head())
print("\nDataset Info:")
df.info()
print("\nShape of Dataset:")
print(df.shape)