import pandas as pd

def load_data(file_path):
    """
    Loads a CSV file and returns a Pandas DataFrame.
    """

    try:
        df = pd.read_csv(file_path)
        print("✅ Data loaded successfully.")
        return df

    except FileNotFoundError:
        print("❌ File not found.")
        return None

    except Exception as e:
        print(f"❌ Error: {e}")
        return None