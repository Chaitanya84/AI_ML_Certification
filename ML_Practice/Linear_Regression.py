import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('train.csv') # Ensure 'train.csv' is in the same directory  
X = data[['x']]
y = data['y'] 
# Split the data into training and validation sets
#X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)
# Create and train the model
Pred_data = pd.read_csv('test.csv') # Ensure 'test.csv' is in the same directory
X_val = Pred_data[['x']]
y_val = Pred_data['y']
model = LinearRegression()
model.fit(X, y)
# Make predictions
y_pred = model.predict(X_val)
#Append predicted y_pred values to test.csv

pd.DataFrame(y_pred, columns=['Predicted_y']).to_csv('predictions.csv', index=False)
# Evaluate the model
mse = mean_squared_error(y_val, y_pred)
r2 = r2_score(y_val, y_pred)
print(f'Mean Squared Error: {mse}')
print(f'R^2 Score: {r2}')
# Plot the results
plt.scatter(X_val, y_val, color='blue', label='Actual')
plt.scatter(X_val, y_pred, color='red', label='Predicted')
plt.xlabel('X')
plt.ylabel('y')
plt.title('Linear Regression: Actual vs Predicted')
plt.legend()
plt.show(block=False)
plt.pause(20)  # Display the plot for 5 seconds
plt.close()

#plot the difference of column y of test.csv and predicted y_pred values
plt.scatter(X_val, y_val - y_pred, color='green', label='Difference (Actual - Predicted)')
plt.xlabel('X')
plt.ylabel('Difference')
plt.title('Difference between Actual and Predicted Values')
plt.legend()
plt.show(block=False)
plt.pause(20)  # Display the plot for 5 seconds
plt.close()

#plot the actual x vs y values of train.csv and superimpose the x of test vs predicted y_pred values
plt.scatter(X, y, color='blue', label='Train Data (Actual)')
plt.scatter(X_val, y_pred, color='red', label='Test Data (Predicted)')
plt.xlabel('X')
plt.ylabel('y')
plt.title('Train Data vs Test Data Predictions')
plt.legend()
plt.show(block=False)
plt.pause(20)  # Display the plot for 5 seconds
plt.close()