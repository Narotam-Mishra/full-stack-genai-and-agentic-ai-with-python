
from pathlib import Path
from dotenv import load_dotenv

env_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path, override=True)

from typing_extensions import TypedDict
from typing import Annotated
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, START, END
from langchain_classic.chat_models import init_chat_model
from langgraph.checkpoint.mongodb import MongoDBSaver
from pymongo import MongoClient

llm = init_chat_model(
    model="gpt-4.1-mini",
    model_provider="openai"
)

class State(TypedDict):
    messages: Annotated[list, add_messages]

def chatbot(state: State):
    response = llm.invoke(state.get("messages"))
    return {"messages": [response]}

# create graph builder
graph_builder = StateGraph(State)
graph_builder.add_node("chatbot", chatbot)
graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", END)

# ✅ Create MongoDB client manually (stays open)
DB_URI = "mongodb://admin:admin@localhost:27017/lg?authSource=admin"
mongodb_client = MongoClient(DB_URI)
checkpointer = MongoDBSaver(mongodb_client)
graph_with_checkpointer = graph_builder.compile(checkpointer=checkpointer)

config = {
    "configurable": {
        "thread_id": "peter"
    }
}

updated_state = graph_with_checkpointer.stream(
    {"messages": ["What is my name?"]},
    config
)
print("\n\nupdated state:", updated_state)

# ✅ Close the client only after you're completely done
mongodb_client.close()