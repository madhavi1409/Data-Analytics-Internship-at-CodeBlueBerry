import pandas as pd
data = {
"Name":["Rahul","Aman","Priya","Rohan","Neha"],
"Course":["Python","SQL","Python","Power BI","SQL"],
"Marks":[78,85,92,65,88]
}
df = pd.DataFrame(data)
print(df)
df[df["Marks"] < 80]
df[df["Marks"] < 70]
df.sort_values(
"Marks",
ascending=False
).head(1)

