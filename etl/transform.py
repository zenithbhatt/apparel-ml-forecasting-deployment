def transform_data(df):
    """
    Transform data by handling missing values and adding features.
    """
    # Example: Drop rows with missing values
    df.dropna(inplace=True)
    # Add a new feature
    df['total_sales'] = df['quantity'] * df['price_per_unit']
    print("Data transformed successfully.")
    return df
