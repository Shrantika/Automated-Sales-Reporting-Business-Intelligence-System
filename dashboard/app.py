import streamlit as st
import pandas as pd
import plotly.express as px

#configure the page
st.set_page_config(
    page_title="Automated Sales Dashboard",
    page_icon="📊",
    layout="wide"
)

#Dashboard title
st.title("📊 Automated Sales Reporting Dashboard")

#Load the clean dataset
df = pd.read_csv("data/cleaned/cleaned_sales.csv")


# -----------------------------
# Sidebar Filters
# -----------------------------
st.sidebar.header("Filters")
st.sidebar.write("Sidebar is working!")
# Year Filter
selected_year = st.sidebar.selectbox(
    "Select Year",
    options=["All"] + sorted(df["Order Year"].unique().tolist())
)

# Region Filter
selected_region = st.sidebar.selectbox(
    "Select Region",
    options=["All"] + sorted(df["Region"].unique().tolist())
)

# Category Filter
selected_category = st.sidebar.selectbox(
    "Select Category",
    options=["All"] + sorted(df["Category"].unique().tolist())
)

# Segment Filter
selected_segment = st.sidebar.selectbox(
    "Select Segment",
    options=["All"] + sorted(df["Segment"].unique().tolist())
)

# -----------------------------
# Apply Filters
# -----------------------------
filtered_df = df.copy()

# Filter by Year
if selected_year != "All":
    filtered_df = filtered_df[filtered_df["Order Year"] == selected_year]

# Filter by Region
if selected_region != "All":
    filtered_df = filtered_df[filtered_df["Region"] == selected_region]

# Filter by Category
if selected_category != "All":
    filtered_df = filtered_df[filtered_df["Category"] == selected_category]

# Filter by Segment
if selected_segment != "All":
    filtered_df = filtered_df[filtered_df["Segment"] == selected_segment]


# -----------------------------
# KPI Calculations
# -----------------------------
total_sales = filtered_df["Sales"].sum()
total_orders = filtered_df["Order ID"].nunique()
average_order_value = total_sales / total_orders if total_orders > 0 else 0
total_categories = filtered_df["Category"].nunique()


# KPI Cards
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("💰 Total Sales", f"${total_sales:,.2f}")

with col2:
    st.metric("📦 Total Orders", total_orders)

with col3:
    st.metric("💵 Avg Order Value", f"${average_order_value:,.2f}")

with col4:
    st.metric("🛍️ Categories", total_categories)

# -----------------------------
# Monthly Sales Trend
# -----------------------------

filtered_df["Order Date"] = pd.to_datetime(filtered_df["Order Date"])

monthly_sales = (
    filtered_df
    .groupby(filtered_df["Order Date"].dt.to_period("M"))["Sales"]
    .sum()
    .reset_index()
)

monthly_sales["Order Date"] = monthly_sales["Order Date"].dt.to_timestamp()

fig = px.line(
    monthly_sales,
    x="Order Date",
    y="Sales",
    title="Monthly Sales Trend",
    markers=True
)

fig.update_layout(
    xaxis_title="Month",
    yaxis_title="Sales",
    hovermode="x unified"
)

st.plotly_chart(fig, use_container_width=True)

# -----------------------------
# Sales by Category
# -----------------------------

category_sales = (
    filtered_df
    .groupby("Category")["Sales"]
    .sum()
    .reset_index()
    .sort_values("Sales", ascending=False)
)

fig_category = px.bar(
    category_sales,
    x="Category",
    y="Sales",
    title="Sales by Category",
    text_auto=".2s"
)

fig_category.update_layout(
    xaxis_title="Category",
    yaxis_title="Sales",
    hovermode="x unified"
)

st.plotly_chart(
    fig_category,
    use_container_width=True
)

# -----------------------------
# Sales by Region
# -----------------------------

region_sales = (
    filtered_df
    .groupby("Region")["Sales"]
    .sum()
    .reset_index()
    .sort_values("Sales", ascending=False)
)

fig_region = px.bar(
    region_sales,
    x="Region",
    y="Sales",
    title="Sales by Region",
    text_auto=".2s"
)

fig_region.update_layout(
    xaxis_title="Region",
    yaxis_title="Sales",
    hovermode="x unified"
)

st.plotly_chart(
    fig_region,
    use_container_width=True
)

# -----------------------------
# Top 10 Products by Sales
# -----------------------------

top_products = (
    filtered_df
    .groupby("Product Name")["Sales"]
    .sum()
    .reset_index()
    .sort_values("Sales", ascending=False)
    .head(10)
    .sort_values("Sales", ascending=True)
)

fig_products = px.bar(
    top_products,
    x="Sales",
    y="Product Name",
    orientation="h",
    title="Top 10 Products by Sales",
    text_auto=".2s"
)

fig_products.update_layout(
    xaxis_title="Sales",
    yaxis_title="Product",
    hovermode="y unified"
)

st.plotly_chart(
    fig_products,
    use_container_width=True
)

# -----------------------------
# Sales by Segment
# -----------------------------

segment_sales = (
    filtered_df
    .groupby("Segment")["Sales"]
    .sum()
    .reset_index()
    .sort_values("Sales", ascending=False)
)

fig_segment = px.bar(
    segment_sales,
    x="Segment",
    y="Sales",
    title="Sales by Segment",
    text_auto=".2s"
)

fig_segment.update_layout(
    xaxis_title="Segment",
    yaxis_title="Sales",
    hovermode="x unified"
)

st.plotly_chart(
    fig_segment,
    use_container_width=True
)