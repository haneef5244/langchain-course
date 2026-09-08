from asyncio import tools

from dotenv import load_dotenv

load_dotenv()

# need to give tools and llm to create_agent
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_ollama import ChatOllama

from langchain_tavily import TavilySearch

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

    llm = ChatOllama(model="qwen2.5",temperature=1)

    tools = [TavilySearch()]

    agent = create_agent(model=llm, tools=tools)

    result = agent.invoke({ "messages": HumanMessage(content="What is the weather in Seksen 6, Kota Damansara, Malaysia?")})
    print(result)

if __name__ == "__main__":
    main()