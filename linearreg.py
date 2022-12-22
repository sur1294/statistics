import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Sample data
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

# Fit the model
slope, intercept, r_value, p_value, std_err = linregress(x, y)

# Predict values for new data
y_pred = intercept + slope * np.array(x)

# Plot the actual and predicted values
plt.plot(x, y, 'bo', label='Actual')
plt.plot(x, y_pred, 'r', label='Predicted')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()
