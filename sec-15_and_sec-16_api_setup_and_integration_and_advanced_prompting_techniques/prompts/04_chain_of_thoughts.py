
# chain of thought prompting (CoT)

from openai import OpenAI
from dotenv import load_dotenv
import os
import json

# load env file
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = OpenAI(
    api_key=api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

SYSTEM_PROMPT = """
    You are an expert AI Assistant in resolving user queries using chain of thought.
    You work on START, PLAN and OUTPUT steps.
    You need to first PLAN what needs to be done. The PLAN can be multiple steps.
    Once you think enough PLAN has been done, finally you can give an OUTPUT.

    Rules:
    - Strictly Follow the given JSON output format
    - Only run one step at a time.
    - The sequence of step is START (where user gives an input), PLAN (That can be multiple times) and finally OUTPUT (which is going to the displayed to the user)

    Output JSON Format:
    { "step": "START" | "PLAN" | "OUTPUT", "content": "string" }

    Example:
    START: Hey, can you solve 2 + 3 * 5 / 10
    PLAN: { "step": "PLAN": "content": "Seems like user is interested in Math's problem"}
    PLAN: { "step": "PLAN": "content": "looking at the problem, we should solve this using BODMAS method" }
    PLAN: { "step": "PLAN": "content": "Yes, The BODMAS is correct thing to be done here"}
    PLAN: { "step": "PLAN": "content": "first we multiply 3 * 5 which is 15"}
    PLAN: { "step": "PLAN": "content": "Now the new equation is 2 + 15 / 10"}
    PLAN: { "step": "PLAN": "content": "we must preform divison that is 15/10 = 1.5"}
    PLAN: { "step": "PLAN": "content": "Now the new equation is 2 + 1.5"}
    PLAN: { "step": "PLAN": "content": "Now finally lets perform add 3.5"}
    PLAN: { "step": "PLAN": "content": "Great, we have solved and finally left with 3.5 as answer"}
    OUTPUT: { "step": "OUTPUT": "content": "3.5"}
"""

response = client.chat.completions.create(
    model="gemini-3-flash-preview",
    response_format={"type": "json_object"},
    messages=[
        {   "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": "Hey, write a code to add n numbers in JS"
        },

        # manually keep adding messages to History
        {
            "role": "assistant",
            "content": json.dumps({
                "step": "START",  
                "content": "The user wants a JavaScript function to sum an arbitrary number of inputs (n numbers"
            })
        },
        {
            "role": "assistant",
            "content": json.dumps({
                "step": "PLAN", 
                "content": "To add an arbitrary amount of numbers in JavaScript, I should use the rest parameter syntax `...args` to collect all inputs into an array."
            })
        },
        {
            "role": "assistant",
            "content": json.dumps({
                "step": "PLAN",
                "content": "Decide on the approach: Using the rest parameter `...numbers` is the most modern and flexible way to handle arguments in JavaScript."
            })
        }
    ]
)

print(f"Gemini API response via openAI: {response.choices[0].message}")