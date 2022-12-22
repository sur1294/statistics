import numpy as np
from sklearn.linear_model import LogisticRegression

# Sample data
X = [[1, 2], [2, 3], [3, 1], [4, 5], [5, 6]]
y = [0, 1, 0, 1, 0]

# Fit the model
model = LogisticRegression()
model.fit(X, y)

# Predict values for new data
X_new = [[6, 7], [7, 8], [8, 6],[9,2]]
y_pred = model.predict(X_new)

print(y_pred) 

