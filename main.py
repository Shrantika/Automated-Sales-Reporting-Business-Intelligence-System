from src.data_loader import load_data
from src.data_cleaning import clean_data, save_cleaned_data
from src.kpi_calculator import calculate_kpis
from src.report_generator import generate_reports
def main():
    df = load_data("data/raw/train.csv")
    cleaned_df = clean_data(df)
    save_cleaned_data(cleaned_df, "data/cleaned/cleaned_sales.csv")
    kpis = calculate_kpis(cleaned_df)
    print("BUSINESS KPIs")
    for key, value in kpis.items():
        print(f"{key}:")
        print(value)
        print("-" * 40)
    generate_reports(kpis)

if __name__ == "__main__":
    main()