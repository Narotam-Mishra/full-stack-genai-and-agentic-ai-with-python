
# automate CoT

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

print("\n\n\n")

message_history = [
    {  "role": "system", "content": SYSTEM_PROMPT },
]

user_query = input("👉")
message_history.append({ "role": "user", "content": user_query })

while True:
    response = client.chat.completions.create(
        model="gemini-3-flash-preview",
        response_format={"type": "json_object"},
        messages=message_history
    )

    raw_result = response.choices[0].message.content
    message_history.append({"role": "assistant", "content": raw_result})

    parsed_result = json.loads(raw_result)

    # if parsed_result.get("step") == "START":
    #     print("🔥 starting:", parsed_result.get("content"))
    #     continue

    # if parsed_result.get("step") == "PLAN":
    #     print("🧠 planning:", parsed_result.get("content"))
    #     continue

    # if parsed_result.get("step") == "OUTPUT":
    #     print("🤖 output:", parsed_result.get("content"))
    #     break

    # normalize to always work with a list of steps
    steps = parsed_result if isinstance(parsed_result, list) else [parsed_result]

    output_reached = False
    for step in steps:
        if step.get("step") == "START":
            print("🔥 starting:", step.get("content"))

        elif step.get("step") == "PLAN":
            print("🧠 planning:", step.get("content"))

        elif step.get("step") == "OUTPUT":
            print("🤖 output:", step.get("content"))
            output_reached = True

    if output_reached:
        break


print("\n\n\n")
