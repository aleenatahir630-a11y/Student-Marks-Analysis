from sklearn.tree import DecisionTreeClassifier

# Training Data
X = [
    [150, 7],
    [170, 8],
    [140, 6],
    [300, 12],
    [320, 13],
    [280, 11],
    [120, 5],
    [130, 5]
]

# Labels (Multiple Classes)
y = [
    "Apple",
    "Apple",
    "Apple",
    "Watermelon",
    "Watermelon",
    "Watermelon",
    "Orange",
    "Orange"
]

# Create Model
model = DecisionTreeClassifier()

# Train Model
model.fit(X, y)

# Prediction
prediction = model.predict([[160, 7]])

print("Predicted Fruit:", prediction[0])