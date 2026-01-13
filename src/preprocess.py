import pandas as pd
import numpy as np
from pathlib import Path

def preprocess_data():
    """
    Applies NumPy-based feature engineering to raw API data.
    """
    raw_file = Path("data/raw_users.csv")
    processed_file = Path("data/processed_users.csv")

    df = pd.read_csv(raw_file)

    # Example numeric feature using NumPy
    name_length = np.vectorize(len)(df["name"].values)
    username_length = np.vectorize(len)(df["username"].values)

    df["name_length"] = name_length
    df["username_length"] = username_length

    df.to_csv(processed_file, index=False)
    print("NumPy-based preprocessing completed.")

if __name__ == "__main__":
    preprocess_data()
