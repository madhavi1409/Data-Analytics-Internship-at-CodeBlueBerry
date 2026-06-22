import pandas as pd
data = {
    "Employee": ["A", "B", "C", "D", "E"],
    "Department": ["IT", "HR", "IT", "Sales", "HR"],
    "Salary": [50000, 60000, 70000, 45000, 80000]
}
df = pd.DataFrame(data)
print("Salary > 60000:")
print(df[df["Salary"] > 60000])
print("\nHR Department:")
print(df[df["Department"] == "HR"])
print("\nHighest Salary:")
print(df.sort_values("Salary", ascending=False).head(1))
print("\nTop 3 Highest Salaries:")
print(df.sort_values("Salary", ascending=False).head(3))