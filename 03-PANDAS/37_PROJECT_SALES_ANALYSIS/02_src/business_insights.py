import pandas as pd


INPUT_PATH = "01_data/02_processed/sales_features.csv"


def load_data():
    return pd.read_csv(INPUT_PATH)


def main():

    df = load_data()

    total_sales = df["net_sales"].sum()
    total_orders = len(df)

    print("=" * 50)
    print("BUSINESS INSIGHTS")
    print("=" * 50)

    # ==================================================
    # 1. TOP CATEGORY
    # ==================================================

    category_sales = (
        df.groupby("category")["net_sales"]
        .sum()
        .sort_values(ascending=False)
    )

    top_category = category_sales.idxmax()
    top_category_sales = category_sales.max()

    top_category_share = (
        top_category_sales / total_sales * 100
    )

    print("\n===== TOP CATEGORY =====")
    print(f"Category: {top_category}")
    print(f"Sales: {top_category_sales:,.2f}")
    print(f"Sales share: {top_category_share:.2f}%")

    # ==================================================
    # 2. CATEGORY CONCENTRATION
    # ==================================================

    print("\n===== CATEGORY CONCENTRATION =====")

    for category, sales in category_sales.items():

        share = sales / total_sales * 100

        print(
            f"{category}: "
            f"{sales:,.2f} "
            f"({share:.2f}%)"
        )

    # ==================================================
    # 3. TOP PRODUCT
    # ==================================================

    product_sales = (
        df.groupby("product_name")["net_sales"]
        .sum()
        .sort_values(ascending=False)
    )

    top_product = product_sales.idxmax()
    top_product_sales = product_sales.max()

    top_product_share = (
        top_product_sales / total_sales * 100
    )

    print("\n===== TOP PRODUCT =====")
    print(f"Product: {top_product}")
    print(f"Sales: {top_product_sales:,.2f}")
    print(f"Sales share: {top_product_share:.2f}%")

    # ==================================================
    # 4. TOP 3 PRODUCT CONCENTRATION
    # ==================================================

    top_3_product_sales = product_sales.head(3).sum()

    top_3_product_share = (
        top_3_product_sales / total_sales * 100
    )

    print("\n===== TOP 3 PRODUCT CONCENTRATION =====")
    print(
        f"Top 3 product sales: "
        f"{top_3_product_sales:,.2f}"
    )

    print(
        f"Top 3 product share: "
        f"{top_3_product_share:.2f}%"
    )

    # ==================================================
    # 5. TOP CITY
    # ==================================================

    city_sales = (
        df.groupby("city")["net_sales"]
        .sum()
        .sort_values(ascending=False)
    )

    top_city = city_sales.idxmax()
    top_city_sales = city_sales.max()

    top_city_share = (
        top_city_sales / total_sales * 100
    )

    print("\n===== TOP CITY =====")
    print(f"City: {top_city}")
    print(f"Sales: {top_city_sales:,.2f}")
    print(f"Sales share: {top_city_share:.2f}%")

    # ==================================================
    # 6. SALES CHANNEL ANALYSIS
    # ==================================================

    channel_analysis = (
        df.groupby("sales_channel")
        .agg(
            total_sales=("net_sales", "sum"),
            orders=("order_id", "count"),
            aov=("net_sales", "mean")
        )
        .sort_values(
            "total_sales",
            ascending=False
        )
    )

    best_channel_by_sales = (
        channel_analysis["total_sales"].idxmax()
    )

    best_channel_by_aov = (
        channel_analysis["aov"].idxmax()
    )

    print("\n===== SALES CHANNEL ANALYSIS =====")
    print(channel_analysis)

    print(
        f"\nBest channel by sales: "
        f"{best_channel_by_sales}"
    )

    print(
        f"Best channel by AOV: "
        f"{best_channel_by_aov}"
    )

    # ==================================================
    # 7. ORDER STATUS ANALYSIS
    # ==================================================

    status_analysis = (
        df.groupby("order_status")
        .agg(
            orders=("order_id", "count"),
            sales=("net_sales", "sum")
        )
    )

    print("\n===== ORDER STATUS ANALYSIS =====")
    print(status_analysis)

    # --------------------------------------------------
    # Non-completed orders
    # --------------------------------------------------

    non_completed = df[
        df["order_status"] != "Completed"
    ]

    non_completed_orders = len(non_completed)

    non_completed_sales = (
        non_completed["net_sales"].sum()
    )

    non_completed_order_rate = (
        non_completed_orders / total_orders * 100
    )

    non_completed_sales_rate = (
        non_completed_sales / total_sales * 100
    )

    print(
        f"\nNon-completed orders: "
        f"{non_completed_orders}"
    )

    print(
        f"Non-completed order rate: "
        f"{non_completed_order_rate:.2f}%"
    )

    print(
        f"Non-completed sales: "
        f"{non_completed_sales:,.2f}"
    )

    print(
        f"Non-completed sales rate: "
        f"{non_completed_sales_rate:.2f}%"
    )

    # ==================================================
    # 8. CUSTOMER TYPE ANALYSIS
    # ==================================================

    customer_type_analysis = (
        df.groupby("customer_type")
        .agg(
            total_sales=("net_sales", "sum"),
            orders=("order_id", "count"),
            aov=("net_sales", "mean")
        )
        .sort_values(
            "total_sales",
            ascending=False
        )
    )

    best_customer_type = (
        customer_type_analysis["aov"].idxmax()
    )

    print("\n===== CUSTOMER TYPE ANALYSIS =====")
    print(customer_type_analysis)

    print(
        f"\nHighest AOV customer type: "
        f"{best_customer_type}"
    )

    # ==================================================
    # 9. MONTHLY PERFORMANCE
    # ==================================================

    monthly_sales = (
        df.groupby(
            ["order_year", "order_month"]
        )["net_sales"]
        .sum()
        .sort_values(ascending=False)
    )

    best_month = monthly_sales.idxmax()
    best_month_sales = monthly_sales.max()

    worst_month = monthly_sales.idxmin()
    worst_month_sales = monthly_sales.min()

    monthly_gap = (
        best_month_sales - worst_month_sales
    )

    monthly_gap_percentage = (
        monthly_gap / worst_month_sales * 100
    )

    print("\n===== MONTHLY PERFORMANCE =====")

    print(
        f"Best month: "
        f"{int(best_month[0])}-"
        f"{int(best_month[1]):02d}"
    )

    print(
        f"Best month sales: "
        f"{best_month_sales:,.2f}"
    )

    print(
        f"Worst month: "
        f"{int(worst_month[0])}-"
        f"{int(worst_month[1]):02d}"
    )

    print(
        f"Worst month sales: "
        f"{worst_month_sales:,.2f}"
    )

    print(
        f"Sales gap: "
        f"{monthly_gap:,.2f}"
    )

    print(
        f"Best month was "
        f"{monthly_gap_percentage:.2f}% "
        f"higher than worst month"
    )

    # ==================================================
    # 10. COMPLETED SALES
    # ==================================================

    completed_sales = df.loc[
        df["order_status"] == "Completed",
        "net_sales"
    ].sum()

    completed_orders = (
        df["order_status"] == "Completed"
    ).sum()

    completed_sales_rate = (
        completed_sales / total_sales * 100
    )

    completed_order_rate = (
        completed_orders / total_orders * 100
    )

    print("\n===== COMPLETED SALES =====")

    print(
        f"Total sales: "
        f"{total_sales:,.2f}"
    )

    print(
        f"Completed sales: "
        f"{completed_sales:,.2f}"
    )

    print(
        f"Completed sales rate: "
        f"{completed_sales_rate:.2f}%"
    )

    print(
        f"Completed order rate: "
        f"{completed_order_rate:.2f}%"
    )

    # ==================================================
    # 11. FINAL BUSINESS SUMMARY
    # ==================================================

    print("\n" + "=" * 50)
    print("FINAL BUSINESS SUMMARY")
    print("=" * 50)

    print(
        f"\n1. {top_category} is the leading category "
        f"with {top_category_share:.2f}% of total sales."
    )

    print(
        f"2. {top_product} is the top product "
        f"with {top_product_share:.2f}% of total sales."
    )


    print(
        f"3. The top 3 products account for "
        f"{top_3_product_share:.2f}% of total sales."
    )
    print(
        f"4. {top_city} generates the highest "
        f"sales among cities."
    )

    print(
        f"5. {best_channel_by_aov} has the highest "
        f"average order value."
    )

    print(
        f"6. {completed_sales_rate:.2f}% of total sales "
        f"come from completed orders."
    )

    print(
        f"7. The best month generated "
        f"{monthly_gap_percentage:.2f}% more sales "
        f"than the worst month."
    )


if __name__ == "__main__":
    main()