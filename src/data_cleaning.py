import pandas as pd
def clean_data(df):
    # Remove duplicates
    df = df.drop_duplicates()
    # Remove missing values
    df = df.dropna()
    # Convert date columns
    df["Order Date"] = pd.to_datetime(df["Order Date"], format="%d/%m/%Y")
    df["Ship Date"] = pd.to_datetime(df["Ship Date"], format="%d/%m/%Y")
    # Clean text columns
    text_cols = df.select_dtypes(include=["object", "string"]).columns
    for col in text_cols:
        df[col] = df[col].str.strip()
    # Feature Engineering
    df["Order Year"] = df["Order Date"].dt.year
    df["Order Month"] = df["Order Date"].dt.month_name()
    df["Order Quarter"] = df["Order Date"].dt.quarter
    return df
def save_cleaned_data(df, output_path):
    df.to_csv(output_path, index=False)
    print(f"Cleaned data saved to {output_path}")