# weather_server.py
from fastmcp import FastMCP

mcp = FastMCP("Weather")

@mcp.tool
async def get_weather(location: str) -> str:
    """Get weather based on location"""
    return f"The weather in {location} is not very hot"

if __name__ == "__main__":
    mcp.run(transport="sse")