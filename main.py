from fastmcp import fastMCP #mcp sersver
from dotenv import load_dotenv #reading dote env file
from starlette.middleware.cors import CORSMiddleware #allow to handel api key
from starlette.middleware import Middleware 

load_dotenv()

mcp = fastMCP(name='Notes APP')

@mcp.tool()
def get_my_notes() -> str:
    """Get all notes for a user"""
    return "no notes"

@mcp.tool()
def add_note(content:str) -> str:
    """Add a note for a user"""
    return f"added note: {content}"

