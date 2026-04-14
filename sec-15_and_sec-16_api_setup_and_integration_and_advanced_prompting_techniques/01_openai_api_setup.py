from openai import OpenAI
from dotenv import load_dotenv
from pathlib import Path
import os

# Load .env explicitly with override=True to avoid shell var conflicts
env_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path, override=True)

api_key = os.getenv("OPENAI_API_KEY")
# print("Loaded from:", env_path)

# pass explicitly to be safe
client = OpenAI(api_key=api_key)  

res = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "How OpenAI supress their competitor?"}]
)

print("Response:", res.choices[0].message.content)