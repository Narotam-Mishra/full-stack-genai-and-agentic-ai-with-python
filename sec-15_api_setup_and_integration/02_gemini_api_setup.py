
from google import genai
from dotenv import load_dotenv
from pathlib import Path
import os

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

# client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client(api_key=api_key)


response = client.models.generate_content(
    model="gemini-3.1-flash-lite-preview", contents="Explain how AI works in a few words"
)
print(f"Response: {response.text}")