import pandas as pd
data = {
    "Department": ["IT", "IT", "HR", "HR"],
    "Gender": ["M", "F", "M", "F"],
    "Salary": [50000, 60000, 45000, 55000]
}
df = pd.DataFrame(data)
result = df.groupby(["Department", "Gender"])["Salary"].mean()
print(result)