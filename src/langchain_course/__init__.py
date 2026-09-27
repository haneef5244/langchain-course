import os

from dotenv import load_dotenv
load_dotenv()

from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from langchain.messages import ToolMessage
from langchain.tools import tool

from langchain_pinecone import PineconeVectorStore
from langchain_ollama import OllamaEmbeddings, ChatOllama
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain.messages import HumanMessage

from typing import Any, Dict

llm_model = ChatOllama(model="deepseek-r1:14b")
# llm_model = ChatGoogleGenerativeAI(model="gemini-3.8-flash")
embeddings = OllamaEmbeddings(model="qwen3-embedding:8b", dimensions=1536)
# embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-2", output_dimensionality=1536)




# content_and_artifact returns 2 values
@tool(response_format="content_and_artifact")
def retrieve_context(query: str): 
    """Retrieve relevant documentation to help answer user queries about LangChain."""

    vector_store = PineconeVectorStore(index_name=os.environ.get("INDEX_NAME"), embedding=embeddings)
    results = vector_store.as_retriever(search_kwargs={'k':5}).invoke(query)
    
    # Serialize documents for the model 
    serialized = "\n\n".join(
        (f"Source: {doc.metadata.get("source", "Unknown")}\n\nContent: {doc.page_content}")
        for doc in results
    )

    # Return both serialized content and raw documents
    return serialized, results

def run_llm(query: str) -> Dict[str, Any]:
    """
    Run the RAG pipeline to answer a query using retrieved documentation.

    Args:
        query: The user's question

    Returns:
        Dictionary containing:
            - answer: The generated answer
            - context: The list of retrieved documents
    """

    print(f"Query={query}")
    system_prompt = """
        You are a helpful AI assistant that answers questions about LangChain documentation.
        You have access to a tool that retrieves relevant documentation.
        You MUST use the tool to find relevant information before answering questions.
        Always cite the sources you use in our answers.
        If you cannot find the answer in the retrieved documentation, say so.
    """
    agent = create_agent(model=llm_model, tools=[retrieve_context], system_prompt=system_prompt)
    # result = agent.invoke({"messages": [{"role": "user", "content": "Summarize AI trends"}]})
    response = agent.invoke({"messages": [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": query}
    ]})
    print()
    print(response)
    answer = response["messages"][-1].content
    return answer

def main():
    run_llm("What is the latest LangChain function?")

if __name__ == "__main__":
    main()

    