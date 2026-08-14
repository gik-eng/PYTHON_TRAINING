"""
Sales Data Cleaning

This module cleans the dirty sales dataset by:
- Removing duplicate rows
- Normalizing city names
- Handling missing text values
- Detecting invalid numeric values
- Converting invalid values to NaN
- Converting order dates to datetime
- Saving the cleaned dataset
"""

import pandas as pd


DIRTY_PATH = "01_data/01_raw/sales_dirty.csv"
CLEAN_PATH = "01_data/02_processed/sales_clean.csv"


def main():

    df = pd.read_csv(DIRTY_PATH)

    print("Original shape:")
    print(df.shape)


    # --------------------------------------------------
    # 1. Remove duplicate rows
    # --------------------------------------------------

    df = df.drop_duplicates()


    # --------------------------------------------------
    # 2. Normalize city names
    # --------------------------------------------------

    df["city"] = (
        df["city"]
        .str.strip()
        .str.title()
    )


    # --------------------------------------------------
    # 3. Handle missing text values
    # --------------------------------------------------

    df["customer_name"] = (
        df["customer_name"]
        .fillna("Unknown")
    )

    df["city"] = (
        df["city"]
        .fillna("Unknown")
    )

    df["payment_method"] = (
        df["payment_method"]
        .fillna("Unknown")
    )


    # --------------------------------------------------
    # 4. Handle invalid quantities
    # --------------------------------------------------

    df.loc[
        df["quantity"] <= 0,
        "quantity"
    ] = pd.NA


    # --------------------------------------------------
    # 5. Handle invalid discounts
    # --------------------------------------------------

    invalid_discount = (
        (df["discount"] < 0) |
        (df["discount"] > 1)
    )

    print("Invalid discounts:")
    print(
        df.loc[
            invalid_discount,
            ["order_id", "discount"]
        ]
    )

    df.loc[
        invalid_discount,
        "discount"
    ] = 0
    print("\nDiscount after cleaning:")
    print(df["discount"].isna().sum())

    # --------------------------------------------------
    # 6. Handle invalid prices
    # --------------------------------------------------

    df.loc[
        df["unit_price"] <= 0,
        "unit_price"
    ] = pd.NA


    # --------------------------------------------------
    # 7. Convert dates
    # --------------------------------------------------

    df["order_date"] = pd.to_datetime(
        df["order_date"],
        errors="coerce"
    )



    # --------------------------------------------------
    # 8. Fill missing prices
    # --------------------------------------------------

    df["unit_price"] = (
        df.groupby("product_id")["unit_price"]
        .transform(
              lambda x: x.fillna(x.median())
        )
    )
    # --------------------------------------------------
    # 9. Save cleaned dataset
    # --------------------------------------------------

    df.to_csv(
        CLEAN_PATH,
        index=False
    )


    print("\nCleaned shape:")
    print(df.shape)

    print("\nRemaining missing values:")
    print(df.isna().sum())

    print("\nCleaned dataset saved successfully.")






    # --------------------------------------------------
    # Final validation
    # --------------------------------------------------

    print("\n" + "=" * 50)
    print("FINAL VALIDATION")
    print("=" * 50)

    print("\nDuplicate rows:")
    print(df.duplicated().sum())

    print("\nInvalid quantities:")
    print((df["quantity"] <= 0).sum())

    print("\nInvalid discounts:")
    print(
        (
            (df["discount"] < 0) |
            (df["discount"] > 1)
        ).sum()
    )

    print("\nInvalid prices:")
    print((df["unit_price"] <= 0).sum())

    print("\nInvalid dates:")
    print(df["order_date"].isna().sum())

    print("\nMissing values:")
    print(df.isna().sum())



if __name__ == "__main__":
    main()