# train_model.py

import joblib
from sklearn.ensemble import RandomForestClassifier
import numpy as np

# Dummy training data
# Features: N, P, K, temperature, humidity
X = np.array([
    [10, 5, 8, 27.5, 80],
    [20, 15, 10, 29.0, 70],
    [30, 25, 20, 31.5, 60],
    [15, 10, 12, 28.5, 75],
    [12, 7, 9, 27.0, 78],
    [25, 20, 18, 30.5, 65],
    [14, 9, 10, 28.0, 72]
])

# Labels: 1 = fertile, 0 = not fertile
y = [1, 1, 0, 1, 1, 0, 1]

# Create and train the model
model = RandomForestClassifier()
model.fit(X, y)

# Save the model to a file
joblib.dump(model, "model.pkl")

print("✅ Model trained and saved as model.pkl")
