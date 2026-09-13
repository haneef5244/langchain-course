from dotenv import load_dotenv

load_dotenv()

from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain_unstructured import UnstructuredLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_pinecone import PineconeVectorStore

import os

def main() -> None:

    print("Hello world")
    file_path = "mediumblog1.txt"
    loader = UnstructuredLoader(file_path=file_path, chunking_strategy="basic", max_characters=1000000)
    document = loader.load()

    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    chunks  =  text_splitter.split_documents(documents=document)

    print(f"Len of chunks: {len(chunks)}")
    embeddings = OllamaEmbeddings(model="qwen3-embedding:4b", dimensions=1536)
    PineconeVectorStore.from_documents(documents=chunks, embedding=embeddings, index_name=os.environ["INDEX_NAME"])
    print("Finish")
    # return document


if __name__ == "__main__":
    main()
