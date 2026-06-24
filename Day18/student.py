import pandas as pd
data = {
    "Name": ["Rahul", "Aman", "Priya", "Neha", "Rohit"],
    "Age": [21, 22, 20, 21, 23],
    "Marks": [78, 85, 92, 88, 75]
}
df = pd.DataFrame(data)
df.to_csv("student.csv", index=False)
print("student.csv file created successfully!\n")
df = pd.read_csv("student.csv")
print("First 5 Rows:")
print(df.head())
print("\nDataset Info:")
df.info()
print("\nShape of Dataset:")
print(df.shape)