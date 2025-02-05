# PyGemini Python Script

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This Python script leverages the Google Gemini API to generate well-structured text responses to user questions. It's designed to provide clear, organized, and readable answers by using system instructions to guide the Gemini model.

## Description

PyGemini takes a user's question as input and sends it to the Google Gemini API. By employing a system instruction that emphasizes structured output, the script encourages the Gemini model to generate responses that are well-formatted using elements like paragraphs, bullet points, numbered lists, and potentially headings. This results in answers that are easier to understand and digest.

## Prerequisites

Before you can run PyGemini, you need to ensure you have the following set up:

1.  **Google AI Studio API Key:** You will need a valid API key from Google AI Studio to access the Gemini API. You can obtain one by visiting [Google AI Studio](https://makersuite.google.com/).
2.  **Python 3.6 or higher:** Python must be installed on your system. You can download it from [python.org](https://www.python.org/).
3.  **`google-generativeai` library:** This Python library is required to interact with the Gemini API. You can install it using pip (Python's package installer):

    ```bash
    pip install google-generativeai
    ```

4.  **Set the `GEMINI_API_KEY` Environment Variable:** For security, the script retrieves your API key from an environment variable. You need to set this environment variable on your system.

    *   **On Linux/macOS:**
        Open your terminal and add the following line to your shell configuration file (e.g., `~/.bashrc`, `~/.zshrc`):
        ```bash
        export GEMINI_API_KEY="YOUR_ACTUAL_API_KEY_HERE"
        ```
        Replace `"YOUR_ACTUAL_API_KEY_HERE"` with your actual Gemini API key. Then, run `source ~/.bashrc` or `source ~/.zshrc` (depending on your shell) to apply the changes.

    *   **On Windows:**
        1.  Open the **Start Menu** and search for "environment variables".
        2.  Select "Edit the system environment variables".
        3.  Click the "Environment Variables..." button.
        4.  In the "System variables" or "User variables" section, click "New...".
        5.  Enter `GEMINI_API_KEY` as the "Variable name".
        6.  Enter your actual Gemini API key as the "Variable value".
        7.  Click "OK" on all dialogs to save the changes.
        8.  You may need to restart your terminal or command prompt for the environment variable to be recognized.

## How to Use PyGemini

Follow these steps to run the PyGemini script:

1.  **Clone or Download the Repository:**
    If you haven't already, clone this repository to your local machine using Git, or download the ZIP file and extract it.

2.  **Navigate to the Project Directory:**
    Open your terminal or command prompt and navigate to the `pygemini` directory where you saved the script files.

3.  **Install the `google-generativeai` library:**
    If you haven't already installed it, run:
    ```bash
    pip install google-generativeai
    ```

4.  **Set the `GEMINI_API_KEY` Environment Variable:**
    Make sure you have correctly set the `GEMINI_API_KEY` environment variable as described in the "Prerequisites" section.

5.  **Run the Python Script:**
    Execute the script using the command:
    ```bash
    python pygemini.py
    ```

6.  **Enter Your Question:**
    When prompted in the terminal, type your question and press Enter. For example:
    ```
    Ask your question: Explain the theory of relativity.
    ```

7.  **View the Structured Answer:**
    PyGemini will send your question to the Gemini API and then display the structured answer in the terminal, enclosed within delimiters:
    ```
    --- Structured Answer ---
    [Structured answer from Gemini API will appear here]
    --- End Answer ---
    ```

## Python Code (`pygemini.py`)

```python
import google.generativeai as genai
import os  # For environment variables

# --- Configuration ---
MODEL_NAME = 'gemini-pro'  # You can change this to 'gemini-pro-vision' or other models
# API Key should be set as an environment variable for security
API_KEY_ENV_VAR_NAME = "GEMINI_API_KEY"

def get_api_key():
    """
    Retrieves the Gemini API key from environment variables.

    Returns:
        str: The API key if found, otherwise None.
    """
    api_key = os.environ.get(API_KEY_ENV_VAR_NAME)
    if not api_key:
        print(f"Error: API key not found. Please set the '{API_KEY_ENV_VAR_NAME}' environment variable.")
        return None
    return api_key

def configure_gemini_api(api_key):
    """
    Configures the Google Gemini API with the provided API key.

    Args:
        api_key (str): The Gemini API key.
    """
    try:
        genai.configure(api_key=api_key)
        print("Gemini API configured successfully.")  # Feedback on successful configuration
    except Exception as e:
        print(f"Error configuring Gemini API: {e}")
        raise  # Re-raise the exception for handling in the main function

def get_structured_response(prompt, model_name=MODEL_NAME):
    """
    Generates a well-structured text response to a question using Gemini API.

    Args:
        prompt (str): The user's question.
        model_name (str, optional): The name of the Gemini model to use. Defaults to MODEL_NAME.

    Returns:
        str: A well-structured text response, or None if an error occurs.
    """
    try:
        model = genai.GenerativeModel(model_name)
        # System instruction to guide towards structured output - now more clearly commented
        system_instruction = """You are an AI assistant specialized in providing well-structured and organized answers.
        When responding to questions, please ensure your answer is clear, logical, and easy to understand.
        Use formatting techniques such as headings, bullet points, numbered lists, and paragraphs
        where appropriate to enhance readability and structure. Aim for a professional and organized presentation of information."""

        full_prompt = f"{system_instruction}\n\nUser Question: {prompt}"

        response = model.generate_content(full_prompt)
        return response.text

    except google.generativeai.APIError as api_error:  # More specific error handling for API issues
        print(f"API Error from Gemini: {api_error}")
        print("Please check your API key, API access, and request limits.")
        return None  # Indicate failure to get a response

    except Exception as e: # Catch-all for other potential errors
        print(f"An unexpected error occurred: {e}")
        return None


if __name__ == "__main__":
    api_key = get_api_key()  # Get API key from environment variable
    if not api_key:
        exit()  # Exit if API key is not found

    try:
        configure_gemini_api(api_key) # Configure API at the start

        user_question = input("Ask your question: ")
        if user_question:
            structured_answer = get_structured_response(user_question, MODEL_NAME) # Pass MODEL_NAME
            if structured_answer: # Check if we got a valid response
                print("\n--- Structured Answer ---")
                print(structured_answer)
                print("\n--- End Answer ---")
            else:
                print("Failed to get a structured answer from Gemini API.") # More informative failure message
        else:
            print("You did not enter a question.")

    except Exception as main_error: # Catch any errors during configuration or main execution
        print(f"A critical error occurred in the main application: {main_error}")
        print("The application may not have started correctly or encountered issues during runtime.")