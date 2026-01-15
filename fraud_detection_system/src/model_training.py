import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE

from preprocessing import preprocess_data

# Load dataset
df = pd.read_csv("../data/fraudTrain.csv")

# Preprocess data
df = preprocess_data(df)

# Split features and target
X = df.drop("is_fraud", axis=1)
y = df["is_fraud"]

# Handle class imbalance
smote = SMOTE(random_state=42)
X_resampled, y_resampled = smote.fit_resample(X, y)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X_resampled, y_resampled, test_size=0.2, random_state=42
)

# Train Random Forest model
model = RandomForestClassifier(n_estimators=200, random_state=42)
model.fit(X_train, y_train)

print("Fraud detection model trained successfully")
