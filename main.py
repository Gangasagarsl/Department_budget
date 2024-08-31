# import pandas as pd

# # Load the CSV data into a Pandas DataFrame
# data = pd.read_csv("Financials.csv")

# # Strip any extra spaces from column names
# data.columns = data.columns.str.strip()

import pandas as pd
import matplotlib.pyplot as plt

# Load the cleaned CSV data into a Pandas DataFrame
data = pd.read_csv("Cleaned_Financials.csv")

# Strip any extra spaces from column names (if not already done)
data.columns = data.columns.str.strip()

# Filter data for the "Government" department
government_data = data[data["Segment"] == "Government"]

# Identify products with the highest COGS
high_cost_products = government_data.groupby("Product")["COGS"].sum().sort_values(ascending=False)
print("High-Cost Products:")
print(high_cost_products)

# Analyze the impact of discounts on profit
discount_analysis = government_data.groupby("Discount Band")["Profit"].sum()
print("Discount Analysis:")
print(discount_analysis)

# Analyze sales and COGS trends by month
monthly_sales = government_data.groupby("Month Name")["Sales"].sum()
monthly_cogs = government_data.groupby("Month Name")["COGS"].sum()

# Plot high-cost products
plt.figure(figsize=(10, 5))
high_cost_products.plot(kind="bar", title="High-Cost Products")
plt.xlabel("Product")
plt.ylabel("COGS")
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.tight_layout()  # Adjust layout to fit labels
plt.show()

# Plot discount analysis
plt.figure(figsize=(10, 5))
discount_analysis.plot(kind="bar", title="Discount Analysis")
plt.xlabel("Discount Band")
plt.ylabel("Profit")
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.tight_layout()  # Adjust layout to fit labels
plt.show()

# Plot seasonal trends
plt.figure(figsize=(10, 5))
monthly_sales.plot(label="Sales")
monthly_cogs.plot(label="COGS")
plt.title("Seasonal Trends")
plt.xlabel("Month")
plt.ylabel("Amount")
plt.legend()
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.tight_layout()  # Adjust layout to fit labels
plt.show()
