from sklearn.preprocessing import LabelEncoder, MinMaxScaler

def preprocess_data(df):
    """
    Cleans and preprocesses transaction data
    """
    # Remove missing values
    df = df.dropna()

    # Encode categorical features
    encoder = LabelEncoder()
    for col in df.select_dtypes(include='object'):
        df[col] = encoder.fit_transform(df[col])

    # Scale numerical features
    scaler = MinMaxScaler()
    df[df.columns] = scaler.fit_transform(df[df.columns])

    return df
