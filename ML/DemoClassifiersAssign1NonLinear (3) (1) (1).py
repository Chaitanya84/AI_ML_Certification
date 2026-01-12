# ======================================================
# CLASSIFICATION ON NON-LINEAR DATASET
# ======================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.preprocessing import StandardScaler


def plot_decision_boundary(model, X, y, title):
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.linspace(x_min, x_max, 400),
                         np.linspace(y_min, y_max, 400))
    grid = np.c_[xx.ravel(), yy.ravel()]
    pred = model.predict(grid).reshape(xx.shape)

    plt.figure(figsize=(6,5))
    plt.contourf(xx, yy, pred, alpha=0.3, cmap='bwr')
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap='bwr', edgecolors='k', s=50)
    plt.title(title)
    plt.xlabel("Feature_1")
    plt.ylabel("Feature_2")
    plt.savefig("nonlinear_dataset_scatter.png", dpi=300, bbox_inches='tight')
    plt.show()


print("\n=== NON-LINEAR DATASET CLASSIFICATION ===\n")

df = pd.read_csv("nonlinear_dataset.csv")
X = df[["Feature_1", "Feature_2"]].values
y = df["Target"].values

plt.figure(figsize=(6,5))
plt.scatter(X[:, 0], X[:, 1], c=y, cmap='bwr', edgecolors='k')
plt.title("Non-Linear Dataset Scatter Plot")
plt.show()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

models = [
    ("Logistic Regression", LogisticRegression(), True),
    ("Decision Tree (depth=3)", DecisionTreeClassifier(max_depth=3), False),
    ("SVM (Linear Kernel)", SVC(kernel='linear'), True),
    ("SVM (RBF Kernel)", SVC(kernel='rbf'), True)
]

for name, model, scale in models:
    model.fit(X_train_scaled if scale else X_train, y_train)
    y_pred = model.predict(X_test_scaled if scale else X_test)

    print("\n---", name, "---")
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
    print(classification_report(y_test, y_pred))

    plot_decision_boundary(model, X_train_scaled if scale else X_train, y_train,
                           name + " Decision Boundary")
