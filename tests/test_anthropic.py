import anthropic
from anthropic import AuthenticationError
from dotenv import load_dotenv
import os 

load_dotenv()

# Replace with your actual key or load from an environment variable
api_key = os.getenv("ANTHROPIC_API_KEY")

def validate_anthropic_key(key):
    try:
        client = anthropic.Anthropic(api_key=key)
        
        # Make a lightweight call to the Messages API
        response = client.messages.create(
            # model="claude-3-haiku-20240307",
            model="claude-haiku-4-5-20251001",
            max_tokens=1,
            messages=[{"role": "user", "content": "Hi"}]
        )
        print("Success: Your API key is valid!")
        return True

    except AuthenticationError:
        print("Failed: Invalid API key or your account lacks active billing.")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

validate_anthropic_key(api_key)
