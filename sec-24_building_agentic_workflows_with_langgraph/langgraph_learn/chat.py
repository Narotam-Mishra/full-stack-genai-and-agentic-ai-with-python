
from typing_extensions import TypedDict
from typing import Annotated
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, START, END

class State(TypedDict):
    messages: Annotated[list, add_messages]

# create node (create method)
def chatbot(state: State):
    print(f"\n\nInside chatbot node: {state}")
    return{
        "messages": ["Hi, This is a message from ChatBot Node"]
    }

def samplenode(state: State):
    print(f"\n\nInside samplenode node: {state}")
    return{
        "messages": ["Sample message appended"]
    }

# create graph builder
graph_builder = StateGraph(State)

# register node with graph builder
graph_builder.add_node("chatbot", chatbot)
graph_builder.add_node("samplenode", samplenode)

# add entry and exit point to tell graph
# where to start and where to end
graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", "samplenode")
graph_builder.add_edge("samplenode", END)

# complie this graph using graph builder
graph = graph_builder.compile()

# run graph with initial state (invoke)
# and return updated state
updated_state = graph.invoke(State({"messages": ["Hi, My name is BenEvans"]}))
print("\n\nupdated state:", updated_state)