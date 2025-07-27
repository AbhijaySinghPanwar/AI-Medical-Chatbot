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
    git clone [https://github.com/YOUR_USERNAME/medical-chatbot-app.git](https://github.com/YOUR_USERNAME/medical-chatbot-app.git)
    cd medical-chatbot-app
    ```
    If you're setting it up from scratch, ensure you have `app.py`, `README.md`, and `.gitignore` in your project directory.

2.  **Create a Virtual Environment (Recommended):**
    ```bash
    python -m venv .venv
    ```

3.  **Activate the Virtual Environment:**
    * **Windows:**
        ```bash
        .venv\Scripts\activate
        ```
    * **macOS/Linux:**
        ```bash
        source .venv/bin/activate
        ```
    (You should see `(.venv)` at the beginning of your terminal prompt.)

4.  **Install Dependencies:**
    ```bash
    pip install streamlit requests
    ```

5.  **Set up Gemini API Key:**
    The application uses the Gemini API. For local development, you need to provide your API key.
    * Go to [Google AI Studio](https://aistudio.google.com/app/apikey) to generate an API key.
    * Set it as an environment variable before running the app.
        * **Windows (for current session):**
            ```bash
            $env:GEMINI_API_KEY="YOUR_API_KEY_HERE"
            ```
        * **macOS/Linux (for current session):**
            ```bash
            export GEMINI_API_KEY="YOUR_API_KEY_HERE"
            ```
        * **Alternatively (for testing only, not recommended for production):** You can temporarily hardcode your API key in `app.py` by changing `API_KEY = os.getenv("GEMINI_API_KEY", "")` to `API_KEY = "YOUR_API_KEY_HERE"`. **Remember to remove this before pushing to a public repository!**

## How to Run the Chatbot

1.  **Ensure your virtual environment is active** and all dependencies are installed.
2.  **Run the Streamlit application:**
    ```bash
    streamlit run app.py
    ```
3.  Your web browser will automatically open to `http://localhost:8501` (or a similar address) where you can interact with the chatbot.

## Project Structure