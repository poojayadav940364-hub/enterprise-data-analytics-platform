from ingest import ingest_api_data
from preprocess import preprocess_data
from clean import clean_data
from load import load_to_snowflake

def run_pipeline():
    """
    Runs the full enterprise data and analytics pipeline.
    """
    print("Starting enterprise data pipeline...")

    ingest_api_data()
    preprocess_data()
    clean_data()
    load_to_snowflake()

    print("Enterprise data pipeline completed successfully.")

if __name__ == "__main__":
    run_pipeline()
