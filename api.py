from flask import Flask, request, jsonify
import pickle
import pandas as pd
import requests

app = Flask(__name__)

# Load model and encoder
with open("disease_model.pkl", "rb") as f:
    model = pickle.load(f)
with open("label_encoder.pkl", "rb") as f:
    le = pickle.load(f)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    symptoms = data.get("symptoms", "")
    if not symptoms:
        return jsonify({"error": "No symptoms provided"}), 400

    # Process symptoms (modify based on dataset)
    symptom_list = symptoms.lower().split(", ")
    input_data = [0] * 3  # Example: [Fever, Cough, Fatigue]
    if "fever" in symptom_list:
        input_data[0] = 1
    if "cough" in symptom_list:
        input_data[1] = 1
    if "fatigue" in symptom_list:
        input_data[2] = 1
    input_df = pd.DataFrame([input_data], columns=["Fever", "Cough", "Fatigue"])

    # Predict
    prediction = model.predict(input_df)[0]
    disease = le.inverse_transform([prediction])[0]
    return jsonify({"disease": disease})

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    message = data.get("message", "")
    if not message:
        return jsonify({"error": "No message provided"}), 400

    # Call Rasa API
    response = requests.post("http://localhost:5005/webhooks/rest/webhook",
                            json={"sender": "user", "message": message})
    return jsonify(response.json())

if __name__ == "__main__":
    app.run(debug=True, port=5000)