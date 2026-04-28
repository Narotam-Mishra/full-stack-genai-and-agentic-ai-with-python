
# weather agent using voice agent

from openai import OpenAI
from dotenv import load_dotenv
import json
import requests
from pathlib import Path
from pydantic import BaseModel, Field
from typing import Optional
import asyncio
import speech_recognition as sr
from openai.helpers import LocalAudioPlayer
from openai import AsyncOpenAI

# Load .env explicitly with override=True to avoid shell var conflicts
env_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path, override=True)


client = OpenAI()

# create async client
async_client = AsyncOpenAI()

async def tts(speech: str):
    async with async_client.audio.speech.with_streaming_response.create(
        model="gpt-4o-mini-tts",
        voice="coral",
        instructions="Always speak in cheerful manner with full of delight and happiness",
        input=speech,
        response_format="pcm",
    ) as response:
        await LocalAudioPlayer().play(response)

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

    Example:
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

class MyOutputFormat(BaseModel):
    step: str = Field(..., description="The ID of the step. Example: PLAN, OUTPUT, TOOL, etc")
    content: Optional[str] = Field(None, description="The optional string content for the step")
    tool: Optional[str] = Field(None, description="The ID of the tool to call")
    input: Optional[str] = Field(None, description="The input params for the tool")

message_history = [
    {  "role": "system", "content": SYSTEM_PROMPT },
]

# speech to text recognizer
spr = sr.Recognizer()
with sr.Microphone() as source:
    spr.adjust_for_ambient_noise(source, duration=0.5)  # shorter calibration
    spr.pause_threshold = 2

    while True:
        print("Speak something...")
        try:
            audio = spr.listen(source, timeout=7, phrase_time_limit=10)
        except sr.WaitTimeoutError:
            print("No speech detected. Try lowering energy_threshold manually.")
            continue

        print("Processing Audio... (STT)")
        try:
            user_query = spr.recognize_google(audio)
            print("You said:", user_query)
        except sr.UnknownValueError:
            print("Could not understand audio.")
            continue
        except sr.RequestError as e:
            print(f"API error: {e}")
            continue

        message_history.append({ "role": "user", "content": user_query })
        
        while True:
            response = client.chat.completions.parse(
                model="gpt-4.1",
                response_format=MyOutputFormat,
                messages=message_history
            )

            raw_result = response.choices[0].message.content
            message_history.append({"role": "assistant", "content": raw_result})

            parsed_result = response.choices[0].message.parsed

            if parsed_result.step == "START":
                print("🔥 starting:", parsed_result.content)
                continue

            if parsed_result.step == "TOOL":
                tool_to_call = parsed_result.tool
                tool_input = parsed_result.input
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

            if parsed_result.step == "PLAN":
                print("🧠 planning:", parsed_result.content)
                continue

            if parsed_result.step == "OUTPUT":
                print("🤖 output:", parsed_result.content)
                
                # run tts task
                asyncio.run(tts(speech=parsed_result.content))
                break
                
        