"""
Sales Feature Engineering

This module creates analytical features from the cleaned
sales dataset.

Created features:
- gross_sales
- discount_amount
- net_sales
- order_month
- order_year
- order_month_name
"""

import pandas as pd


CLEAN_PATH = "01_data/02_processed/sales_clean.csv"
FEATURE_PATH = "01_data/02_processed/sales_features.csv"


def main():

    # --------------------------------------------------
    # Load cleaned dataset
    # --------------------------------------------------

    df = pd.read_csv(CLEAN_PATH)

    print("Original shape:")
    print(df.shape)


    # --------------------------------------------------
    # Convert order date
    # --------------------------------------------------

    df["order_date"] = pd.to_datetime(
        df["order_date"],
        errors="coerce"
    )


    # --------------------------------------------------
    # Gross sales
    # --------------------------------------------------

    df["gross_sales"] = (
        df["quantity"] *
        df["unit_price"]
    )


    # --------------------------------------------------
    # Discount amount
    # --------------------------------------------------

    df["discount_amount"] = (
        df["gross_sales"] *
        df["discount"]
    )


    # --------------------------------------------------
    # Net sales
    # --------------------------------------------------

    df["net_sales"] = (
        df["gross_sales"] -
        df["discount_amount"]
    )


    # --------------------------------------------------
    # Date features
    # --------------------------------------------------

    df["order_year"] = (
        df["order_date"].dt.year
    )

    df["order_month"] = (
        df["order_date"].dt.month
    )

    df["order_month_name"] = (
        df["order_date"].dt.month_name()
    )


    # --------------------------------------------------
    # Display results
    # --------------------------------------------------

    print("\nFeature columns:")

    print(
        df[
            [
                "order_id",
                "quantity",
                "unit_price",
                "discount",
                "gross_sales",
                "discount_amount",
                "net_sales",
                "order_year",
                "order_month",
                "order_month_name"
            ]
        ].head(10)
    )


    # --------------------------------------------------
    # Save feature dataset
    # --------------------------------------------------

    df.to_csv(
        FEATURE_PATH,
        index=False
    )

    print("\nFeature dataset saved successfully.")
    print(f"Rows: {df.shape[0]}")
    print(f"Columns: {df.shape[1]}")
    print(f"Saved to: {FEATURE_PATH}")


if __name__ == "__main__":
    main()