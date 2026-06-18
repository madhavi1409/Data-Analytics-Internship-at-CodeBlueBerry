import pandas as pd
import numpy as np

data = [21,21, np.nan, 20, 22]

df = pd.DataFrame({"Age": data})

df["Age"] = df["Age"].fillna(0)
df["Age"].fillna(
df["Age"].mean()
)
df.duplicated().sum()
df.drop_duplicates()
df.drop_duplicates(inplace=True)

print(df)
