from typing import List

from pydantic import BaseModel, Field

from dotenv import load_dotenv

load_dotenv()

# need to give tools and llm to create_agent
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
# from langchain_ollama import ChatOllama
from langchain_groq import ChatGroq
from langchain_tavily import TavilySearch

class Source(BaseModel):
    """Schema for a source used by the agent"""

    url:str = Field(description="The URL of the source")

class AgentResponse(BaseModel):
    """Schema for agent response  with answer and sources"""

    answer:str = Field(description="Agent's answer to the query")
    sources:List[Source] = Field(default_factory=list, description="List of sources to the answer")

# Custom Tool for searching over the internet using Tavily API
# from tavily import TavilyClient

# tavily_client = TavilyClient()

# @tool
# def search(query: str) -> str:
#     """
#     Tool that searches over the internet
    
#     Args:
#         query: The query to search for

#     Returns:
#         The search result
#     """
#     print(f"Searching for {query}")
#     response = tavily_client.search(query)
#     return response

def main() -> None:
    print("Hello from langchain-course!")

    llm = ChatGroq(model="qwen/qwen3.8-27b",temperature=0.3)
    tools = [TavilySearch()]

    agent = create_agent(model=llm, tools=tools, response_format=AgentResponse)

    result = agent.invoke({ "messages": HumanMessage(content="What is the weather in Kota Damansara, Malaysia?")}) 
    print(result)

if __name__ == "__main__":
    main()