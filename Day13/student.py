import pandas as pd
df = pd.DataFrame({
     "Name": ["Ram", "Shyam", "Mohan","Sita","Geeta"],
     "Age": [18,19,20,30,22],
    "Marks":[78,85,92,88,76]
})

print(df)
print("Average Marks =", df["Marks"].mean())
print("Highest Marks =", df["Marks"].max())
print("Lowest Marks =", df["Marks"].min())
