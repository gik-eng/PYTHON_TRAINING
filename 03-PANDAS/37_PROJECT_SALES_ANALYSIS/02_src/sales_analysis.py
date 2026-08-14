"""
Sales Analysis

This module analyzes the cleaned and feature-engineered
sales dataset.

Main topics:
- Total sales
- Total orders
- Total quantity sold
- Average order value
- Average discount
- Minimum and maximum order value
- Sales statistics
"""

import pandas as pd


FEATURE_PATH = "01_data/02_processed/sales_features.csv"


def main():

    # --------------------------------------------------
    # Load feature dataset
    # --------------------------------------------------

    df = pd.read_csv(FEATURE_PATH)

    print("=" * 50)
    print("SALES ANALYSIS")
    print("=" * 50)


    # --------------------------------------------------
    # Basic sales KPIs
    # --------------------------------------------------

    total_sales = df["net_sales"].sum()

    total_orders = df["order_id"].nunique()

    total_quantity = df["quantity"].sum()

    average_order_value = df["net_sales"].mean()

    average_discount = df["discount"].mean()

    minimum_order_value = df["net_sales"].min()

    maximum_order_value = df["net_sales"].max()

    completed_sales = df.loc[
        df["order_status"] == "Completed",
        "net_sales"
    ].sum()

    completed_orders = df.loc[
        df["order_status"] == "Completed",
        "order_id"
    ].nunique()

    completed_aov = (
        completed_sales / completed_orders
    )


    # --------------------------------------------------
    # Display KPIs
    # --------------------------------------------------

    print("\n===== SALES KPIs =====")

    print(f"Total sales: {total_sales:,.2f}")

    print(f"Total orders: {total_orders:,}")

    print(f"Total quantity sold: {total_quantity:,.0f}")

    print(
        f"Average order value: "
        f"{average_order_value:,.2f}"
    )

    print(
        f"Average discount: "
        f"{average_discount:.2%}"
    )

    print(
        f"Minimum order value: "
        f"{minimum_order_value:,.2f}"
    )

    print(
        f"Maximum order value: "
        f"{maximum_order_value:,.2f}"
    )


    print("\n===== COMPLETED SALES =====")

    print(
        f"Completed sales: "
        f"{completed_sales:,.2f}"
    )

    print(
        f"Completed orders: "
        f"{completed_orders:,}"
    )

    print(
        f"Completed AOV: "
        f"{completed_aov:,.2f}"
    )


    # --------------------------------------------------
    # Sales by category
    # --------------------------------------------------

    sales_by_category = (
        df.groupby("category")["net_sales"]
        .agg(["sum", "mean", "count"])
        .sort_values("sum", ascending=False)
    )

    print("\n===== SALES BY CATEGORY =====")
    print(sales_by_category)


    # --------------------------------------------------
    # Sales by product
    # --------------------------------------------------

    sales_by_product = (
        df.groupby(
            ["product_id", "product_name"]
        )["net_sales"]
        .agg(["sum", "mean", "count"])
        .sort_values("sum", ascending=False)
    )

    print("\n===== SALES BY PRODUCT =====")
    print(sales_by_product)



    # --------------------------------------------------
    # Sales by city
    # --------------------------------------------------

    sales_by_city = (
        df.groupby("city")["net_sales"]
        .agg(["sum", "mean", "count"])
        .sort_values("sum", ascending=False)
    )

    print("\n===== SALES BY CITY =====")
    print(sales_by_city)



    # --------------------------------------------------
    # Sales by customer type
    # --------------------------------------------------

    sales_by_customer_type = (
        df.groupby("customer_type")["net_sales"]
        .agg(["sum", "mean", "count"])
        .sort_values("sum", ascending=False)
    )

    print("\n===== SALES BY CUSTOMER TYPE =====")
    print(sales_by_customer_type)


    # --------------------------------------------------
    # Top customers
    # --------------------------------------------------

    top_customers = (
        df.groupby(
            ["customer_id", "customer_name"]
        )["net_sales"]
        .agg(["sum", "mean", "count"])
        .sort_values("sum", ascending=False)
        .head(10)
    )

    print("\n===== TOP 10 CUSTOMERS =====")
    print(top_customers)


    # --------------------------------------------------
    # Monthly sales analysis
    # --------------------------------------------------

    monthly_sales = (
        df.groupby(
            ["order_year", "order_month"]
        )["net_sales"]
        .agg(["sum", "mean", "count"])
        .sort_index()
    )

    print("\n===== MONTHLY SALES =====")
    print(monthly_sales)


    # --------------------------------------------------
    # Best month
    # --------------------------------------------------

    best_month = (
        monthly_sales["sum"]
        .idxmax()
    )

    best_month_sales = (
        monthly_sales["sum"]
        .max()
    )

    print("\n===== BEST MONTH =====")
    print(f"Best month: {best_month}")
    print(f"Sales: {best_month_sales:,.2f}")


    # --------------------------------------------------
    # Worst month
    # --------------------------------------------------

    worst_month = (
        monthly_sales["sum"]
        .idxmin()
    )

    worst_month_sales = (
        monthly_sales["sum"]
        .min()
    )

    print("\n===== WORST MONTH =====")
    print(f"Worst month: {worst_month}")
    print(f"Sales: {worst_month_sales:,.2f}")

    # --------------------------------------------------
    # Sales by payment method
    # --------------------------------------------------

    sales_by_payment = (
        df.groupby("payment_method")["net_sales"]
        .agg(["sum", "mean", "count"])
        .sort_values("sum", ascending=False)
    )

    print("\n===== SALES BY PAYMENT METHOD =====")
    print(sales_by_payment)


    # --------------------------------------------------
    # Sales by sales channel
    # --------------------------------------------------

    sales_by_channel = (
        df.groupby("sales_channel")["net_sales"]
        .agg(["sum", "mean", "count"])
        .sort_values("sum", ascending=False)
    )

    print("\n===== SALES BY SALES CHANNEL =====")
    print(sales_by_channel)


    # --------------------------------------------------
    # Order status analysis
    # --------------------------------------------------

    orders_by_status = (
        df.groupby("order_status")
        .agg(
            orders=("order_id", "nunique"),
            sales=("net_sales", "sum")
        )
        .sort_values("orders", ascending=False)
    )

    print("\n===== ORDER STATUS =====")
    print(orders_by_status)


    # --------------------------------------------------
    # Sales statistics
    # --------------------------------------------------

    print("\n===== SALES STATISTICS =====")

    print(
        df["net_sales"].describe()
    )


if __name__ == "__main__":
    main()