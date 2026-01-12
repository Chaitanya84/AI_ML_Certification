# ============================================================
# Exploring the California Housing Dataset in Scikit-learn
# ============================================================

from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import cross_val_score, KFold
from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ------------------------------------------------------------
# 1. Load the dataset
# ------------------------------------------------------------
data = fetch_california_housing(as_frame=True)

# Check what’s inside the dataset
print("Dataset keys:\n", data.keys(), "\n")

# ------------------------------------------------------------
# 2. Explore basic metadata
# ------------------------------------------------------------
print("Feature Names:\n", data.feature_names, "\n")
print("Target Name:\n", data.target_names, "\n")

# Print the dataset description
print("Dataset Description:\n")
print(data.DESCR[:800], "...")   # Print first 800 chars for brevity

# ------------------------------------------------------------
# 3. Create a DataFrame combining predictors and target
# ------------------------------------------------------------
df = data.frame
print("\nFirst 5 rows of the dataset:")
print(df.head())

# ------------------------------------------------------------
# 4. Summary statistics
# ------------------------------------------------------------
print("\nStatistical Summary:")
print(df.describe())

# ------------------------------------------------------------
# 5. Correlation analysis
# ------------------------------------------------------------
corr = df.corr(numeric_only=True)
print("\nCorrelation with target (MedHouseVal):")
print(corr["MedHouseVal"].sort_values(ascending=False))

# ------------------------------------------------------------
# 6. Visualize a key relationship
# ------------------------------------------------------------
plt.figure(figsize=(6, 4))
plt.scatter(df["MedInc"], df["MedHouseVal"], alpha=0.5)
plt.xlabel("Median Income")
plt.ylabel("Median House Value")
plt.title("Income vs House Value in California Housing Data")
plt.show()

# ------------------------------------------------------------
# 7. Example: Cross-validation on Linear Regression
# ------------------------------------------------------------
X = df[data.feature_names]
y = df["MedHouseVal"]

model = LinearRegression()
kf = KFold(n_splits=5, shuffle=True, random_state=1)
scores = cross_val_score(model, X, y, cv=kf, scoring="r2")

print("\nCross Validation R² scores:", scores)
print("Average R²:", np.mean(scores))
