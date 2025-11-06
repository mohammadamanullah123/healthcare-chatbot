# 🤖 AI-Powered Healthcare Chatbot with Disease Prediction

# 🩺 1. Overview

This project is an intelligent healthcare assistant chatbot built using the Rasa framework and integrated with a machine learning model for disease prediction (e.g., heart disease).

It interacts conversationally with users, answers health-related questions, and can predict diseases based on user-provided medical parameters.
The project demonstrates the integration of NLP (Natural Language Processing) with AI-driven predictive analytics.

# ⚙️ 2. Installation & Setup
2.1 Install Dependencies

Before starting, ensure Python 3.8+ is installed. Then follow these steps:

sudo apt update  
sudo apt install -y python3 python3-pip  


Now install required packages:

pip install rasa scikit-learn pandas numpy


Optional (if using actions server):

pip install flask joblib

# 2.2 Create and Activate Virtual Environment

Recommended setup (for Ubuntu, Windows or macOS):

python3 -m venv .venv  
source .venv/bin/activate      # (Linux/macOS)
.venv\Scripts\activate         # (Windows)


Install all dependencies inside the environment:

pip install -r requirements.txt


(If you don’t have a requirements.txt, install the packages manually.)

# 2.3 Project Structure 🧩
AI-Healthcare-Chatbot/
│
├── actions.py                → Custom actions (includes disease prediction logic)
├── predict_disease.py        → Script to predict disease using ML model
├── domain.yml                → Intents, entities, slots, and responses
├── data/
│   ├── nlu.yml               → Training examples for intents
│   ├── stories.yml           → Conversation stories
│   └── rules.yml             → Conversation rules
├── models/                   → Trained Rasa models stored here
├── heart_disease_model.pkl   → Pretrained ML model for prediction
└── config.yml                → NLP pipeline and policies

# 🧠 3. Model Training
3.1 Train ML Model

Train a heart-disease prediction model using a dataset containing attributes like:
age, cholesterol, blood pressure, max heart rate, etc.

After training, export and save the model as:

heart_disease_model.pkl


This file will be loaded by actions.py whenever the chatbot performs disease prediction.

# 3.2 Train Rasa Chatbot

Use the Rasa CLI to train the chatbot:

rasa train


A trained model will be saved inside the models/ folder.

# 🚀 4. Running the Chatbot
# Step 1: Start the Action Server

Run your custom action server to enable disease prediction actions:

rasa run actions

# Step 2: Start the Chatbot

In another terminal, start the chatbot shell:

rasa shell


Once both are running, you can chat directly in the terminal or integrate it into a web interface.

# 💬 5. Example Interaction
User: Hi, I’m feeling chest pain and shortness of breath.
Bot: I’m sorry to hear that. Could you please provide your age, cholesterol level, and blood pressure?
User: Age 45, cholesterol 210, BP 140.
Bot: Based on your data, there is a moderate risk of heart disease. Please consult a doctor for further examination.

# 🛠️ 6. Customization
Add More Diseases 🧬

You can extend the chatbot to include additional models (e.g., diabetes, kidney disease).
Update the following files:
• actions.py – include new model loading and prediction logic
• domain.yml – add new intents and responses
• nlu.yml – train with more disease-related sentences

# 🎮 7. Usage Options
Command-Line Options

You can run Rasa commands as follows:

rasa train           → Train chatbot  
rasa shell           → Chat in terminal  
rasa run actions     → Start custom actions  
rasa interactive     → Interactive training mode

Example Combined Run
rasa run actions & rasa shell

# 🔍 8. Troubleshooting
Chatbot doesn’t respond 🤐

• Check that the action server is running.
• Verify that actions.py is correctly referenced in endpoints.yml.

Model not found ⚠️

• Make sure heart_disease_model.pkl exists in the correct folder.
• Re-train and save the model again if needed.

Error importing libraries 📦

• Reinstall dependencies using pip install -r requirements.txt.
• Check your Python environment with which python or python --version.

Prediction inaccurate 🤔

• Use more training data to improve your ML model.
• Normalize or scale input features before training.


# 🤝 10. Getting Help

If you face issues:
• Check the Rasa documentation (https://rasa.com/docs
)
• Search existing GitHub issues or create a new one
• Share your logs and model details when reporting problems

# ❤️ Thank You!

You’ve reached the end — now go build your own intelligent healthcare assistant!
Stay healthy and keep innovating! 🩺🤖
