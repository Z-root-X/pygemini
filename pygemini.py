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