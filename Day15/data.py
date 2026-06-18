import pandas as pd
import numpy as np

data = {
"Name":["Rahul","Aman","Rahul","Priya",None],
"Age":[21,np.nan,21,20,22],
"City":["Lucknow","Delhi","Lucknow","DELHI","Mumbai"]
}

df = pd.DataFrame(data)

print(df)

print(df.isnull())
print(df.isnull().sum())
df.dropna()
df.dropna(inplace=True)
