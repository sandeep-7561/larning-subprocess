# ----------------- this all are demo code -------------------
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Friday")

@mcp.tool
def hello(name: str):
    return f"Hello {name}"

mcp.run()


# ------------------- await -------------------
async def weather():

    data = await client.get(...)

    return data

