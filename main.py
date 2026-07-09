from src.data_loader import load_data
from src.data_cleaning import clean_data, save_cleaned_data

df = load_data("data/raw/train.csv")
cleaned_df = clean_data(df)
save_cleaned_data(cleaned_df, "data/cleaned/cleaned_sales.csv")