

from pathlib import Path
from dotenv import load_dotenv

# Load .env explicitly with override=True to avoid shell var conflicts
env_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path, override=True)

from typing_extensions import TypedDict
from typing import Optional, Literal
from langgraph.graph import StateGraph, START, END
from openai import OpenAI

client = OpenAI()

class State(TypedDict):
    user_query: str
    llm_output: Optional[str]
    is_good: Optional[bool]


def chatbot(state: State):
    print("Into chatbot node:", state)
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            { "role": "user", "content": state.get("user_query") }
        ]
    )

    state["llm_output"] = response.choices[0].message.content
    return state
    

def evaluate_response(state: State) -> Literal["chatbot_gemini", "endnode"]:
    print("Into evaluation node:", state)
    if False:
        return "endnode"
    
    return "chatbot_gemini"

def chatbot_gemini(state: State):
    print("Into chatbot_gemini node:", state)
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            { "role": "user", "content": state.get("user_query") }
        ]
    )

    state["llm_output"] = response.choices[0].message.content
    return state

def endnode(state: State):
    print("Into end node:", state)
    return state

# create graph builder
graph_builder = StateGraph(State)

# register node with graph builder
graph_builder.add_node("chatbot", chatbot)
graph_builder.add_node("chatbot_gemini", chatbot_gemini)
graph_builder.add_node("endnode", endnode)

# add entry and exit point to tell graph
# where to start and where to end
graph_builder.add_edge(START, "chatbot")
graph_builder.add_conditional_edges("chatbot", evaluate_response)
graph_builder.add_edge("chatbot_gemini", "endnode")
graph_builder.add_edge("endnode", END)

# complie this graph using graph builder
graph = graph_builder.compile()

# run graph with initial state (invoke)
# and return updated state
updated_state = graph.invoke(State({"user_query": "Hey, What is capital of Canada?"}))
print("\n\nupdated state:", updated_state)