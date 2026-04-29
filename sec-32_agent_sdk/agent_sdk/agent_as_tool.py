
# agent as tool

from dotenv import load_dotenv
from pathlib import Path

# Load .env explicitly with override=True to avoid shell var conflicts
env_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path, override=True)

import asyncio
from agents import Agent, Runner

# define spanish agent
spanish_agent = Agent(
    name="Spanish Agent",
    instructions="You translate the user's message to Spanish",
)

# define french agent
french_agent = Agent(
    name="French Agent",
    instructions="You translate the user's message to French",
)

# orchestrator agent is going to talk to user
orchestrator_agent = Agent(
    name="orchestrator_agent",
    instructions=(
        "You are a translation agent. You use the tools given to you to translate."
        "If asked for multiple translations, you call the relevant tools."
    ),
    tools=[
        spanish_agent.as_tool(
            tool_name="translate_to_spanish",
            tool_description="Translate the user's message to Spanish",
        ),
        french_agent.as_tool(
            tool_name="translate_to_french",
            tool_description="Translate the user's message to French",
        ),
    ],
)

# run agent
async def main():
    result = await Runner.run(orchestrator_agent, input="Say 'Hello, how are you?' in French.")
    print("Result:", result.final_output)
    print("Raw Responses:", result.raw_responses)

if __name__ == "__main__":
    asyncio.run(main())

