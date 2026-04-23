
# memory agent

from pathlib import Path
from dotenv import load_dotenv

env_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path, override=True)
import os

from mem0 import Memory
from openai import OpenAI
import json

# create openai client
client = OpenAI()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
NEO4J_URL = os.getenv("NEO4J_CONNECTION_URI")
NEO4J_USERNAME = os.getenv("NEO4J_USERNAME")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")

# define configuration for memory setup
config = {
    "version": "v1.1",
    "embedder": {
        "provider": "openai",
        "config": {
            "api_key": OPENAI_API_KEY,
            "model": "text-embedding-3-small"
        },
        "llm": {
            "provider": "openai",
            "config": {
                "api_key": OPENAI_API_KEY,
                "model": "gpt-4.1"
            },
        },
    },
    "graph_store":{
        "provider": "neo4j",
        "config": {
            "url": NEO4J_URL,
            "username": NEO4J_USERNAME,
            "password": NEO4J_PASSWORD,
        }
    },
    "vector_store": {
        "provider": "qdrant",
        "config": {
            "host": "localhost",
            "port": 6333,
        }
    }
}

# create memory client
mem_client = Memory.from_config(config)

# create loop for continuous conversation...
while True:
    user_query = input("> ")

    # search memory using given user's query
    # it will return dictionary
    search_memory = mem_client.search(query=user_query, filters={"user_id": "peter"})

    # dic to list
    memories = [
        f"ID: {mem.get("id")}\n Memory: {mem.get("memory")}" 
        for mem in search_memory.get("results")
    ]

    print("found memories:", memories)

    SYSTEM_PROMPT = f"""
        Here is the context about the user:
        {json.dumps(memories)}
    """

    response =  client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            { "role": "system", "content": SYSTEM_PROMPT },
            { "role": "user", "content": user_query }
        ]
    )

    ai_response = response.choices[0].message.content

    print("AI Response:", ai_response)

    # add chat to memory agent
    mem_client.add(
        user_id="peter",
        messages=[
            { "role": "user", "content": user_query },
            { "role": "assistant", "content": ai_response }
        ]
    )

    print("Memory has been saved...")