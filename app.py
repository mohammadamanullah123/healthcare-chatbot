import streamlit as st
import requests

st.title("AI Healthcare Chatbot")
st.write("Enter your symptoms (e.g., fever, cough, fatigue):")
user_input = st.text_input("Symptoms")
if st.button("Submit"):
    if user_input:
        # Call Rasa API
        try:
            response = requests.post("http://localhost:5005/webhooks/rest/webhook",
                                    json={"sender": "user", "message": user_input})
            for msg in response.json():
                st.write(f"Bot: {msg['text']}")
        except Exception as e:
            st.error(f"Error connecting to chatbot: {e}")
    else:
        st.warning("Please enter symptoms.")