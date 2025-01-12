import pandas as pd

def extract_data(file_path):
    """
    Extract data from an Excel file.
    """
    try:
        data = pd.read_excel(file_path)
        print(f"Data extracted successfully from {file_path}")
        return data
    except Exception as e:
        print(f"Error extracting data: {e}")
        return None
