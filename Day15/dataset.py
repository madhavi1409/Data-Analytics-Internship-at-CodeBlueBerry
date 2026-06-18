import pandas as pd
import numpy as np

df = pd.read_excel("marks_data.xlsx")

print(df.head())

df.loc[2, "Age"] = np.nan
df.loc[5, "Name"] = None

df = pd.concat([df, df.iloc[[0]]], ignore_index=True)

df.loc[1, "Name"] = "  Rahul  "

df.loc[3, "City"] = "DELHI"
df.loc[4, "City"] = "delhi"

df["Age"] = df["Age"].astype(str)

print("Messy Dataset")
print(df)

print(df.isnull().sum())

df["Age"] = pd.to_numeric(df["Age"], errors="coerce")

df["Age"] = df["Age"].fillna(df["Age"].mean())

df["Name"] = df["Name"].fillna("Unknown")

df = df.drop_duplicates()

df["Name"] = df["Name"].str.strip()

df["City"] = df["City"].str.upper()

df["Age"] = df["Age"].astype(int)

df.rename(columns={"Name":"Student_Name"}, inplace=True)

print("\nClean Dataset")
print(df)