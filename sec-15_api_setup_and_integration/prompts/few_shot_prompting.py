
# Few Shot Prompting

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

# Few Shot Prompting - directly giving the instructions along with few examples to the model.
SYSTEM_PROMPT = """
You should only and only answer the coding related questions. Do not answer anything else. Your name is Codey. If user asks something other than coding, just say sorry

Examples: 
Q. Can you explain the a + b whole square?
A: Sorry, I can only help with Coding related questions.

Q. Write a code in python for adding two numbers
A: def add(a, b):
        return a + b


"""

response = client.chat.completions.create(
    model="gemini-3-flash-preview",
    messages=[
        {   "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": "Hey, Can you explain the a + b whole square?"
        }
    ]
)

print(f"Gemini API response via openAI: {response.choices[0].message}")
