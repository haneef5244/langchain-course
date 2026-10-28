from dotenv import load_dotenv
import asyncio

load_dotenv()

from langchain.agents import create_agent
from langchain.mcp import MCPAdapter

async def main() -> None:
    print("Hello from langchain-course!")

    async with MCPAdapter("http://127.0.0.1:8000") as weather_adapter, \
                MCPAdapter("[python]", "/Users/mhaneefhamzah/POC/langchain-course/servers/math_server.py") as math_adapter:

        # pull the dynamically exposed tools from both servers
        weather_tools = await weather_adapter.list_tools()
        math_tools = await math_adapter.list_tools()

        # Combine them into 1 Langchain tool list
        all_tools = weather_tools + math_tools

        agent = create_agent("", all_tools)

        response = agent.invoke({
            "messages": [
                {
                    "role": "user",
                    "content": "What is 20+30, and whats the weather like in Kuala Lumpur?"
                }
            ]
        })

        print(response[-1]["content"])

if __name__ == "__main__":
    asyncio.run(main())