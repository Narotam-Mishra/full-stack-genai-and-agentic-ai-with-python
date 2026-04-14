
# automate CoT

from openai import OpenAI
from dotenv import load_dotenv
from pathlib import Path
import os
import json

# Load .env explicitly with override=True to avoid shell var conflicts
env_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path, override=True)

api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(
    api_key=api_key,
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
        model="gpt-4o",
        response_format={"type": "json_object"},
        messages=message_history
    )

    raw_result = response.choices[0].message.content
    message_history.append({"role": "assistant", "content": raw_result})

    parsed_result = json.loads(raw_result)

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
