# SALE Analyzer

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data = {
    "Product": ["Laptop", "Mobile", "Tablet", "Headphones", "Smartwatch"],
    "Units_Sold": [120, 250, 90, 300, 150],
    "Cost_Price": [40000, 15000, 12000, 2000, 5000],
    "Selling_Price": [50000, 20000, 16000, 3500, 8000]
}

df = pd.DataFrame(data)
print(df)

df["Revenue"] = df["Units_Sold"] * df["Selling_Price"]
df["Cost"] = df["Units_Sold"] * df["Cost_Price"]
df["Profit"] = df["Revenue"] - df["Cost"]

total_sales = np.sum(df["Revenue"])
total_profit = np.sum(df["Profit"])

print("\nTotal Sales:", total_sales)

top_product = df.loc[df["Units_Sold"].idxmax()]
print("\nTop Selling Product:")
print(top_product)

monthly_sales = np.array([200000, 220000, 250000, 270000, 300000])

growth_rate = np.mean(np.diff(monthly_sales) / monthly_sales[:-1])
forecast_next_month = monthly_sales[-1] * (1 + growth_rate)

print("\nForecasted Next Month Sales:", int(forecast_next_month))

plt.figure()
plt.bar(df["Product"], df["Revenue"])
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.title("Revenue by Product")
plt.show()

plt.figure()
plt.pie(df["Profit"], labels=df["Product"], autopct="%1.1f%%")
plt.title("Profit Contribution")
plt.show()

plt.figure()
plt.plot(monthly_sales, marker='o')
plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Monthly Sales Trend")
plt.show()

print("\n--- Sales Insights ---")
print("Highest Revenue Product:", df.loc[df["Revenue"].idxmax(), "Product"])
print("Most Profitable Product:", df.loc[df["Profit"].idxmax(), "Product"])
print("Average Profit:", np.mean(df["Profit"]))

