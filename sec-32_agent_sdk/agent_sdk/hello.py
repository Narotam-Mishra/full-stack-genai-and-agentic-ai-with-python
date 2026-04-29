
# create first agent using openai agent sdk

from dotenv import load_dotenv
from pathlib import Path

# Load .env explicitly with override=True to avoid shell var conflicts
env_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path, override=True)

from agents import Agent, Runner

# define an agent
hello_agent = Agent(
    name="Hello World Agent",
    instructions="You are an agent which greets the user and helps them answer using emoji and in funny way",
)

# run agent
res = Runner.run_sync(hello_agent, "Hey there, My Name is Peter Evans")

print(f"Result: {res.final_output}")