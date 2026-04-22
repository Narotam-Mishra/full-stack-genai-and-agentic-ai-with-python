
# memory agent

from pathlib import Path
from dotenv import load_dotenv

env_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path, override=True)
import os

from mem0 import Memory

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

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
        "vector_store": {
            "provider": "qdrant",
            "config": {
                "host": "localhost",
                "port": 6333,
            }
        }
    }
}

# create memory client
mem_client = Memory.from_config(config)