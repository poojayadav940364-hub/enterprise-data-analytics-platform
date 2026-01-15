def calculate_fraud_rate(df):
    """
    Calculates fraud percentage in the dataset
    """
    return df["is_fraud"].mean() * 100
