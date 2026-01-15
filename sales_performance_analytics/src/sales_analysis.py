import pandas as pd

def load_sales_data(file_path):
    return pd.read_csv(file_path)

def calculate_kpis(df):
    return {
        "total_revenue": df["revenue"].sum(),
        "average_order_value": df["revenue"].mean(),
        "total_quantity_sold": df["quantity"].sum()
    }
