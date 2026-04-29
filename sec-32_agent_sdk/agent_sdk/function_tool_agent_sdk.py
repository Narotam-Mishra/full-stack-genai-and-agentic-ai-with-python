

# using function tools with agent sdk

from dotenv import load_dotenv
from pathlib import Path

# Load .env explicitly with override=True to avoid shell var conflicts
env_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path, override=True)

from agents import Agent, Runner, WebSearchTool, function_tool
import requests

@function_tool()
def get_weather(city: str):
    """ fetch the weather for the given city
    Args:
        city: The city name to fetch the weather for
    """

    url = f"https://wttr.in/{city.lower()}?format=%C+%t"
    res = requests.get(url)

    if res.status_code == 200:
        return f"The weather in {city} is {res.text}"
    
    return "Something went wrong"


# define an agent
hello_agent = Agent(
    name="Hello World Agent",
    instructions="You are an agent which greets the user and helps them answer using emoji and in funny way",
    tools=[
        # WebSearchTool(),
        get_weather
    ]
)

# run agent
res = Runner.run_sync(hello_agent, "Hey, can you fetch weather information for Buxar, 802101??")

print(f"Result: {res.final_output}")

