# Automated Sales Reporting & Business Intelligence System

A Python-based sales analytics project that takes raw sales data, cleans it, calculates useful business metrics, and presents the results through automated reports and an interactive Streamlit dashboard.

## What it does

- Loads sales data from a CSV file
- Cleans and preprocesses the data
- Handles missing and duplicate records
- Converts and extracts information from date columns
- Performs feature engineering
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
```

## How it works

```text
Raw CSV
   ↓
Load Data
   ↓
Clean & Preprocess
   ↓
Feature Engineering
   ↓
Calculate KPIs
   ↓
Generate Reports
   ↓
Streamlit Dashboard
```

## KPIs

- Total Sales
- Total Orders
- Average Order Value
- Sales by Category
- Sales by Region
- Sales by Segment
- Top 10 Products by Sales
- Monthly Sales Trend

## Running the project

### 1. Clone the repository

```bash
git clone https://github.com/Shrantika/Automated-Sales-Reporting-Business-Intelligence-System.git
cd Automated-Sales-Reporting-Business-Intelligence-System
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it:

**Linux / macOS**

```bash
source .venv/bin/activate
```

**Windows**

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the reporting pipeline

```bash
python main.py
```

This processes the sales data and generates the reports.

### 5. Run the dashboard

```bash
streamlit run dashboard/app.py
```

The dashboard will open in your browser.

## Dataset

The project uses the Sample Superstore Sales Dataset from Kaggle.

## Dashboard Preview

Screenshots of the dashboard will be added here.
<img width="1912" height="749" alt="image" src="https://github.com/user-attachments/assets/cf2ae2c9-7bf0-4a29-bcc6-a3390fb410a1" />

<img width="1915" height="839" alt="image" src="https://github.com/user-attachments/assets/e89b9834-10d7-4d7e-9a69-ae59cd01b388" />

## Future Improvements

- Power BI dashboard
- SQL database integration
- Automated email reports
- Sales forecasting
- PDF report generation
- Docker deployment
- Cloud deployment

## Author

**Shrantika**

GitHub:  
https://github.com/Shrantika
