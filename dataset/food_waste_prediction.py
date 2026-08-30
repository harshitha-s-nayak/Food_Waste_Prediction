print("====================================")
print("     FOOD WASTE PREDICTION SYSTEM")
print("====================================")
from pathlib import Path
import pandas as pd
data_file = Path(__file__).with_name("food_waste.csv.txt")
data = pd.read_csv(data_file)
print(data)
# Basic statistics
print("\nBasic Statistics:")
print(data.describe())

# Average food waste
average_waste = data["food_wasted_kg"].mean()

print("\nAverage Food Waste:", average_waste, "kg")
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Select input and output
X = data[["food_prepared_kg", "people_served", "temperature_c"]]
y = data["food_wasted_kg"]

# Split the data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create the model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)
import joblib
joblib.dump(model, "food_waste_model.pkl")
print("Model saved successfully!")
print("\nMachine Learning model trained successfully!")
# Make a prediction
prediction = model.predict([[60, 50, 29]])

print("\nPredicted Food Waste:", prediction[0], "kg")
from sklearn.metrics import mean_absolute_error, r2_score

# Predict test data
y_pred = model.predict(X_test)

# Calculate accuracy metrics
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\nMean Absolute Error:", mae)
print("R2 Score:", r2)
# User input for prediction
food_prepared = float(input("\nEnter food prepared (kg): "))
people_served = int(input("Enter number of people served: "))
temperature = float(input("Enter temperature (°C): "))

# Predict food waste
user_prediction = model.predict([[food_prepared, people_served, temperature]])

print("Predicted Food Waste:", round(user_prediction[0], 2), "kg")
import matplotlib.pyplot as plt

plt.scatter(data["food_prepared_kg"], data["food_wasted_kg"])
plt.xlabel("Food Prepared (kg)")
plt.ylabel("Food Wasted (kg)")
plt.title("Food Prepared vs Food Wasted")
plt.show()
# People Served vs Food Wasted
plt.scatter(data["people_served"], data["food_wasted_kg"])
plt.xlabel("People Served")
plt.ylabel("Food Wasted (kg)")
plt.title("People Served vs Food Wasted")
plt.show()
if user_prediction[0] > 10:
    print("⚠️ High food waste predicted. Consider reducing food preparation.")
else:
    print("✅ Food waste is within an acceptable range.")
    from sklearn.metrics import mean_absolute_error, r2_score

# Predict on test data
y_pred = model.predict(X_test)

# Evaluation
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"MAE: {mae:.4f}")
print(f"R²: {r2:.4f}")