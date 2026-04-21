from pathlib import Path
from dotenv import load_dotenv

# Load .env explicitly with override=True to avoid shell var conflicts
env_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path, override=True)

from typing_extensions import TypedDict
from typing import Annotated
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, START, END
from langchain_classic.chat_models import init_chat_model
from langgraph.checkpoint.mongodb import MongoDBSaver

llm = init_chat_model(
    model="gpt-4.1-mini",
    model_provider="openai"
)

class State(TypedDict):
    messages: Annotated[list, add_messages]

# create node (create method)
def chatbot(state: State):
    response = llm.invoke(state.get("messages"))
    return{
        "messages": [response]
    }


# create graph builder
graph_builder = StateGraph(State)

# register node with graph builder
graph_builder.add_node("chatbot", chatbot)

# add entry and exit point to tell graph
# where to start and where to end
graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", END)

# complie this graph using graph builder
graph = graph_builder.compile()

# method to compile graph with checkpointer
def compile_graph_with_checkpointer(checkpointer):
    return graph_builder.compile(checkpointer=checkpointer)

# open MongoDB connection and build graph with checkpointer
DB_URI = "mongodb://admin:admin@localhost:27017/lg?authSource=admin"
with MongoDBSaver.from_conn_string(DB_URI) as checkpointer:
    graph_with_checkpointer = compile_graph_with_checkpointer(checkpointer=checkpointer)

    config = {
        "configurable": {
            "thread_id": "peter"
        }
    }

    # run graph with initial state (invoke)
    # and return updated state
    for chunk in graph_with_checkpointer.stream(
        State({"messages": ["What is my name?"]}),
        config,
        stream_mode="values",
        ):
            chunk["messages"][-1].pretty_print()
        