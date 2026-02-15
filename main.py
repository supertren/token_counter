import os
import sys
import logging
import argparse
import google.generativeai as genai
import json
from dotenv import load_dotenv

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

# Load environment variables from .env file
load_dotenv()

# --- Configuration ---
API_KEY = os.getenv("GEMINI_API_KEY")
MODEL_NAME = os.getenv("GEMINI_MODEL", "gemini-1.5-flash")
DEFAULT_PROMPT = "System health check and tokenization metric test."

def main():
    """
    Main function to run the Gemini token counter.
    """
    if not API_KEY:
        logging.critical("GEMINI_API_KEY var not loaded.")
        sys.exit(1)

    try:
        genai.configure(api_key=API_KEY)
    except Exception as e:
        logging.critical(f"Failed to configure Gemini API: {e}")
        sys.exit(1)

    # --- Argument Parsing ---
    parser = argparse.ArgumentParser(description="Count tokens for a given prompt using the Gemini API.")
    parser.add_argument("prompt", type=str, nargs='?', default=DEFAULT_PROMPT,
                        help="The prompt text to count tokens for.")
    args = parser.parse_args()

    # --- Token Counting ---
    tokens = get_token_count(args.prompt, MODEL_NAME)

    # --- Structured Output ---
    output_data = {
        "target_model": MODEL_NAME,
        "prompt_text": args.prompt,
        "status": "SUCCESS" if tokens != -1 else "FAILED",
        "token_count": tokens if tokens != -1 else None,
    }
    print(json.dumps(output_data))

def get_token_count(prompt_text: str, model_name: str) -> int:
    """
    Counts the number of tokens in a given text for a specific Gemini model.

    Args:
        prompt_text: The text to be tokenized.
        model_name: The name of the Gemini model to use for tokenization.

    Returns:
        The total number of tokens, or -1 if an error occurs.
    """
    try:
        model = genai.GenerativeModel(model_name)
        response = model.count_tokens(prompt_text)
        return response.total_tokens
    except Exception as e:
        logging.error(f"Could not count tokens: {e}")
        return -1

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logging.critical(f"An unexpected error occurred: {e}")
        sys.exit(1)
