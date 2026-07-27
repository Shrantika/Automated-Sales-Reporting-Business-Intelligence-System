# Automated-Sales-Reporting-Business-Intelligence-System

An end-to-end Business Intelligence system built with Python that automates the process of cleaning sales data, calculating business KPIs, and generating visual reports. This project demonstrates a complete data analytics workflow, from raw CSV files to actionable business insights.

---

## 🚀 Features

- 📂 Load raw sales data from CSV
- 🧹 Data cleaning and preprocessing
  - Remove duplicate records
  - Handle missing values
  - Standardize text fields
  - Convert date columns
  - Feature engineering (Year, Month, Quarter)
- 📈 Business KPI calculation
  - Total Sales
  - Total Orders
  - Average Order Value
  - Sales by Category
  - Sales by Sub-Category
  - Sales by Region
  - Sales by Segment
  - Top 10 Products
  - Monthly Sales Trend
- 📊 Automated report generation
  - Sales by Category
  - Sales by Region
  - Monthly Sales Trend
  - Top 10 Products
- 🏗 Modular project architecture

---

## 🛠 Tech Stack

- Python
- Pandas
- Matplotlib
- Git & GitHub

---

## 📁 Project Structure

```
Automated-Sales-Reporting-Business-Intelligence-System/
│
├── data/
│   ├── raw/
│   └── cleaned/
│
├── notebook/
│   └── data_exploration.ipynb
│
├── src/
│   ├── data_loader.py
│   ├── data_cleaning.py
│   ├── kpi_calculator.py
│   └── report_generator.py
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Workflow

```
Raw CSV
   │
   ▼
Load Data
   │
   ▼
Clean & Preprocess Data
   │
   ▼
Feature Engineering
   │
   ▼
Calculate Business KPIs
   │
   ▼
Generate Visual Reports
```

---

## 📊 KPIs Generated

- Total Sales
- Total Orders
- Average Order Value
- Sales by Category
- Sales by Sub-Category
- Sales by Region
- Sales by Segment
- Top 10 Products by Sales
- Monthly Sales Trend

---

## 📈 Reports Generated

The system automatically generates visual reports including:

- Sales by Category
- Sales by Region
- Monthly Sales Trend
- Top 10 Products by Sales

These reports are automatically saved to the **reports/** directory whenever the project is executed.

---

## 📦 Installation

Clone the repository

```bash
git clone https://github.com/Shrantika/Automated-Sales-Reporting-Business-Intelligence-System.git
```

Navigate to the project directory

```bash
cd Automated-Sales-Reporting-Business-Intelligence-System
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate the environment

Linux / macOS

```bash
source .venv/bin/activate
```

Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

Run the project using

```bash
python main.py
```

The system will:

- Load the dataset
- Clean and preprocess the data
- Calculate business KPIs
- Generate visual reports automatically

---

## 📂 Dataset

Dataset used:

**Sample Superstore Sales Dataset**

Source:
https://www.kaggle.com/datasets/rohitsahoo/sales-forecasting

---

## 📸 Sample Output

### Sales by Category

> *(Add screenshot here)*

### Sales by Region

> *(Add screenshot here)*

### Monthly Sales Trend

> *(Add screenshot here)*

### Top 10 Products

> *(Add screenshot here)*

---

## 🎯 Future Improvements

- Interactive Streamlit Dashboard
- Power BI Dashboard
- PDF Report Generation
- Automated Email Reports
- SQL Database Integration
- Forecasting using Machine Learning
- Docker Support
- Cloud Deployment

---

## 📚 Learning Outcomes

This project helped me practice:

- Data Cleaning
- Exploratory Data Analysis
- Business KPI Design
- Data Visualization
- Modular Python Development
- Git & GitHub
- Business Intelligence Reporting

---

## 👤 Author

**Shrantika**

GitHub:
https://github.com/Shrantika

---
