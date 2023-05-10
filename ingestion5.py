from langchain.document_loaders import PyMuPDFLoader
import os
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

    loader = PyMuPDFLoader("dataTemp/001.pdf")
    data1= loader.load()
    
    loader = PyMuPDFLoader("dataTemp/002.pdf")
    data2= loader.load()

    loader = PyMuPDFLoader("dataTemp/003.pdf")
    data3= loader.load()

    raw_documents = data1 + data2 + data3

    print(f"loaded {len(raw_documents)} documents")

    text_splitter = RecursiveCharacterTextSplitter( chunk_size=400, chunk_overlap=50 )
    documents    = text_splitter.split_documents(raw_documents)
    
    print( documents[10] )
    embeddings = OpenAIEmbeddings()
    
    print(f"Going to add {len(documents)} to Pinecone")
    #Pinecone.from_documents(documents, embeddings, index_name=INDEX_NAME)
    print("****Loading to vectorestore done ***")

    
if __name__ == "__main__":
    ingest_docs()
