import pandas as pd
data = {
    "Employee": ["Rahul", "Aman", "Priya", "Neha", "Rohan"],
    "Department": ["IT", "IT", "HR", "HR", "Sales"],
    "Salary": [50000, 60000, 45000, 55000, 70000]
}
df = pd.DataFrame(data)
result = df.groupby("Department")["Salary"].sum()
print(result)