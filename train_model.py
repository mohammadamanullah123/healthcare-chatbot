import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import pickle

# Load dataset
data = pd.read_csv("dataset.csv")

# Encode all symptoms and disease
label_encoders = {}
for column in data.columns:
    if data[column].dtype == 'object':
        le = LabelEncoder()
        # Handle missing values (fill with empty string)
        data[column] = data[column].fillna('')
        data[column] = le.fit_transform(data[column])
        label_encoders[column] = le

# Split features and target
X = data.drop("Disease", axis=1)  # Symptoms
y = data["Disease"]  # Encoded

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save model
with open("disease_model.pkl", "wb") as f:
    pickle.dump(model, f)

# Save all encoders
with open("label_encoders.pkl", "wb") as f:
    pickle.dump(label_encoders, f)

# Test accuracy
accuracy = model.score(X_test, y_test)
print(f"Model Accuracy: {accuracy}")
