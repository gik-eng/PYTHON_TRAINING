# Pandas Sales Analysis Project

## Overview

This project is an end-to-end sales data analysis project built with **Python and Pandas**.

The goal of the project is to simulate a realistic sales dataset, inspect and clean the data, create analytical features, perform sales analysis, generate visualizations, and extract business insights.

The project follows a complete data analysis workflow:

```text
Raw Data
   ↓
Data Inspection
   ↓
Data Cleaning
   ↓
Feature Engineering
   ↓
Sales Analysis
   ↓
Visualization
   ↓
Business Insights
```

---

## Technologies

* Python
* Pandas
* Matplotlib

---

## Dataset

The project uses a generated sales dataset containing **1,003 raw records** and **15 columns**.

After the cleaning process, the dataset contains **1,000 valid records**.

Main columns include:

* `order_id`
* `order_date`
* `customer_id`
* `customer_name`
* `customer_type`
* `product_id`
* `product_name`
* `category`
* `city`
* `quantity`
* `unit_price`
* `discount`
* `payment_method`
* `order_status`
* `sales_channel`

The raw dataset intentionally contains issues such as:

* Missing values
* Duplicate rows
* Invalid quantities
* Invalid prices
* Invalid discounts
* Invalid dates
* Inconsistent city values

This allows the project to demonstrate a realistic data-cleaning workflow.

---

## Project Structure

```text
37_PROJECT_SALES_ANALYSIS/
│
├── 01_data/
│   ├── 01_raw/
│   └── 02_processed/
│
├── 02_src/
│   ├── generate_data.py
│   ├── analysis.py
│   ├── cleaning_data.py
│   ├── feature_engineering.py
│   ├── sales_analysis.py
│   ├── visualization.py
│   └── business_insights.py
│
├── 03_outputs/
│   └── charts/
│
└── README.md
```

---

## Analysis Workflow

### 1. Data Generation

`generate_data.py` creates the initial sales dataset and saves it as a raw CSV file.

The generated data contains realistic sales-related information such as customers, products, categories, cities, prices, discounts, payment methods, order statuses, and sales channels.

---

### 2. Data Inspection

`analysis.py` is used to inspect the raw dataset.

The analysis includes:

* Dataset shape
* Column names
* Data types
* Missing values
* Duplicate rows
* Invalid quantities
* Invalid discounts
* Invalid prices
* Invalid dates
* Categorical value inspection
* Descriptive statistics

---

### 3. Data Cleaning

`cleaning_data.py` prepares the dataset for analysis.

The cleaning process handles:

* Duplicate rows
* Missing values
* Invalid quantities
* Invalid prices
* Invalid discounts
* Invalid dates
* Inconsistent city values

The cleaned dataset is saved in the processed-data directory.

---

### 4. Feature Engineering

`feature_engineering.py` creates additional analytical features from the cleaned dataset.

Examples include:

* `gross_sales`
* `discount_amount`
* `net_sales`
* `order_year`
* `order_month`
* `order_month_name`

These features make the dataset easier to analyze.

---

### 5. Sales Analysis

`sales_analysis.py` calculates important sales metrics and performs grouped analysis.

The analysis covers:

* Total sales
* Total orders
* Total quantity sold
* Average order value
* Average discount
* Completed sales
* Sales by category
* Sales by product
* Sales by city
* Sales by customer type
* Top customers
* Monthly sales
* Payment method performance
* Sales channel performance
* Order status analysis
* Best and worst months

---

### 6. Visualization

`visualization.py` creates charts from the processed dataset.

The visualizations cover different aspects of the sales data, including:

* Sales by category
* Sales by product
* Sales by city
* Monthly sales
* Sales by customer type
* Sales by payment method
* Sales by sales channel
* Order status

The generated charts are stored in the output directory.

---

### 7. Business Insights

`business_insights.py` converts the analysis results into business-oriented findings.

The analysis includes:

* Category concentration
* Product concentration
* City performance
* Sales channel performance
* Customer type performance
* Order completion performance
* Monthly performance
* Non-completed sales
* Best and worst month comparison

---

## Key Findings

Based on the final analysis:

* **Electronics** is the leading category, generating **70.82%** of total sales.
* **Laptop** is the top-selling product, accounting for **35.25%** of total sales.
* The **top 3 products** account for **68.06%** of total sales.
* **Tehran** generates the highest city-level sales, representing **29.42%** of total sales.
* **Mobile App** has the highest average order value at approximately **498.44**.
* **86.00%** of orders are completed.
* Completed orders account for **83.15%** of total sales.
* **14.00%** of orders are not completed.
* Non-completed orders represent **16.85%** of total sales value.
* The best-performing month was **February 2024**, with sales of **46,292.25**.
* The weakest month was **April 2024**, with sales of **25,223.25**.
* February generated **21,069.00** more sales than April, meaning the best month performed **83.53% higher** than the worst month.

---

## Main KPIs

| Metric               |      Value |
| -------------------- | ---------: |
| Total Sales          | 449,983.75 |
| Total Orders         |      1,000 |
| Total Quantity Sold  |      3,026 |
| Average Order Value  |     450.89 |
| Average Discount     |      8.62% |
| Completed Orders     |        860 |
| Completed Sales      | 374,183.25 |
| Completed Order Rate |     86.00% |
| Completed Sales Rate |     83.15% |

---

## How to Run

From the project root directory:

```bash
python 02_src/generate_data.py
```

Run the data inspection:

```bash
python 02_src/analysis.py
```

Run data cleaning:

```bash
python 02_src/cleaning_data.py
```

Run feature engineering:

```bash
python 02_src/feature_engineering.py
```

Run sales analysis:

```bash
python 02_src/sales_analysis.py
```

Generate visualizations:

```bash
python 02_src/visualization.py
```

Generate business insights:

```bash
python 02_src/business_insights.py
```

---

## Project Goal

This project was built as part of a structured Python and Pandas learning path.

The focus was not only on calculating sales metrics, but on practicing a complete data-analysis workflow:

**data generation → inspection → cleaning → feature engineering → analysis → visualization → business insights**

The project is designed to demonstrate practical Pandas skills using a realistic sales-analysis scenario.
