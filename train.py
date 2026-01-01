import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from xgboost import XGBRegressor

# Load data
df = pd.read_csv("water_consumption.csv")

# Feature engineering
df["date"] = pd.to_datetime(df["date"])
df["day_of_week"] = df["date"].dt.dayofweek
df["is_weekend"] = df["day_of_week"].isin([5, 6]).astype(int)
df = df.drop(columns=["date"])

# One-hot encoding
df = pd.get_dummies(df, columns=["zone"], drop_first=True)

# Split X and y
X = df.drop(columns=["consumption_litres"])
y = df["consumption_litres"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = XGBRegressor(
    n_estimators=200,
    learning_rate=0.05,
    max_depth=5,
    random_state=42
)

model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
print("R2 Score:", r2_score(y_test, y_pred))

# Save model
joblib.dump(model, "models/water_demand_model.pkl")
print("Model saved successfully")
