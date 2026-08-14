"""
Sales Data Generator

Generates a realistic synthetic sales dataset
for the Pandas Sales Analysis project.
"""

import random
from datetime import datetime, timedelta

import pandas as pd


random.seed(42)


CUSTOMERS = [
    ("C001", "Ali Ahmadi", "Regular", "Tehran"),
    ("C002", "Sara Mohammadi", "VIP", "Shiraz"),
    ("C003", "Reza Hosseini", "Regular", "Tehran"),
    ("C004", "Mina Karimi", "New", "Tabriz"),
    ("C005", "Nima Rezaei", "Regular", "Mashhad"),
    ("C006", "Zahra Moradi", "VIP", "Tehran"),
    ("C007", "Amir Jafari", "Regular", "Isfahan"),
    ("C008", "Leila Ahmadi", "New", "Karaj"),
    ("C009", "Hamed Rahimi", "Regular", "Ahvaz"),
    ("C010", "Maryam Ebrahimi", "VIP", "Rasht"),
]


PRODUCTS = [
    ("P001", "Laptop", "Electronics", 900),
    ("P002", "Smartphone", "Electronics", 650),
    ("P003", "Wireless Mouse", "Electronics", 35),
    ("P004", "Keyboard", "Electronics", 55),
    ("P005", "Headphones", "Electronics", 120),
    ("P006", "Coffee Maker", "Home & Kitchen", 180),
    ("P007", "Blender", "Home & Kitchen", 110),
    ("P008", "T-Shirt", "Clothing", 35),
    ("P009", "Sneakers", "Clothing", 95),
    ("P010", "Backpack", "Clothing", 65),
    ("P011", "Perfume", "Beauty", 85),
    ("P012", "Skincare Set", "Beauty", 70),
    ("P013", "Football", "Sports", 45),
    ("P014", "Yoga Mat", "Sports", 30),
    ("P015", "Novel", "Books", 20),
    ("P016", "Programming Book", "Books", 45),
]


PAYMENT_METHODS = [
    "Cash",
    "Card",
    "Online",
    "Wallet",
    "Bank Transfer",
]


ORDER_STATUSES = [
    "Completed",
    "Cancelled",
    "Returned",
    "Pending",
]


SALES_CHANNELS = [
    "Website",
    "Mobile App",
    "Store",
    "Social Media",
    "Marketplace",
]


def random_date(start_date, end_date):
    """Generate a random date between two dates."""

    days_difference = (end_date - start_date).days

    random_days = random.randint(
        0,
        days_difference
    )

    return start_date + timedelta(
        days=random_days
    )


def choose_order_status():
    """Select an order status using realistic probabilities."""

    return random.choices(
        ORDER_STATUSES,
        weights=[85, 5, 7, 3],
        k=1
    )[0]


def choose_customer():
    """Select a customer from the customer list."""

    return random.choice(CUSTOMERS)


def choose_product():
    """Select a product from the product list."""

    return random.choice(PRODUCTS)


def generate_order(order_number):
    """Generate one synthetic sales order."""

    customer = choose_customer()
    product = choose_product()

    customer_id = customer[0]
    customer_name = customer[1]
    customer_type = customer[2]
    city = customer[3]

    product_id = product[0]
    product_name = product[1]
    category = product[2]
    unit_price = product[3]

    start_date = datetime(2024, 1, 1)
    end_date = datetime(2024, 12, 31)

    order_date = random_date(
        start_date,
        end_date
    )

    quantity = random.randint(1, 5)

    discount = random.choice([
        0,
        0,
        0.05,
        0.10,
        0.15,
        0.20
    ])

    return {
        "order_id": f"O{order_number:05d}",
        "order_date": order_date,
        "customer_id": customer_id,
        "customer_name": customer_name,
        "customer_type": customer_type,
        "product_id": product_id,
        "product_name": product_name,
        "category": category,
        "city": city,
        "quantity": quantity,
        "unit_price": unit_price,
        "discount": discount,
        "payment_method": random.choice(
            PAYMENT_METHODS
        ),
        "order_status": choose_order_status(),
        "sales_channel": random.choice(
            SALES_CHANNELS
        ),
    }


def generate_sales_data(number_of_orders=1000):
    """Generate a complete synthetic sales dataset."""

    orders = []

    for order_number in range(
        1,
        number_of_orders + 1
    ):
        orders.append(
            generate_order(order_number)
        )

    return pd.DataFrame(orders)


def main():
    """Generate and save the raw sales dataset."""

    df = generate_sales_data(1000)

    df.to_csv(
        "01_data/01_raw/sales_raw.csv",
        index=False
    )

    print("Sales dataset generated successfully.")
    print(f"Rows: {len(df)}")
    print(f"Columns: {len(df.columns)}")


if __name__ == "__main__":
    main()