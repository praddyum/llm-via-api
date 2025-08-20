import os
import requests
import json 

# Model Specifications
MODEL_NAME = "gemini-1.5-flash-latest"
API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL_NAME}:generateContent"

class GeminiClient:
    """A client to interact with the Google Gemini API."""

    def __init__(self, api_key: str):
        """
        Initializes the client.
        - Best Practice: Raise an error if the API key is missing.
        """
        if not api_key:
            raise ValueError("GEMINI_API_KEY environment variable not found.")
        self.api_key = api_key
        self.headers = {"Content-Type": "application/json"}
        self.params = {"key": self.api_key}
    
    def ask(self, question: str) -> str:
        """
        Sends a question to the Gemini API and returns the answer.
        - Best Practice: Separate the logic for making the API call.
        """
        payload = {"contents": [{"parts": [{"text": question}]}]}
    
        try:
            response = requests.post(API_URL, params=self.params, headers=self.headers, json=payload)
            
            # --- Best Practice: Check for HTTP errors ---
            response.raise_for_status() 
            
            data = response.json()
            
            # --- Best Practice: Safely parse the expected JSON structure ---
            return data['candidates'][0]['content']["parts"][0]["text"]

        except requests.exceptions.HTTPError as http_err:
            return f"HTTP Error: {http_err}"
        except requests.exceptions.RequestException as req_err:
            return f"Request Error: {req_err}"
        except (KeyError, IndexError) as json_err:
            return f"Error parsing response JSON: {json_err}\\nRaw Response: {response.text}"
        except Exception as e:
            return f"An unexpected error occurred: {e}"

def main():
    """
    The main function to run the interactive terminal chat.
    - Best Practice: Keep the user interaction loop clean and separate.
    """

    print("🔮 Welcome to the Gemini Terminal Chat 🔮")
    print("Ask me anything! Type 'exit' or 'quit' to end the session.")

    try:
        api_key = os.getenv("GEMINI_API_KEY")
        client = GeminiClient(api_key)

        while True:
            question = input("\\n> ")
            if question.lower() in ["exit", "quit"]:
                print("Farewell, mortal!")
                break
            
            answer = client.ask(question)
            print(f"\\n🤖 Gemini: {answer}")

    except ValueError as e:
        print(f"Configuration Error: {e}")
    except KeyboardInterrupt:
        print("\\n\\nSession ended by user. Farewell!")

# Entry Point for the Application
if __name__=="__main__":
    main()
