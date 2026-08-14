"""
Create a dirty version of the raw sales dataset.

This script intentionally introduces common data-quality
problems into the raw dataset for cleaning practice.

Introduced problems:
- Missing values
- Duplicate rows
- Invalid quantities
- Invalid discounts
- Inconsistent city names
- Invalid unit prices
- Invalid date values
"""

import pandas as pd


RAW_PATH = "01_data/01_raw/sales_raw.csv"
DIRTY_PATH = "01_data/01_raw/sales_dirty.csv"


def main():
    df = pd.read_csv(RAW_PATH)

    # --------------------------------------------------
    # 1. Missing values
    # --------------------------------------------------

    df.loc[10, "customer_name"] = None
    df.loc[25, "city"] = None
    df.loc[40, "payment_method"] = None
    df.loc[55, "unit_price"] = None


    # --------------------------------------------------
    # 2. Duplicate rows
    # --------------------------------------------------

    duplicate_rows = df.iloc[[5, 15, 25]].copy()

    df = pd.concat(
        [df, duplicate_rows],
        ignore_index=True
    )


    # --------------------------------------------------
    # 3. Invalid quantities
    # --------------------------------------------------

    df.loc[70, "quantity"] = 0
    df.loc[71, "quantity"] = -3


    # --------------------------------------------------
    # 4. Invalid discounts
    # --------------------------------------------------

    df.loc[80, "discount"] = -0.10
    df.loc[81, "discount"] = 1.50


    # --------------------------------------------------
    # 5. Inconsistent city names
    # --------------------------------------------------

    df.loc[90, "city"] = " tehran "
    df.loc[91, "city"] = "TEHRAN"
    df.loc[92, "city"] = "Tehran "


    # --------------------------------------------------
    # 6. Invalid unit prices
    # --------------------------------------------------

    df.loc[100, "unit_price"] = -50
    df.loc[101, "unit_price"] = 0


    # --------------------------------------------------
    # 7. Invalid date values
    # --------------------------------------------------

    df.loc[110, "order_date"] = "not-a-date"
    df.loc[111, "order_date"] = "2024-99-99"


    # --------------------------------------------------
    # Save dirty dataset
    # --------------------------------------------------

    df.to_csv(
        DIRTY_PATH,
        index=False
    )

    print("Dirty dataset created successfully.")
    print(f"Rows: {len(df)}")
    print(f"Columns: {len(df.columns)}")
    print(f"Saved to: {DIRTY_PATH}")


if __name__ == "__main__":
    main()