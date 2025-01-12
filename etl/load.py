def load_data(df, output_path):
    """
    Load transformed data to a CSV file.
    """
    try:
        df.to_csv(output_path, index=False)
        print(f"Data loaded successfully to {output_path}")
    except Exception as e:
        print(f"Error loading data: {e}")
