import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("train.csv")

print("Dataset Shape:", df.shape)

# -------------------------------
# 1️⃣ Total Sales
# -------------------------------
total_sales = df["Sales"].sum()
print("Total Sales:", total_sales)

# -------------------------------
# 2️⃣ Category Wise Sales
# -------------------------------
category_sales = df.groupby("Category")["Sales"].sum().sort_values(ascending=False)
print("\nCategory Wise Sales:")
print(category_sales)

# -------------------------------
# 3️⃣ Sub-Category Wise Sales
# -------------------------------
sub_category_sales = df.groupby("Sub-Category")["Sales"].sum().sort_values(ascending=False)
print("\nTop Sub-Categories:")
print(sub_category_sales.head(10))

# -------------------------------
# 4️⃣ Region Wise Sales
# -------------------------------
region_sales = df.groupby("Region")["Sales"].sum().sort_values(ascending=False)
print("\nRegion Wise Sales:")
print(region_sales)

# -------------------------------
# 5️⃣ Top 5 Products by Sales
# -------------------------------
top_products = df.groupby("Product Name")["Sales"].sum().sort_values(ascending=False).head(5)
print("\nTop 5 Products:")
print(top_products)

# -------------------------------
# 6️⃣ Visualization - Category Sales
# -------------------------------
category_sales.plot(kind="bar")
plt.title("Category Wise Sales")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.show()