# ============================================
# CLASSIFICATION DEMO USING CSV FILE PATH
# Logistic Regression vs Decision Tree vs SVM
# ============================================

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# ============================================================
# Step 1: Specify CSV File Path
# ============================================================

# ✅ EDIT THIS PATH to match where your dataset is saved
csv_path = r"D:\Drive2\Data\classification_dataset.csv"

# Check if file exists
if not os.path.exists(csv_path):
    raise FileNotFoundError(
        "❌ Dataset not found at: %s\nPlease check the path or ensure the file exists." % csv_path
    )

# ============================================================
# Step 2: Load Dataset from CSV
# ============================================================

print("Loading dataset from: %s\n" % csv_path)
df = pd.read_csv(csv_path)

print("=== Dataset Description ===")
print(df.describe(), "\n")

print("=== First Five Samples ===")
print(df.head(), "\n")

# Separate features and target
X = df[["Feature_1", "Feature_2"]].values
y = df["Target"].values

# ============================================================
# Step 3: Visualize the Dataset Before Classification
# ============================================================

plt.figure(figsize=(7,6))
plt.scatter(X[:, 0], X[:, 1], c=y, cmap='bwr', edgecolors='k', s=50)
plt.title("Dataset Visualization: Two-Class Synthetic Data")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig("dataset_visualization.png", dpi=300)
print("Saved: dataset_visualization.png")
plt.show()
plt.close()
print()

# ============================================================
# Step 4: Split Data into Train and Test Sets
# ============================================================

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)
print("Training samples: %d, Testing samples: %d\n" % (len(X_train), len(X_test)))

# ============================================================
# Helper Function for Plotting Decision Boundaries
# ============================================================

def plot_decision_boundary(model, X, y, title, filename):
    h = 0.02
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                         np.arange(y_min, y_max, h))
    Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)

    plt.figure(figsize=(6,5))
    plt.contourf(xx, yy, Z, cmap='bwr', alpha=0.3)
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap='bwr', edgecolors='k')
    plt.title(title)
    plt.xlabel("Feature 1")
    plt.ylabel("Feature 2")
    plt.tight_layout()
    plt.savefig(filename, dpi=300)
    plt.close()
    print("Saved: %s" % filename)

# ============================================================
# Step 5: Logistic Regression
# ============================================================

print("==== Logistic Regression ====")
lr = LogisticRegression()
lr.fit(X_train, y_train)
y_pred_lr = lr.predict(X_test)
acc_lr = accuracy_score(y_test, y_pred_lr)
print("Accuracy: %.3f" % acc_lr)
print(confusion_matrix(y_test, y_pred_lr))
print(classification_report(y_test, y_pred_lr))
plot_decision_boundary(lr, X, y, "Logistic Regression Decision Boundary", "logistic_boundary.png")

# ============================================================
# Step 6: Decision Tree
# ============================================================

print("\n==== Decision Tree ====")
dt = DecisionTreeClassifier(max_depth=3, random_state=42)
dt.fit(X_train, y_train)
y_pred_dt = dt.predict(X_test)
acc_dt = accuracy_score(y_test, y_pred_dt)
print("Accuracy: %.3f" % acc_dt)
print(confusion_matrix(y_test, y_pred_dt))
print(classification_report(y_test, y_pred_dt))
plot_decision_boundary(dt, X, y, "Decision Tree (max_depth=3) Decision Regions", "decisiontree_boundary.png")

# ============================================================
# Step 7: Support Vector Machine
# ============================================================

print("\n==== Support Vector Machine (Linear Kernel) ====")
svm = SVC(kernel='linear', C=1.0, random_state=42)
svm.fit(X_train, y_train)
y_pred_svm = svm.predict(X_test)
acc_svm = accuracy_score(y_test, y_pred_svm)
print("Accuracy: %.3f" % acc_svm)
print(confusion_matrix(y_test, y_pred_svm))
print(classification_report(y_test, y_pred_svm))
plot_decision_boundary(svm, X, y, "SVM (Linear Kernel) Decision Boundary", "svm_boundary.png")

# ============================================================
# Step 8: Model Performance Summary
# ============================================================

print("\n===== Model Accuracy Comparison =====")
print("Logistic Regression : %.3f" % acc_lr)
print("Decision Tree        : %.3f" % acc_dt)
print("SVM (Linear Kernel)  : %.3f" % acc_svm)

# Identify best model
models = [("Logistic Regression", acc_lr), ("Decision Tree", acc_dt), ("SVM", acc_svm)]
best_model = max(models, key=lambda x: x[1])
print("\n✅ Best Performing Model: %s with accuracy = %.3f" % (best_model[0], best_model[1]))
print("===========================================")
