


### 2\.`README.md`

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
