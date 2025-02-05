# Gemini Structured Response Python Script

This Python script utilizes the Google Gemini API to generate well-structured text responses to user questions. It is designed to provide clear, organized, and readable answers by leveraging system instructions to guide the Gemini model.

## Description

The script takes a user's question as input and sends it to the Google Gemini API. By employing a system instruction that emphasizes structured output, the script encourages the Gemini model to generate responses that are well-formatted using elements like paragraphs, bullet points, numbered lists, and potentially headings. This makes the answers easier to understand and digest.

## Prerequisites

Before running this script, ensure you have the following:

1.  **Google AI Studio API Key:** You need a valid API key from Google AI Studio to access the Gemini API. You can obtain one by visiting [Google AI Studio](https://makersuite.google.com/).
2.  **Python 3.6 or higher:**  Python must be installed on your system.
3.  **`google-generativeai` library:** This Python library is required to interact with the Gemini API. You can install it using pip:

    ```bash
    pip install google-generativeai
    ```

## How to Use

Follow these steps to use the script:

1.  **Obtain your Google Gemini API Key:**
    *   Go to [Google AI Studio](https://makersuite.google.com/) and create or access your project.
    *   Generate an API key if you haven't already.
    *   Copy your API key.

2.  **Replace Placeholder API Key:**
    *   Open the Python script (`your_script_name.py`, or whatever you named it) in a text editor.
    *   Locate the line:
        ```python
        GEMINI_API_KEY = "YOUR_API_KEY_HERE"
        ```
    *   Replace `"YOUR_API_KEY_HERE"` with your actual Gemini API key you copied in the previous step. **Make sure to keep the API key secure and do not share it publicly.**

3.  **Install `google-generativeai` library:**
    *   If you haven't already, open your terminal or command prompt and run:
        ```bash
        pip install google-generativeai
        ```

4.  **Run the Python Script:**
    *   Navigate to the directory where you saved the Python script in your terminal.
    *   Execute the script using the command:
        ```bash
        python your_script_name.py
        ```
        (Replace `your_script_name.py` with the actual name of your script file).

5.  **Enter Your Question:**
    *   When prompted in the terminal, type your question and press Enter. For example:
        ```
        Ask your question: What are the benefits of exercise?
        ```

6.  **View the Structured Answer:**
    *   The script will send your question to the Gemini API and then display the structured answer in the terminal, enclosed within delimiters:
        ```
        --- Structured Answer ---
        [Structured answer from Gemini API will appear here]
        --- End Answer ---
        ```

## Python Code

```python
import google.generativeai as genai

# Paste your Google AI Studio API key here
GEMINI_API_KEY = "YOUR_API_KEY_HERE"

# Configure the API key
genai.configure(api_key=GEMINI_API_KEY)

# Select the Gemini model - back to 'gemini-pro' for text
model = genai.GenerativeModel('gemini-pro')

def get_structured_response(prompt):
    """
    Generates a well-structured text response to a question using Gemini API.

    Args:
        prompt (str): The user's question.

    Returns:
        str: A well-structured text response, or an error message if something goes wrong.
    """
    try:
        # System instruction to guide towards structured output
        system_instruction = "You are an AI assistant specialized in providing well-structured and organized answers. " \
                             "When responding to questions, please ensure your answer is clear, logical, and easy to understand. " \
                             "Use formatting techniques such as headings, bullet points, numbered lists, and paragraphs " \
                             "where appropriate to enhance readability and structure. Aim for a professional and organized presentation of information."

        # Combine system instruction and user prompt
        full_prompt = f"{system_instruction}\n\nUser Question: {prompt}"

        response = model.generate_content(full_prompt)
        return response.text
    except Exception as e:
        return f"An error occurred: {str(e)}"

if __name__ == "__main__":
    user_question = input("Ask your question: ")
    if user_question:
        structured_answer = get_structured_response(user_question)
        print("\n--- Structured Answer ---")
        print(structured_answer)
        print("\n--- End Answer ---")
    else:
        print("You did not enter a question.")