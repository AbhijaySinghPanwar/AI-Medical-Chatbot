Okay, let's update your Streamlit Medical Chatbot project to use an environment variable for the API key, which is a much safer and recommended practice.

We'll modify the `app.py` file and the `README.md` file.

-----

### 1\. Modified `app.py` (Main Python Application Code)

I've added `import os` and changed how the `API_KEY` is retrieved.

```python
import streamlit as st
import requests
import json
import os # Import the os module to access environment variables

# --- Configuration ---
# The API key will be provided by the environment.
# It's recommended to set this as an environment variable (e.g., GEMINI_API_KEY).
# For local testing, you can temporarily hardcode it, but remove before committing to public repo.
API_KEY = os.getenv("GEMINI_API_KEY", "") # Reads API key from environment variable, default to empty string if not found
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
    if not API_KEY:
        st.error("Gemini API Key not set. Please set the GEMINI_API_KEY environment variable.")
        return "Error: API key is missing. Please configure it."

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
```

-----

### 2\. Modified `README.md`

I've updated the "Set up Gemini API Key" section to provide clear instructions for setting the environment variable.

````markdown
# Medical Chatbot for Symptom Analysis (Streamlit & Gemini API)

## Project Description
This project implements a simple, interactive medical chatbot designed to assist users in identifying the most appropriate medical department or specialist based on their described symptoms. Built with Streamlit for the user interface and powered by the Google Gemini API for natural language understanding and symptom analysis, this chatbot aims to guide users to the right healthcare professional, potentially reducing misdirected appointments.

**Important Note:** This chatbot is for informational purposes only and **does not provide medical advice, diagnoses, or treatment**. Always consult a qualified healthcare professional for medical concerns.

## Features
* **Symptom Input:** Users can describe their symptoms in natural language.
* **Department Recommendation:** The chatbot recommends a relevant medical department (e.g., Cardiology, Dermatology, General Physician).
* **Interactive Chat Interface:** A clean and responsive chat interface built with Streamlit.
* **AI-Powered Reasoning:** Leverages the Gemini API for intelligent symptom interpretation and recommendations.

## Technologies Used
* **Python:** The core programming language.
* **Streamlit:** For building the interactive web user interface.
* **Google Gemini API:** For Large Language Model (LLM) capabilities, simulating backend reasoning for symptom analysis.
* **`requests` library:** For making HTTP requests to the Gemini API.

## Setup and Installation

### Prerequisites
* Python 3.8 or higher
* `pip` (Python package installer)

### Steps
1.  **Clone the Repository (or create the files):**
    If you're cloning this repository:
    ```bash
    git clone [https://github.com/AbhijaySinghPanwar/AI-Medical-Chatbot.git](https://github.com/AbhijaySinghPanwar/AI-Medical-Chatbot.git)
    cd medical-chatbot-app
    ```
    If you're setting it up from scratch, ensure you have `app.py`, `README.md`, and `.gitignore` in your project directory.

2.  **Create a Virtual Environment (Recommended):**
    ```bash
    python -m venv .venv
    ```

3.  **Activate the Virtual Environment:**
    * **Windows (Command Prompt/PowerShell):**
        ```bash
        .venv\Scripts\activate
        ```
    * **macOS/Linux (Bash/Zsh):**
        ```bash
        source .venv/bin/activate
        ```
    (You should see `(.venv)` at the beginning of your terminal prompt.)

4.  **Install Dependencies:**
    ```bash
    pip install streamlit requests
    ```

5.  **Set up Gemini API Key (Crucial for Functionality):**
    The application requires a Google Gemini API key to function.
    * Go to [Google AI Studio](https://aistudio.google.com/app/apikey) to generate your API key.
    * **Set this key as an environment variable named `GEMINI_API_KEY`** before running the application. This is the recommended and most secure way to handle API keys.

    * **For Windows (Command Prompt/PowerShell - for current session):**
        ```powershell
        $env:GEMINI_API_KEY="YOUR_API_KEY_HERE"
        # Or in Command Prompt: set GEMINI_API_KEY=YOUR_API_KEY_HERE
        ```
        *(Replace `YOUR_API_KEY_HERE` with your actual key)*

    * **For macOS/Linux (Bash/Zsh - for current session):**
        ```bash
        export GEMINI_API_KEY="YOUR_API_KEY_HERE"
        ```
        *(Replace `YOUR_API_KEY_HERE` with your actual key)*

    * **Important:** Setting environment variables this way makes them available only for the current terminal session. If you close the terminal, you'll need to set it again. For permanent setting, you'd add it to your system's environment variables (Windows) or shell profile file (e.g., `.bashrc`, `.zshrc` on Linux/macOS).

## How to Run the Chatbot

1.  **Ensure your virtual environment is active** and all dependencies are installed.
2.  **Ensure the `GEMINI_API_KEY` environment variable is set** in your current terminal session.
3.  **Run the Streamlit application:**
    ```bash
    streamlit run app.py
    ```
4.  Your web browser will automatically open to `http://localhost:8501` (or a similar address) where you can interact with the chatbot.

## Project Structure
````

.
├── .venv/                  \# Python virtual environment (ignored by Git)
├── app.py                  \# Main Streamlit application code
├── .gitignore              \# Specifies intentionally untracked files to ignore
└── README.md               \# Project description and setup instructions

```

## Contributing
Feel free to fork this repository, open issues, or submit pull requests.

## License
[Optional: Specify your license here, e.g., MIT License]
```