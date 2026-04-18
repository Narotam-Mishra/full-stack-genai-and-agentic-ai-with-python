
from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader

pdf_path = Path(__file__).parent / "stanford-machine-learning.pdf"

# load this pdf file intp program
loader = PyPDFLoader(file_path=pdf_path)

# load pdf document (page by page)
docs = loader.load()

print(f"Docs at page 10: {docs[10]}")