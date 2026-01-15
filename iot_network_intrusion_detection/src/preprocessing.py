from sklearn.preprocessing import MinMaxScaler

def preprocess_data(df):
    """
    Clean and scale IoT network traffic data
    """
    df = df.dropna()

    numeric_cols = df.select_dtypes(include='number').columns
    scaler = MinMaxScaler()
    df[numeric_cols] = scaler.fit_transform(df[numeric_cols])

    return df
