import pandas as pd
import plotly.express as px


def create_monthly_sales_chart(filtered_df):

    filtered_df = filtered_df.copy()

    filtered_df["Order Date"] = pd.to_datetime(
        filtered_df["Order Date"]
    )

    monthly_sales = (
        filtered_df
        .groupby(
            filtered_df["Order Date"].dt.to_period("M")
        )["Sales"]
        .sum()
        .reset_index()
    )

    monthly_sales["Order Date"] = (
        monthly_sales["Order Date"].dt.to_timestamp()
    )

    fig = px.line(
        monthly_sales,
        x="Order Date",
        y="Sales",
        title="Monthly Sales Trend",
        markers=True
    )

    fig.update_layout(
        title_font=dict(size=22),
        font=dict(size=14),
        xaxis_title="Month",
        yaxis_title="Sales",
        xaxis=dict(
            title_font=dict(size=16),
            tickfont=dict(size=13)
        ),
        yaxis=dict(
            title_font=dict(size=16),
            tickfont=dict(size=13)
        ),
        hovermode="x unified",
        height=450,
        margin=dict(l=60, r=30, t=70, b=60)
    )

    return fig


def create_category_chart(filtered_df):

    category_sales = (
        filtered_df
        .groupby("Category")["Sales"]
        .sum()
        .reset_index()
        .sort_values("Sales", ascending=False)
    )

    fig = px.bar(
        category_sales,
        x="Category",
        y="Sales",
        title="Sales by Category",
        text_auto=".2s"
    )

    fig.update_layout(
        title_font=dict(size=20),
        font=dict(size=14),
        xaxis_title="Category",
        yaxis_title="Sales",
        xaxis=dict(
            title_font=dict(size=15),
            tickfont=dict(size=13)
        ),
        yaxis=dict(
            title_font=dict(size=15),
            tickfont=dict(size=13)
        ),
        height=400,
        margin=dict(l=60, r=30, t=70, b=60)
    )

    return fig


def create_region_chart(filtered_df):

    region_sales = (
        filtered_df
        .groupby("Region")["Sales"]
        .sum()
        .reset_index()
        .sort_values("Sales", ascending=False)
    )

    fig = px.bar(
        region_sales,
        x="Region",
        y="Sales",
        title="Sales by Region",
        text_auto=".2s"
    )

    fig.update_layout(
        title_font=dict(size=20),
        font=dict(size=14),
        xaxis_title="Region",
        yaxis_title="Sales",
        xaxis=dict(
            title_font=dict(size=15),
            tickfont=dict(size=13)
        ),
        yaxis=dict(
            title_font=dict(size=15),
            tickfont=dict(size=13)
        ),
        height=400,
        margin=dict(l=60, r=30, t=70, b=60)
    )

    return fig


def create_top_products_chart(filtered_df):

    top_products = (
        filtered_df
        .groupby("Product Name")["Sales"]
        .sum()
        .reset_index()
        .sort_values("Sales", ascending=False)
        .head(10)
        .sort_values("Sales", ascending=True)
    )

    fig = px.bar(
        top_products,
        x="Sales",
        y="Product Name",
        orientation="h",
        title="Top 10 Products by Sales",
        text_auto=".2s"
    )

    fig.update_layout(
        title_font=dict(size=20),
        font=dict(size=14),
        xaxis_title="Sales",
        yaxis_title="Product",
        xaxis=dict(
            title_font=dict(size=15),
            tickfont=dict(size=13)
        ),
        yaxis=dict(
            title_font=dict(size=15),
            tickfont=dict(size=13)
        ),
        height=500,
        margin=dict(l=180, r=30, t=70, b=60)
    )

    return fig


def create_segment_chart(filtered_df):

    segment_sales = (
        filtered_df
        .groupby("Segment")["Sales"]
        .sum()
        .reset_index()
        .sort_values("Sales", ascending=False)
    )

    fig = px.bar(
        segment_sales,
        x="Segment",
        y="Sales",
        title="Sales by Segment",
        text_auto=".2s"
    )

    fig.update_layout(
        title_font=dict(size=20),
        font=dict(size=14),
        xaxis_title="Segment",
        yaxis_title="Sales",
        xaxis=dict(
            title_font=dict(size=15),
            tickfont=dict(size=13)
        ),
        yaxis=dict(
            title_font=dict(size=15),
            tickfont=dict(size=13)
        ),
        height=400,
        margin=dict(l=60, r=30, t=70, b=60)
    )

    return fig