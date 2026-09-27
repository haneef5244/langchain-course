import asyncio, os, ssl
from typing import Any, Dict, List

import certifi
from dotenv import load_dotenv

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from langchain_ollama import OllamaEmbeddings
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore
from langchain_tavily import TavilyCrawl, TavilyExtract, TavilyMap, tavily_crawl

from crawl import crawl_url
from logger import(Colors, log_error, log_header, log_info, log_success)

load_dotenv()

# Configure SSL Context to use certifi certificates
ssl_context = ssl.create_default_context(cafile=certifi.where())
os.environ["SSL_CERT_FILE"] = certifi.where()
os.environ["REQUESTS_CA_BUNDLE"] = certifi.where()

documentation_url = "https://python.langchain.com"

 # Call embedding model
embeddings = OllamaEmbeddings(
    model="qwen3-embedding:0.6b",
) 

vector_store = PineconeVectorStore(
        index_name=os.environ.get("INDEX_NAME"),
        embedding=embeddings
)

async def main():
    """Main async function to orchestrate the entire process."""

    log_header("DOCUMENTATION INGESTION PIPELINE")

    log_info(
        f"   TavilyCrawl: Starting to Crawl documentation from {documentation_url}",
        Colors.PURPLE
    )

    # Load the data

    documents = await crawl_url(url=documentation_url)

    # Split the data into chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=4000, chunk_overlap=200)
    splitted_docs = text_splitter.split_documents(documents)
    log_success(
        f"Text Splitter: Created {len(splitted_docs)} chunks from {len(documents)} documents"
    )

    # await aindex_documents(documents=splitted_docs, batch_size=200)

async def aindex_documents(documents: List[Document], batch_size: int = 50):
    """Process documents in batches asynchronously"""
    log_header("VECTOR STORAGE PHASE")
    log_info(
        f"  VectorStore indexing: Preparing to add {len(documents)} documents to vector store",
        Colors.DARKCYAN
    )

    batches = [
        documents[i : i + batch_size] for i in range(0, len(documents), batch_size)
    ]

    log_info(
        f"  VectorStore indexing: split into {len(batches)} batches of {batch_size} documents each"
    )

    async def aadd_batch(batches: List[Document], batch_num: int):  
        try:
            await vector_store.aadd_documents(batches)
            log_success(
                f"VectorStore indexing: Successfully added batch {batch_num}/{len(batches)} ({len(batches)} documents)"
            )
        except Exception as e:
            log_error(f"VectorStore indexing: Failed to add batch {batch_num} - {e}")
            return False
        return True

    tasks = [aadd_batch(batch, i + 1) for i, batch in enumerate(batches)]
    results = await asyncio.gather(*tasks, return_exceptions=True)

    successful_count = sum(1 for i in results if i == True)

    log_info(
        f"Inserted {successful_count}/{len()}"
    )


if __name__ == "__main__":
    asyncio.run(main())