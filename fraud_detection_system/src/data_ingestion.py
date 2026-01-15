import pandas as pd

def load_data(file_path):
    """
    Load transaction data from CSV file
    """
    return pd.read_csv(file_path)
