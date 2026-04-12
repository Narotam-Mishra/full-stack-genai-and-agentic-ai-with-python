
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

response = client.chat.completions.create(
    model="gemini-3-flash-preview",
    messages=[
        # {   "role": "system",
        #     "content": "You are a helpful assistant."
        # },
        {   "role": "system",
            "content": "You are an expert in Maths and only and only answer Maths related questions. If the query is not related to Maths, just say sorry and do not answer"
        },
        {
            "role": "user",
            "content": "Hey, Can you help me solve a + b whole cube"
        }
    ]
)

print(f"Gemini API response via openAI: {response.choices[0].message}")
