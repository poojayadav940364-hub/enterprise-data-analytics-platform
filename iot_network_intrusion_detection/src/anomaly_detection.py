from sklearn.ensemble import IsolationForest

def detect_anomalies(df):
    """
    Detect anomalies in IoT network traffic using Isolation Forest
    """
    model = IsolationForest(contamination=0.02, random_state=42)

    numeric_df = df.select_dtypes(include='number')
    df['anomaly'] = model.fit_predict(numeric_df)

    return df
