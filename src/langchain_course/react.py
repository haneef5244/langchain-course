# Holds all reasoning logic that will be used in graph
from dotenv import load_dotenv
from langchain_core.tools import tool
from langchain_ollama import ChatOllama
from langchain_tavily import TavilySearch
from datetime import date

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

@tool
def get_current_date() -> date:
  """
    Returns the current date.
    Returns:
      The current date.
  """
  return date.today()

tools = [TavilySearch(max_results=100), triple, get_current_date]

llm = ChatOllama(model="richardyoung/qwen2.5-14b-instruct-abliterated", temperature=0.3).bind_tools(tools)