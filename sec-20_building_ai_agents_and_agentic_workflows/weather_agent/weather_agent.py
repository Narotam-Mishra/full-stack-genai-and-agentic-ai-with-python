
# weather agent

from openai import OpenAI
from dotenv import load_dotenv
import json
import requests
from pathlib import Path


# Load .env explicitly with override=True to avoid shell var conflicts
env_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path, override=True)


client = OpenAI()

def get_weather(city: str):
    url = f"https://wttr.in/{city.lower()}?format=%C+%t"
    res = requests.get(url)

    if res.status_code == 200:
        return f"The weather in {city} is {res.text}"
    
    return "Something went wrong"

available_tools = {
    "get_weather": get_weather
}

SYSTEM_PROMPT = """
    You are an expert AI Assistant in resolving user queries using chain of thought.
    You work on START, PLAN and OUTPUT steps.
    You need to first PLAN what needs to be done. The PLAN can be multiple steps.
    Once you think enough PLAN has been done, finally you can give an OUTPUT.
    You can also call a tool if required from the list of available tools
    for every tool call wait for the observe step which is the output from the called tool.

    Rules:
    - Strictly Follow the given JSON output format
    - Only run one step at a time.
    - The sequence of step is START (where user gives an input), PLAN (That can be multiple times) and finally OUTPUT (which is going to the displayed to the user)

    Output JSON Format:
    { "step": "START" | "PLAN" | "OUTPUT" | "TOOL" , "content": "string", "tool": "string", "input": "string" }

    Available Tools:
    - get_weather(city: str): Takes city name as an input string and returns the weather info about the city.

    Example 1:
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

    Example 2:
    START: What is weather of Delhi?
    PLAN: { "step": "PLAN": "content": "Seems like user is interested in getting weather of Delhi in India"}
    PLAN: { "step": "PLAN": "content": "let see if we have any available tool from the list of available tools" }
    PLAN: { "step": "PLAN": "content": "Great, we have get_weather tool available for this query"}
    PLAN: { "step": "PLAN": "content": "I need to call get_weather tool for delhi as input for city"}
    PLAN: { "step": "TOOL": "tool": "get_weather" "input": "delhi"}
    PLAN: { "step": "OBSERVE": "tool": "get_weather" "output": "The temperature of delhi is cloudy with 24 C"}
    PLAN: { "step": "PLAN": "content": "Great, I got the weather info about delhi"}
    OUTPUT: { "step": "OUTPUT": "content": "The current weather in delhi is 20 C with some cloudy sky."}
"""

print("\n\n\n") 

message_history = [
    {  "role": "system", "content": SYSTEM_PROMPT },
]

while True:
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

            elif step.get("step") == "TOOL":
                tool_to_call = step.get("tool")
                tool_input = step.get("input")
                tool_response = available_tools[tool_to_call](tool_input)
                print(f"🔨tool call: {tool_to_call} {tool_input} = {tool_response}")

                message_history.append({ "role": "developer", "content": json.dumps(
                    {
                        "step": "OBSERVE",
                        "tool": tool_to_call,
                        "input": tool_input,
                        "output": tool_response
                    }
                )})
                continue

            elif step.get("step") == "PLAN":
                print("🧠 planning:", step.get("content"))

            elif step.get("step") == "OUTPUT":
                print("🤖 output:", step.get("content"))
                output_reached = True

        if output_reached:
            break


    print("\n\n\n")
