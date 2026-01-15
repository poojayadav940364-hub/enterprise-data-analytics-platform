import pandas as pd

def load_data(file_path):
    """
    Load IoT network traffic data from CSV file
    """
    return pd.read_csv(file_path)
