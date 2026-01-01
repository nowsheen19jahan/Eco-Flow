import pandas as pd
import joblib
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Ensure models folder exists
os.makedirs("models", exist_ok=True)

# Load the trained model
model = joblib.load("models/water_demand_model.pkl")

# Load data
df = pd.read_csv("water_consumption.csv")

# Feature engineering
df["date"] = pd.to_datetime(df["date"])
df["day_of_week"] = df["date"].dt.dayofweek
df["is_weekend"] = df["day_of_week"].isin([5, 6]).astype(int)
df = df.drop(columns=["date"])

# One-hot encoding (match training)
df = pd.get_dummies(df, columns=["zone"], drop_first=True)

# Split features and target
X = df.drop(columns=["consumption_litres"])
y = df["consumption_litres"]

# Split train/test (same as training)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Predict on test set
y_pred = model.predict(X_test)

# Compute metrics
r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = mse ** 0.5

print("Model Evaluation Metrics:")
print(f"R² Score: {r2:.4f}")
print(f"MAE: {mae:.2f} litres")
print(f"RMSE: {rmse:.2f} litres")

# Optional: plot predicted vs actual
plt.figure(figsize=(8,5))
sns.scatterplot(x=y_test, y=y_pred)
plt.xlabel("Actual Consumption (litres)")
plt.ylabel("Predicted Consumption (litres)")
plt.title("Actual vs Predicted Water Consumption")
plt.show()

# Optional: residual plot
residuals = y_test - y_pred
plt.figure(figsize=(8,5))
sns.histplot(residuals, kde=True, color='orange')
plt.xlabel("Residuals (litres)")
plt.title("Prediction Residuals")
plt.show()
