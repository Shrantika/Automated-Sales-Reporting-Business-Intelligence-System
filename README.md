# Automated Sales Reporting & Business Intelligence System

A Python-based sales analytics project that takes raw sales data, cleans it, calculates useful business metrics, and presents the results through reports and an interactive Streamlit dashboard.

## What it does

- Loads sales data from a CSV file
- Cleans and preprocesses the data
- Handles missing and duplicate records
- Converts and extracts information from date columns
- Calculates business KPIs
- Generates sales reports and charts
- Provides an interactive Streamlit dashboard
- Allows filtering by:
  - Year
  - Region
  - Category
  - Segment

## Dashboard

The dashboard includes:

- Total Sales
- Total Orders
- Average Order Value
- Number of Categories
- Monthly Sales Trend
- Sales by Category
- Sales by Region
- Top 10 Products by Sales
- Sales by Segment

The charts and KPIs update when different filters are selected.

## Tech Stack

- Python
- Pandas
- Plotly
- Streamlit
- Matplotlib
- Jupyter Notebook
- Git & GitHub

## Project Structure

```text
Automated-Sales-Reporting-Business-Intelligence-System/
│
├── dashboard/
│   ├── app.py
│   ├── charts.py
│   ├── components.py
│   └── style.css
│
├── data/
│   ├── raw/
│   │   └── train.csv
│   └── cleaned/
│       └── cleaned_sales.csv
│
├── notebook/
│   └── data_exploration.ipynb
│
├── src/
│   ├── data_loader.py
│   ├── data_cleaning.py
│   ├── kpi_calculator.py
│   ├── report_generator.py
│   └── utils.py
│
├── reports/
├── main.py
├── requirements.txt
├── README.md
└── .gitignore

