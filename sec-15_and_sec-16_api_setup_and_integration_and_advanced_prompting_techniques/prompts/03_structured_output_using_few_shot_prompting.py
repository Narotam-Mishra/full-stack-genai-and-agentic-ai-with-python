
# structured output using few shot prompting

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

Rule:
- Strictly follow the output in JSON format

Output Format:
{{
  "code": "string" or null
  "is_coding_question": boolean
}}

Examples: 
Q. Can you explain the a + b whole square?
A: {{ "code": null, "is_coding_question": false }}

Q. Write a code in python for adding two numbers
A: {{ "code": "def add(a, b):
        return a + b", "is_coding_question": true }}



"""

response = client.chat.completions.create(
    model="gemini-3-flash-preview",
    messages=[
        {   "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": "Hey, write a code to add n numbers in JS"
        }
    ]
)

print(f"Gemini API response via openAI: {response.choices[0].message}")
