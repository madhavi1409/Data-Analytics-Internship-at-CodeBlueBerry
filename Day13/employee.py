import pandas as pd
data = {
    "Name": ["Rahul", "Priya", "Aman", "Neha"],
    "Salary": [50000, 60000, 55000, 70000]
}
df = pd.DataFrame(data)
print("Employee DataFrame:")
print(df)
avg_salary = df["Salary"].mean()
print("\nAverage Salary =", avg_salary)
highest_salary = df["Salary"].max()
print("Highest Salary =", highest_salary)