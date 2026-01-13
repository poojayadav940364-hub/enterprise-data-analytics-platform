import pandas as pd
from pathlib import Path

def load_to_snowflake():
    """
    Simulates loading cleaned data into Snowflake RAW schema.
    In production, this would use the Snowflake Python connector.
    """
    input_file = Path("data/clean_users.csv")

    df = pd.read_csv(input_file)

    # Simulated Snowflake load
    print("Connecting to Snowflake...")
    print("Uploading data to RAW.USERS table...")
    print(f"Rows loaded: {len(df)}")
    print("Load completed successfully.")

if __name__ == "__main__":
    load_to_snowflake()
