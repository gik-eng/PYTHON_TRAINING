"""
Sales Data Quality Analysis

This module inspects the dirty sales dataset and identifies
common data-quality problems before the cleaning stage.

Checks:
- Missing values
- Duplicate rows
- Invalid quantities
- Invalid discounts
- Invalid prices
- Invalid dates
- Inconsistent city names
"""

import pandas as pd


DIRTY_PATH = "01_data/01_raw/sales_dirty.csv"


def main():
    df = pd.read_csv(DIRTY_PATH)

    print("=" * 50)
    print("DATASET OVERVIEW")
    print("=" * 50)

    print(f"Rows: {df.shape[0]}")
    print(f"Columns: {df.shape[1]}")

    print("\nColumns:")
    print(df.columns.tolist())

    print("\nData Types:")
    print(df.dtypes)


    # --------------------------------------------------
    # Missing Values
    # --------------------------------------------------

    print("\n" + "=" * 50)
    print("MISSING VALUES")
    print("=" * 50)

    missing_values = df.isna().sum()

    print(missing_values)


    # --------------------------------------------------
    # Duplicate Rows
    # --------------------------------------------------

    print("\n" + "=" * 50)
    print("DUPLICATE ROWS")
    print("=" * 50)

    duplicate_count = df.duplicated().sum()

    print(f"Duplicate rows: {duplicate_count}")


    # --------------------------------------------------
    # Invalid Quantities
    # --------------------------------------------------

    print("\n" + "=" * 50)
    print("INVALID QUANTITIES")
    print("=" * 50)

    invalid_quantity = df[
        df["quantity"] <= 0
    ]

    print(invalid_quantity[
        ["order_id", "quantity"]
    ])


    # --------------------------------------------------
    # Invalid Discounts
    # --------------------------------------------------

    print("\n" + "=" * 50)
    print("INVALID DISCOUNTS")
    print("=" * 50)

    invalid_discount = df[
        (df["discount"] < 0) |
        (df["discount"] > 1)
    ]

    print(invalid_discount[
        ["order_id", "discount"]
    ])


    # --------------------------------------------------
    # Invalid Prices
    # --------------------------------------------------

    print("\n" + "=" * 50)
    print("INVALID PRICES")
    print("=" * 50)

    invalid_price = df[
        df["unit_price"] <= 0
    ]

    print(invalid_price[
        ["order_id", "unit_price"]
    ])


    # --------------------------------------------------
    # Invalid Dates
    # --------------------------------------------------

    print("\n" + "=" * 50)
    print("INVALID DATES")
    print("=" * 50)

    parsed_dates = pd.to_datetime(
        df["order_date"],
        errors="coerce"
    )

    invalid_dates = df[
        parsed_dates.isna()
    ]

    print(invalid_dates[
        ["order_id", "order_date"]
    ])


    # --------------------------------------------------
    # Inconsistent Cities
    # --------------------------------------------------

    print("\n" + "=" * 50)
    print("CITY VALUES")
    print("=" * 50)

    print(df["city"].value_counts(dropna=False))


if __name__ == "__main__":
    main()
    