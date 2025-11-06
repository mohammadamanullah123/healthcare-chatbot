# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
# from rasa_sdk import Action
# from rasa_sdk.events import SlotSet
# import pickle
# import pandas as pd

# class ActionPredictDisease(Action):
#     def name(self):
#         return "action_predict_disease"

#     def run(self, dispatcher, tracker, domain):
#         symptoms = tracker.get_slot("symptoms")
#         if not symptoms:
#             dispatcher.utter_message(text="Please provide your symptoms.")
#             return []

#         # Load model and encoder
#         with open("disease_model.pkl", "rb") as f:
#             model = pickle.load(f)
#         with open("label_encoder.pkl", "rb") as f:
#             le = pickle.load(f)

#         # Dummy symptom processing (modify based on your dataset)
#         symptom_list = symptoms.lower().split(", ")
#         input_data = [0] * 3  # Example: [Fever, Cough, Fatigue]
#         if "fever" in symptom_list:
#             input_data[0] = 1
#         if "cough" in symptom_list:
#             input_data[1] = 1
#         if "fatigue" in symptom_list:
#             input_data[2] = 1
#         input_df = pd.DataFrame([input_data], columns=["Fever", "Cough", "Fatigue"])

#         # Predict
#         prediction = model.predict(input_df)[0]
#         disease = le.inverse_transform([prediction])[0]

#         # Respond
#         dispatcher.utter_message(text=f"Based on your symptoms, you might have {disease}. Please consult a doctor.")
#         return [SlotSet("symptoms", symptoms)]
import pandas as pd
import os
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionPredictDisease(Action):
    def name(self):
        return "action_predict_disease"

    def run(self, dispatcher, tracker, domain):
        # Get symptoms from the slot
        symptoms = tracker.get_slot("symptom") or []
        if not symptoms:
            dispatcher.utter_message(text="No symptoms provided. Please tell me your symptoms (e.g., fever, cough).")
            return []

        try:
            # Load dataset
            dataset_path = os.path.join(os.path.dirname(__file__), "dataset.csv")
            if not os.path.exists(dataset_path):
                dispatcher.utter_message(text=f"Error: Dataset file not found at {dataset_path}")
                return []
            dataset = pd.read_csv(dataset_path)

            # Clean symptom columns (remove NaN and convert to list)
            symptom_columns = [f"Symptom_{i}" for i in range(1, 18)]
            matched_diseases = set()
            for symptom in symptoms:
                symptom = symptom.strip().lower()
                # Check each symptom column for matches
                for col in symptom_columns:
                    matches = dataset[dataset[col].str.lower().str.contains(symptom, na=False)]
                    if not matches.empty:
                        matched_diseases.update(matches["Disease"].tolist())

            if matched_diseases:
                disease_list = ", ".join(matched_diseases)
                dispatcher.utter_message(text=f"Based on your symptoms ({', '.join(symptoms)}), you might have: {disease_list}. Please consult a doctor for a proper diagnosis.")
            else:
                dispatcher.utter_message(text=f"No diseases found matching symptoms: {', '.join(symptoms)}. Please provide more details or consult a doctor.")
        except Exception as e:
            dispatcher.utter_message(text=f"Error processing dataset: {str(e)}")
        return []
