import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

df = pd.read_csv("housing.csv")

print(df.head())
print(df.shape)
print(df.columns)
print(df.isnull().sum())
print(df.describe())

X = df[['area', 'bedrooms', 'bathrooms']]
y = df['price']

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

print("\nTraining Samples :", len(X_train))
print("Testing Samples  :", len(X_test))

model = LinearRegression()
model.fit(X_train, y_train)

print("\nModel Trained Successfully!")

y_pred = model.predict(X_test)

print("\n==============================")
print("MODEL PERFORMANCE")
print("==============================")

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print("Mean Absolute Error :", mae)
print("Mean Squared Error  :", mse)
print("Root Mean Squared Error :", rmse)
print("R² Score :", r2)

print("\n==============================")
print("MODEL PARAMETERS")
print("==============================")

print("\nIntercept")
print(model.intercept_)

print("\nFeature Coefficients")

coefficients = pd.DataFrame({
    "Feature": X.columns,
    "Coefficient": model.coef_
})

print(coefficients)

comparison = pd.DataFrame({
    "Actual Price": y_test.values,
    "Predicted Price": y_pred
})

print("\n==============================")
print("ACTUAL vs PREDICTED")
print("==============================")

print(comparison.head(10))

comparison.to_csv("House_Price_Predictions.csv", index=False)

print("\nPrediction file saved successfully!")

print("\n==============================")
print("HOUSE PRICE PREDICTION")
print("==============================")

area = float(input("Enter Area (sq.ft): "))
bedrooms = int(input("Enter Number of Bedrooms: "))
bathrooms = int(input("Enter Number of Bathrooms: "))

new_house = pd.DataFrame({
    "area": [area],
    "bedrooms": [bedrooms],
    "bathrooms": [bathrooms]
})

prediction = model.predict(new_house)

print("\nEstimated House Price = ₹ {:.2f}".format(prediction[0]))

plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_pred, color="blue")
plt.plot(
    [y_test.min(), y_test.max()],
    [y_test.min(), y_test.max()],
    color="red",
    linewidth=2
)
plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")
plt.title("Actual vs Predicted House Prices")
plt.grid(True)
plt.show()

plt.figure(figsize=(6, 4))
plt.bar(X.columns, model.coef_)
plt.title("Feature Importance")
plt.xlabel("Features")
plt.ylabel("Coefficient")
plt.grid(axis='y')
plt.show()

errors = y_test - y_pred

plt.figure(figsize=(8, 5))
plt.hist(errors, bins=25, edgecolor='black')
plt.title("Prediction Error Distribution")
plt.xlabel("Prediction Error")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()

print("\nTask Completed Successfully!")