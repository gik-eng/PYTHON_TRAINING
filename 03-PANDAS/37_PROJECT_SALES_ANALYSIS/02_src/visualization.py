"""
Sales Analysis Project — Visualization

This module creates and saves visualizations
from the processed sales dataset.

Visualizations:
- Sales by category
- Sales by product
- Sales by city
- Monthly sales
- Sales by customer type
- Sales by payment method
- Sales by sales channel
- Sales by order status
"""

from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt


# ==================================================
# PATHS
# ==================================================

DATA_PATH = Path("01_data/02_processed/sales_features.csv")
OUTPUT_DIR = Path("03_outputs")

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


# ==================================================
# LOAD DATA
# ==================================================

df = pd.read_csv(DATA_PATH)


# ==================================================
# SALES BY CATEGORY
# ==================================================

sales_by_category = (
    df.groupby("category")["net_sales"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(10, 6))

sales_by_category.plot(
    kind="bar"
)

plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "sales_by_category.png",
    dpi=300
)

plt.show()
plt.close()


# ==================================================
# SALES BY PRODUCT
# ==================================================

sales_by_product = (
    df.groupby("product_name")["net_sales"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(12, 7))

sales_by_product.plot(
    kind="bar"
)

plt.title("Sales by Product")
plt.xlabel("Product")
plt.ylabel("Sales")

plt.xticks(rotation=60)
plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "sales_by_product.png",
    dpi=300
)

plt.show()
plt.close()


# ==================================================
# SALES BY CITY
# ==================================================

sales_by_city = (
    df.groupby("city")["net_sales"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(10, 6))

sales_by_city.plot(
    kind="bar"
)

plt.title("Sales by City")
plt.xlabel("City")
plt.ylabel("Sales")

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "sales_by_city.png",
    dpi=300
)

plt.show()
plt.close()


# ==================================================
# MONTHLY SALES
# ==================================================

monthly_sales = (
    df.groupby(
        ["order_year", "order_month"]
    )["net_sales"]
    .sum()
)

monthly_sales.index = (
    monthly_sales.index
    .map(lambda x: f"{int(x[0])}-{int(x[1]):02d}")
)

plt.figure(figsize=(12, 6))

monthly_sales.plot(
    kind="line",
    marker="o"
)

plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "monthly_sales.png",
    dpi=300
)

plt.show()
plt.close()


# ==================================================
# SALES BY CUSTOMER TYPE
# ==================================================

sales_by_customer_type = (
    df.groupby("customer_type")["net_sales"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(8, 6))

sales_by_customer_type.plot(
    kind="bar"
)

plt.title("Sales by Customer Type")
plt.xlabel("Customer Type")
plt.ylabel("Sales")

plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "sales_by_customer_type.png",
    dpi=300
)

plt.show()
plt.close()


# ==================================================
# SALES BY PAYMENT METHOD
# ==================================================

sales_by_payment = (
    df.groupby("payment_method")["net_sales"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(10, 6))

sales_by_payment.plot(
    kind="bar"
)

plt.title("Sales by Payment Method")
plt.xlabel("Payment Method")
plt.ylabel("Sales")

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "sales_by_payment_method.png",
    dpi=300
)

plt.show()
plt.close()


# ==================================================
# SALES BY SALES CHANNEL
# ==================================================

sales_by_channel = (
    df.groupby("sales_channel")["net_sales"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(10, 6))

sales_by_channel.plot(
    kind="bar"
)

plt.title("Sales by Sales Channel")
plt.xlabel("Sales Channel")
plt.ylabel("Sales")

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "sales_by_channel.png",
    dpi=300
)

plt.show()
plt.close()


# ==================================================
# ORDER STATUS
# ==================================================

sales_by_status = (
    df.groupby("order_status")["net_sales"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(8, 6))

sales_by_status.plot(
    kind="bar"
)

plt.title("Sales by Order Status")
plt.xlabel("Order Status")
plt.ylabel("Sales")

plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "order_status.png",
    dpi=300
)

plt.show()
plt.close()


# ==================================================
# FINISHED
# ==================================================

print("=" * 50)
print("VISUALIZATION COMPLETED")
print("=" * 50)

print(f"Charts saved to: {OUTPUT_DIR}")