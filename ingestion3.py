from langchain.document_loaders import ReadTheDocsLoader, PyPDFDirectoryLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Pinecone
import pinecone
import os
import PyPDF2
import fitz

pinecone.init(
    api_key=os.environ["PINECONE_API_KEY"],
    environment=os.environ["PINECONE_ENVIRONMENT_REGION"],
)

INDEX_NAME = "bsks-unibot2-index"

def ingest_docs():
    # './data/' 폴더에서 PDF 파일 목록 가져오기
    data_folder = './dataTemp/'
    pdf_files = [f for f in os.listdir(data_folder) if f.endswith('.pdf')]

    # PDF 파일별로 텍스트 추출 및 출력
    for pdf_file in pdf_files:
        file_path = os.path.join(data_folder, pdf_file)
    
        # PDF 파일 열기
        with open(file_path, 'rb') as file:
            doc = fitz.open(file_path)
            print( doc )
            # PDF 페이지별로 텍스트 추출
            extracted_text = ''
            for page in doc:
                extracted_text +=  page.get_text()

            # 추출된 텍스트 출력
            print(f'Text extracted from {pdf_file}:\n')
            print(extracted_text)
            print('\n' + '-' * 80 + '\n')



if __name__ == "__main__":
    ingest_docs()
