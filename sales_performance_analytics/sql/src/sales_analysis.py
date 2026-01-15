import pandas as pd

def load_sales_data(file_path):
    return pd.read_csv(file_path)

def calculate_kpis(df):
    kpis = {
        "total_revenue": df["revenue"].sum(),
        "average_order_value": df["revenue"].mean(),
        "total_quantity_sold": df["quantity"].sum()
    }
    return kpis

if __name__ == "__main__":
    df = load_sales_data("../data/sales.csv")
    kpis = calculate_kpis(df)
    print(kpis)
