
# Zero Shot Prompting

from openai import OpenAI
from dotenv import load_dotenv
import os

# load env file
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = OpenAI(
    api_key=api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Zero Shot Prompting - directly giving the instructions to the model.
SYSTEM_PROMPT = "You should only and only answer the coding related questions. Do not answer anything else. Your name is Codey. If user asks something other than coding, just say sorry"

response = client.chat.completions.create(
    model="gemini-3-flash-preview",
    messages=[
        {   "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": "Hey, Can you write a python code to translate the word hello to Hindi?"
        }
    ]
)

print(f"Gemini API response via openAI: {response.choices[0].message}")
