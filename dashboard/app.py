import streamlit as st
import pandas as pd
from pathlib import Path
from components import display_kpi_card

from charts import (
    create_monthly_sales_chart,
    create_category_chart,
    create_region_chart,
    create_top_products_chart,
    create_segment_chart
)

#configure the page
st.set_page_config(
    page_title="Automated Sales Dashboard",
    page_icon="📊",
    layout="wide"
)

# Load custom CSS
css_path = Path(__file__).parent / "style.css"

with open(css_path) as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

#Dashboard title
st.markdown(
    '<div class="dashboard-title">📊 Automated Sales Reporting Dashboard</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="dashboard-subtitle">'
    'Interactive business intelligence dashboard for sales performance analysis'
    '</div>',
    unsafe_allow_html=True
)

#Load the clean dataset
df = pd.read_csv("data/cleaned/cleaned_sales.csv")


# -----------------------------
# Sidebar Filters
# -----------------------------
st.sidebar.header("Filters")
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

filters = {
    "Order Year": selected_year,
    "Region": selected_region,
    "Category": selected_category,
    "Segment": selected_segment
}

for column, value in filters.items():
    if value != "All":
        filtered_df = filtered_df[filtered_df[column] == value]

# Handle empty results
if filtered_df.empty:
    st.warning("⚠️ No data available for the selected filters.")
    st.stop()

# -----------------------------
# KPI Calculations
# -----------------------------
total_sales = filtered_df["Sales"].sum()
total_orders = filtered_df["Order ID"].nunique()
average_order_value = total_sales / total_orders if total_orders > 0 else 0
total_categories = filtered_df["Category"].nunique()

# -----------------------------
# KPI Cards
# -----------------------------
col1, col2, col3, col4 = st.columns(4)

with col1:
    display_kpi_card(
        "Total Sales",
        f"${total_sales:,.2f}",
        "💰"
    )

with col2:
    display_kpi_card(
        "Total Orders",
        f"{total_orders:,}",
        "📦"
    )

with col3:
    display_kpi_card(
        "Avg Order Value",
        f"${average_order_value:,.2f}",
        "💵"
    )

with col4:
    display_kpi_card(
        "Categories",
        f"{total_categories}",
        "🛍️"
    )

# -----------------------------
# Monthly Sales Trend
# -----------------------------

fig_monthly = create_monthly_sales_chart(filtered_df)

st.plotly_chart(
    fig_monthly,
    use_container_width=True
)

# -----------------------------
# Category & Region Analysis
# -----------------------------

col1, col2 = st.columns(2)

with col1:
    fig_category = create_category_chart(filtered_df)

    st.plotly_chart(
        fig_category,
        use_container_width=True
    )

with col2:
    fig_region = create_region_chart(filtered_df)

    st.plotly_chart(
        fig_region,
        use_container_width=True
    )

# -----------------------------
# Product & Segment Analysis
# -----------------------------


col1, col2 = st.columns(2)

with col1:
    fig_products = create_top_products_chart(filtered_df)

    st.plotly_chart(
        fig_products,
        use_container_width=True
    )

with col2:
    fig_segment = create_segment_chart(filtered_df)

    st.plotly_chart(
        fig_segment,
        use_container_width=True
    )