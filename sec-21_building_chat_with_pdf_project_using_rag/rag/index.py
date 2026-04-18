
from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from dotenv import load_dotenv

# Load .env explicitly with override=True to avoid shell var conflicts
env_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path, override=True)

pdf_path = Path(__file__).parent / "Intro_to_ML_NPTEL.pdf"

# load this pdf file intp program
loader = PyPDFLoader(file_path=pdf_path)

# load pdf document (page by page)
docs = loader.load()

# split the docs into smaller chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=400,
)

# create chunks
chunks = text_splitter.split_documents(documents=docs)

# create vector embeddings for chunks
embedding_model = OpenAIEmbeddings(
    model="text-embedding-3-large"
)

# Langchain Qdrant integration

# create vector store in vector db
vector_store = QdrantVectorStore.from_documents(
    documents=chunks,
    embedding=embedding_model,
    url="http://localhost:6333",
    collection_name="learning_rag"
)

print(f"Indexing of documents done....")
