import pandas as pd
from pathlib import Path

def clean_data():
    """
    Cleans processed user data using business rules.
    """
    input_file = Path("data/processed_users.csv")
    output_file = Path("data/clean_users.csv")

    df = pd.read_csv(input_file)

    # Remove rows with missing critical fields
    df = df.dropna(subset=["email", "username"])

    # Standardize email casing
    df["email"] = df["email"].str.lower()

    # Remove duplicate users
    df = df.drop_duplicates(subset=["id"])

    df.to_csv(output_file, index=False)
    print("Data cleaned successfully.")

if __name__ == "__main__":
    clean_data()
