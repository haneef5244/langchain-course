# Holds all reasoning logic that will be used in graph
from dotenv import load_dotenv
from langchain_core.tools import tool
from langchain_ollama import ChatOllama
from langchain_tavily import TavilySearch

load_dotenv()

@tool
def triple(num: float) -> float:
    """
        Returns the input number multiplied by 3

        Args:
            num: The float number to be multiplied by 3
        Returns:
            Number that is multiplied by 3
    """
    return float(num) * 3

tools = [TavilySearch(max_results=1), triple]

llm = ChatOllama(model="qwen3.5:9b", temperature=0.3).bind_tools(tools)