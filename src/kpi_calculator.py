import pandas as pd
def calculate_kpis(df) :
    kpis={}

    #overall kpi
    kpis["Total Sales"] = round(df["Sales"].sum(),2)
    #kpis["Total Profit"] = round(df["Profit"].sum(),2)
    kpis["Total Orders"] = df["Order ID"].nunique()

    kpis["Average Order Value"] = round(kpis["Total Sales"]/kpis["Total Orders"],2)
    #kpis["Profit Margin(%)"] = round(kpis["Total Profit"]/kpis["Total Sales"]*100,2)

    #sales by category
    kpis["Sales by Category"] = (df.groupby("Category")["Sales"].sum().sort_values(ascending=False))

    #sales by sub-category
    kpis["Sales by Sub-Category"] = (df.groupby("Sub-Category")["Sales"].sum().sort_values(ascending=False))

    #Sales by region
    kpis["Sales by Region"] = (df.groupby("Region")["Sales"].sum().sort_values(ascending=False))

    #Sales by segment
    kpis["Sales by Segment"] = (df.groupby("Segment")["Sales"].sum().sort_values(ascending=False))

    #top 10 products
    kpis["top 10 products"] = (df.groupby("Product Name")["Sales"].sum().sort_values(ascending=False).head(10))

    #Monthly Sales trend
    monthly_sales = (df.groupby(df["Order Date"].dt.to_period("M"))["Sales"].sum())
    monthly_sales.index = monthly_sales.index.astype(str)
    kpis["Monthly Sales"] = monthly_sales

    return kpis