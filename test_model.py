import pandas as pd
import pickle

# Load model and label encoder
with open("disease_model.pkl", "rb") as f:
    model = pickle.load(f)
with open("label_encoder.pkl", "rb") as f:
    le = pickle.load(f)

# Load the original dataset just to get correct column names
data = pd.read_csv("dataset.csv")
symptom_columns = data.drop("Disease", axis=1).columns.tolist()

# Select symptoms you want to test (must match column names exactly)
# Use lowercase or correct spellings, based on your CSV headers
input_symptoms = ["Fever", "Fatigue", "Cough"]  # Change symptoms here

# Create input vector: 1 if symptom present, else 0
input_vector = [1 if col in input_symptoms else 0 for col in symptom_columns]

# Create DataFrame for prediction
input_data = pd.DataFrame([input_vector], columns=symptom_columns)

# Predict
prediction = model.predict(input_data)
disease = le.inverse_transform(prediction)[0]

print(f"Predicted Disease: {disease}")

