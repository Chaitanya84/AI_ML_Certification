# ===========================================
# Linear Regression on House Price Dataset
# ===========================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# ---------------------------
# 1. Create the dataset
# ---------------------------
houses = pd.DataFrame({
    'Square_Footage': [1500, 1600, 1800, 1900, 2100, 2200, 2500, 2600, 2800, 2900],
    'Actual_Price': [200.0, 214.0, 250.0, 258.9, 300.0, 320.2, 350.0, 352.2, 400.0, 408.1]
})

# ---------------------------
# 2. Prepare data for model
# ---------------------------
X = houses[['Square_Footage']]     # Predictor
y = houses['Actual_Price']         # Response

# ---------------------------
# 3. Fit linear regression
# ---------------------------
model = LinearRegression()
model.fit(X, y)

# Get model parameters
intercept = model.intercept_
slope = model.coef_[0]

print("===== Simple Linear Regression Model =====")
print("Intercept (b0): %.3f" % intercept)
print("Slope (b1): %.3f" % slope)

# ---------------------------
# 4. Predictions
# ---------------------------
houses['Predicted_Price'] = model.predict(X)
houses['Residuals'] = houses['Actual_Price'] - houses['Predicted_Price']

# ---------------------------
# 5. Compute error metrics
# ---------------------------
# Residual Sum of Squares (RSS)
RSS = np.sum((houses['Residuals'])**2)

# Total Sum of Squares (TSS)
TSS = np.sum((houses['Actual_Price'] - np.mean(houses['Actual_Price']))**2)

# Explained Sum of Squares (ESS)
ESS = TSS - RSS

# Mean Squared Error (MSE)
n = len(houses)
p = 2  # parameters (intercept + slope)
MSE = RSS / n
RSE = np.sqrt(RSS / (n - p))

# R-squared
R2 = 1 - (RSS / TSS)

# ---------------------------
# 6. Display results
# ---------------------------
print("\n===== Regression Model Performance =====")
print("RSS (Residual Sum of Squares): %.3f" % RSS)
print("TSS (Total Sum of Squares): %.3f" % TSS)
print("ESS (Explained Sum of Squares): %.3f" % ESS)
print("MSE (Mean Squared Error): %.3f" % MSE)
print("RSE (Residual Standard Error): %.3f" % RSE)
print("R2 (Coefficient of Determination): %.3f" % R2)

# ---------------------------
# 7. Display data with predictions
# ---------------------------
print("\nSample of Predicted vs Actual:")
print(houses[['Square_Footage', 'Actual_Price', 'Predicted_Price', 'Residuals']].head())

# ---------------------------
# 8. Visualization: Actual vs Predicted Line
# ---------------------------
plt.figure(figsize=(7,5))
plt.scatter(houses['Square_Footage'], houses['Actual_Price'], color='blue', label='Actual Data')
plt.plot(houses['Square_Footage'], houses['Predicted_Price'], color='red', linewidth=2, label='Regression Line')

# Labels and formatting
plt.xlabel("Square Footage")
plt.ylabel("House Price")
plt.title("Linear Regression: Actual vs Predicted Prices")
plt.legend()
plt.grid(True)

# Display the plot
plt.show()