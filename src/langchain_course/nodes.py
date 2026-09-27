from dotenv import load_dotenv
from langgraph.graph import MessagesState
from langgraph.prebuilt import ToolNode
from langchain_course.react import llm, tools

load_dotenv()

SYSTEM_MESSAGE="""
You are a helpful assistant that can use the following tools to answer questions.
"""

# First node
def run_agent_reasoning(state: MessagesState) -> MessagesState:
    """
        Run the agent reasoning node.
    """
    response = llm.invoke([
        {
            "role": "system", 
            "content": SYSTEM_MESSAGE,
        },
        *state["messages"]
    ])
    # below returned response will be appended to the list of messages state by LangGraph
    return { "messages": [response]}

tool_node = ToolNode(tools=tools)