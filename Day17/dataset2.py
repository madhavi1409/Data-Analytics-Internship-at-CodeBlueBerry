import pandas as pd
data = {
    "Student": ["Rahul", "Aman", "Priya", "Neha", "Rohan"],
    "Course": ["Python", "SQL", "Python", "SQL", "Power BI"],
    "Marks": [78, 85, 92, 88, 65]
}
df = pd.DataFrame(data)
result = df.groupby("Course")["Marks"].agg(
    Average_Marks="mean",
    Highest_Marks="max",
    Student_Count="count"
)
print(result)