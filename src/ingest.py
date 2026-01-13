import requests
import pandas as pd
from pathlib import Path

def ingest_api_data():
    """
    Ingests user data from a public API and stores raw data locally.
    """
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    response.raise_for_status()

    data = response.json()
    df = pd.json_normalize(data)

    data_dir = Path("data")
    data_dir.mkdir(exist_ok=True)

    output_path = data_dir / "raw_users.csv"
    df.to_csv(output_path, index=False)

    print("API data ingested successfully.")

if __name__ == "__main__":
    ingest_api_data()
