import pandas as pd
data = {
    "Product": ["Laptop", "Laptop", "Mobile", "Mobile", "Tablet"],
    "Sales": [50000, 60000, 30000, 35000, 25000]
}
df = pd.DataFrame(data)
result = df.groupby("Product")["Sales"].agg(
    Total_Sales="sum",
    Average_Sales="mean",
    Transaction_Count="count"
)
print(result)