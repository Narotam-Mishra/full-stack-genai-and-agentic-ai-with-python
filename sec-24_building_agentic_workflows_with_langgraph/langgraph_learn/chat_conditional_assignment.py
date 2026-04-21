
from pathlib import Path
from dotenv import load_dotenv

# Load .env explicitly with override=True to avoid shell var conflicts
env_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path, override=True)

from typing import Optional, Literal
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
from openai import OpenAI

client = OpenAI()

class State(TypedDict):
    user_query: str
    llm_output: Optional[str]
    is_good: Optional[bool]

# Node 1: Chatbot (GPT-4o-mini)
def chatbot_node(state: State) -> State:
    print("\n📝 [CHATBOT] Generating initial response...")
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": state["user_query"]}]
    )
    output = response.choices[0].message.content
    print(f"   Response: {output[:100]}...")
    return {"llm_output": output}

# Node 2: Gemini fallback (better model)
def gemini_node(state: State) -> State:
    print("\n🔄 [GEMINI] Generating improved response...")
    # Using GPT-4 (better model) as fallback
    response = client.chat.completions.create(
        model="gpt-4",  # Better model for fallback
        messages=[
            {"role": "system", "content": "Provide a more accurate, detailed, and helpful response."},
            {"role": "user", "content": state["user_query"]}
        ]
    )
    output = response.choices[0].message.content
    print(f"   Improved response: {output[:100]}...")
    return {"llm_output": output, "is_good": True}

# Node 3: End node
def end_node(state: State) -> State:
    print("\n🏁 [END] Done!")
    return state

# ============================================
# ASSIGNMENT SOLUTION: AI-based evaluation
# ============================================
def evaluate_with_ai(state: State) -> Literal["good_end", "retry_gemini"]:
    """
    Use an AI judge to evaluate response quality.
    Returns which node to go to next.
    """
    print("\n🤖 [EVALUATOR] AI Judge is reviewing the response...")
    
    evaluation_prompt = f"""
    You are a quality evaluator. Analyze this response and decide if it's GOOD or BAD.
    
    User Question: {state['user_query']}
    
    AI Response: {state['llm_output']}
    
    Criteria for GOOD response:
    - Accurate and correct information
    - Helpful and relevant to the question
    - Clear and well-structured
    - No harmful or misleading content
    
    Respond with ONLY ONE WORD: "GOOD" or "BAD"
    """
    
    try:
        eval_response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # Cheaper model for evaluation
            messages=[{"role": "user", "content": evaluation_prompt}],
            max_tokens=10
        )
        
        verdict = eval_response.choices[0].message.content.strip().upper()
        
        if "GOOD" in verdict:
            print("   ✅ AI Judge says: GOOD response!")
            return "good_end"
        else:
            print("   ❌ AI Judge says: BAD response - needs improvement!")
            return "retry_gemini"
            
    except Exception as e:
        print(f"   ⚠️ Evaluation error: {e}. Defaulting to GOOD.")
        return "good_end"

# Build graph
builder = StateGraph(State)
builder.add_node("chatbot", chatbot_node)
builder.add_node("retry_gemini", gemini_node)
builder.add_node("good_end", end_node)

# Edges
builder.add_edge(START, "chatbot")
builder.add_conditional_edges(
    "chatbot",
    evaluate_with_ai,  # USING AI EVALUATION (not hardcoded!)
    {
        "good_end": "good_end",
        "retry_gemini": "retry_gemini"
    }
)
builder.add_edge("retry_gemini", "good_end")
builder.add_edge("good_end", END)

graph = builder.compile()

# Test with different queries
test_queries = [
    "What is 2+2?",  # Should be GOOD
    "Explain quantum physics in one sentence",  # Might be GOOD
    "What is the meaning of life?"  # Subjective
]

for query in test_queries:
    print("\n" + "=" * 60)
    print(f"🔵 TESTING QUERY: {query}")
    print("=" * 60)
    
    result = graph.invoke({"user_query": query})
    print(f"\n📌 FINAL ANSWER: {result['llm_output']}")