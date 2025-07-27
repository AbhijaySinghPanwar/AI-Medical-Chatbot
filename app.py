import streamlit as st
import requests
import json
import os

# --- Configuration ---
# The API key will be provided by the environment in Canvas.
# If running locally, you might need to set this as an environment variable
# or replace with your actual API key for testing.
# For security, never hardcode API keys in production code.
API_KEY = "AIzaSyDFv4JemfnY0Lpqail1pjYwAHSs5AASx1o" # Or set your key here for local testing: "YOUR_GEMINI_API_KEY"
GEMINI_API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={API_KEY}"

# --- Streamlit App Setup ---
st.set_page_config(page_title="Medical Chatbot", page_icon="⚕️")

st.title("⚕️ Medical Chatbot for Symptom Analysis")
st.markdown("Describe your symptoms, and I'll recommend a medical department. **I do not provide medical advice or diagnoses.**")

# --- Initialize Chat History in Session State ---
# Streamlit's session_state is crucial for maintaining state across reruns.
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- Function to Call Gemini API ---
def get_gemini_response(user_message):
    """
    Sends the user's symptoms to the Gemini API and gets a department recommendation.
    """
    prompt = f"""
    You are a medical symptom analysis chatbot. Your goal is to recommend the most appropriate medical department or specialist based on the symptoms provided by the user.
    Do NOT provide medical advice, diagnoses, or treatment. Only recommend a department.
    If symptoms are vague or insufficient, ask for more details or suggest a general physician.

    Here are some examples of symptom-to-department mappings:
    - Headache, fever, body aches, cough: General Physician
    - Skin rash, itching, acne: Dermatology
    - Chest pain, shortness of breath, palpitations: Cardiology
    - Joint pain, swelling, stiffness: Orthopedics or Rheumatology
    - Eye redness, blurred vision, eye pain: Ophthalmology
    - Earache, sore throat, difficulty swallowing: ENT (Ear, Nose, Throat)
    - Abdominal pain, nausea, vomiting, diarrhea: Gastroenterology
    - Frequent urination, burning sensation during urination: Urology
    - Anxiety, persistent sadness, difficulty concentrating: Psychiatry or Psychology

    User symptoms: "{user_message}"
    Based on these symptoms, which medical department should the user consult?
    Please respond concisely with only the department name or a request for more information.
    """

    headers = {
        'Content-Type': 'application/json'
    }
    payload = {
        "contents": [
            {
                "role": "user",
                "parts": [
                    {"text": prompt}
                ]
            }
        ]
    }

    try:
        response = requests.post(GEMINI_API_URL, headers=headers, data=json.dumps(payload))
        response.raise_for_status() # Raise an exception for HTTP errors (4xx or 5xx)
        result = response.json()

        if result.get("candidates") and len(result["candidates"]) > 0 and \
           result["candidates"][0].get("content") and \
           result["candidates"][0]["content"].get("parts") and \
           len(result["candidates"][0]["content"]["parts"]) > 0:
            return result["candidates"][0]["content"]["parts"][0]["text"]
        else:
            st.error("Error: Unexpected API response structure.")
            st.json(result) # Display the full response for debugging
            return "I'm sorry, I couldn't process that. Please try again."
    except requests.exceptions.RequestException as e:
        st.error(f"Error communicating with Gemini API: {e}")
        return "Oops! Something went wrong. Please try again later."
    except json.JSONDecodeError as e:
        st.error(f"Error decoding API response: {e}")
        return "Oops! Something went wrong with the response format."

# --- Display Chat Messages ---
# Iterate through the messages in session_state and display them
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- Chat Input ---
if user_input := st.chat_input("Describe your symptoms..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": user_input})
    # Display user message immediately
    with st.chat_message("user"):
        st.markdown(user_input)

    # Get bot response and add to chat history
    with st.spinner("Thinking..."): # Show a spinner while waiting for API response
        bot_response = get_gemini_response(user_input)
    st.session_state.messages.append({"role": "assistant", "content": bot_response})

    # Display bot response
    with st.chat_message("assistant"):
        st.markdown(bot_response)

# Note: In a real-world scenario, you'd want to handle API key securely
# and potentially use a more robust logging mechanism.
