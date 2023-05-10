from langchain.document_loaders import PyMuPDFLoader
import os, glob
from langchain.document_loaders import ReadTheDocsLoader, PyPDFDirectoryLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Pinecone
import pinecone
from llama_index import SimpleDirectoryReader


pinecone.init(
    api_key=os.environ["PINECONE_API_KEY"],
    environment=os.environ["PINECONE_ENVIRONMENT_REGION"],
)

INDEX_NAME = "bsks-unibot2-index"

def ingest_docs():
    # Define the directory and file pattern
    directory = './data'
    file_pattern = "*.pdf"

    # Use os.path.join to combine the directory and file pattern
    search_path = os.path.join(directory, file_pattern)

    # Use glob.glob to find all matching files
    pdf_files = glob.glob(search_path)

    text_data = []
    # Print each file path
    for file_path in pdf_files:
        print(file_path)
        loader = PyMuPDFLoader(file_path)
        doc = loader.load()
        text_data = text_data + doc 
    
    raw_documents = text_data
    
    print(f"loaded {len(raw_documents)} documents")

    text_splitter = RecursiveCharacterTextSplitter( chunk_size=400, chunk_overlap=50 )
    documents    = text_splitter.split_documents(raw_documents)
    
    print( documents[10] )
    embeddings = OpenAIEmbeddings()
    
    print(f"Going to add {len(documents)} to Pinecone")
    Pinecone.from_documents(documents, embeddings, index_name=INDEX_NAME)
    print("****Loading to vectorestore done ***")

    
if __name__ == "__main__":
    ingest_docs()
