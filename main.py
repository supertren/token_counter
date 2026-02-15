import os
import sys
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    print("CRITICAL: GEMINI_API_KEY var not loaded.")
    sys.exit(1)

genai.configure(api_key=API_KEY)

def get_token_count(prompt_text):
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.count_tokens(prompt_text)
        return response.total_tokens
    except Exception as e:
        print(f"ERROR: {e}")
        return -1

if __name__ == "__main__":
    test_prompt = "System health check and tokenization metric test."
    tokens = get_token_count(test_prompt)
    print(f"--- CONTAINER OUTPUT ---")
    print(f"Target: Gemini 1.5 Flash")
    print(f"Payload Tokens: {tokens}")
    print(f"--- END OUTPUT ---")
