import pandas as pd
df = pd.read_excel("employee.xlsx")
print("Employee Data:")
print(df)
avg_salary = df["Salary"].mean()
print("\nAverage Salary:")
print(avg_salary)
result = pd.DataFrame({
    "Average Salary": [avg_salary]
})
result.to_excel("employee_report.xlsx", index=False)
print("\nReport exported successfully!")