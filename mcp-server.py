from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Friday")

@mcp.tool
def hello(name: str):
    return f"Hello {name}"

mcp.run()