from sklearn import tree

# Training Data
X = [
    [25, 30000],
    [35, 60000],
    [45, 80000],
    [20, 20000],
    [30, 50000]
]

# Labels
y = ["No", "Yes", "Yes", "No", "Yes"]

# Create Model
model = tree.DecisionTreeClassifier()

# Train Model
model.fit(X, y)

# Prediction
prediction = model.predict([[28, 40000]])

print("Prediction:", prediction[0])