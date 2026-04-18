
from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from dotenv import load_dotenv
from openai import OpenAI

# Load .env explicitly with override=True to avoid shell var conflicts
env_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path, override=True)

# openai clinet
openai_client = OpenAI()

# create vector embeddings for chunks
embedding_model = OpenAIEmbeddings(
    model="text-embedding-3-large"
)

# connect to vector db
vector_db = QdrantVectorStore.from_existing_collection(
    url="http://localhost:6333",
    collection_name="learning_rag",
    embedding=embedding_model,
)

# take user input
user_query = input("Ask something: ")

# perform similarity search on vector db using user query
# get relevant chunks from the vector db
search_results = vector_db.similarity_search(query=user_query)

context = "\n\n\n".join([f"Page Content: {result.page_content}\nPage Number:{result.metadata['page_label']}\nFile Location: {result.metadata['source']}" for result in search_results])

SYSTEM_PROMPT = f"""
   You are a helpful AI Assistant who answers user query based on the available context retrieved from a PDF file along with page_contents and page number.

   You should only answer the user based on the following context and navigate the user to open the right page number to know more.

   Context: {context}
"""

response = openai_client.chat.completions.create(
    model="gpt-5",
    messages=[
        { "role": "system", "content": SYSTEM_PROMPT },
        { "role": "user", "content": user_query }
    ],
)

print(f"🤖: Response: {response}")