from fastmcp import FastMCP #mcp sersver
from dotenv import load_dotenv #reading dote env file
from starlette.middleware.cors import CORSMiddleware #allow to handel api key
from starlette.middleware import Middleware 

load_dotenv()

mcp = FastMCP(name='Notes APP')

@mcp.tool()
def get_my_notes() -> str:
    """Get all notes for a user"""
    return "no notes"

@mcp.tool()
def add_note(content:str) -> str:
    """Add a note for a user"""
    return f"added note: {content}"

if __name__ == "__main__":
    mcp.run(
        transport = "http", # / stdio for communication terminal 
        host='127.0.0.1', # / host="0.0.0.0" for wifi connections
        port =8000, 
        middleware=[
            Middleware(
                CORSMiddleware,
                allow_origins=["*"], #allow  all { localhost,127.0.0.1,abc.com,xyz.com}
                allow_credentials=True, #Credentials {Cookies,Login Session,Authorization}
                allow_methods=["*"], #HTTP methods {GET,,POST,PUT,DELETE,PATCH}
                allow_headers=["*"] #Headers {Authorization,Content-Type,Bearer Token,API-Key}
            )
        ]
    )