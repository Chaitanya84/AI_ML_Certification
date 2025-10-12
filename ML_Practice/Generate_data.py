import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Generate training data (100 points)
x_train = np.random.uniform(0, 100, 100)
noise_train = np.random.normal(0, 10, 100)
y_train = 3 * x_train + 7 + noise_train

train_df = pd.DataFrame({
    "x": x_train,
    "y": y_train
})

# Generate test data (20 points)
x_test = np.random.uniform(0, 100, 20)
noise_test = np.random.normal(0, 10, 20)
y_test = 3 * x_test + 7 + noise_test

test_df = pd.DataFrame({
    "x": x_test,
    "y": y_test
})

# Save as CSV files
train_df.to_csv("train.csv", index=False)
test_df.to_csv("test.csv", index=False)

print("Files 'train.csv' and 'test.csv' have been created.")
