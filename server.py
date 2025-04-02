from mcp.server.fastmcp import FastMCP
import os
import glob
from pathlib import Path

#uv run mcp run .\server.py
#in cursor/broweser http://localhost:8000/sse



# Create an MCP server
mcp = FastMCP("Atomontage MCP")
filepath = "D:\\atomontage\\Build\\win64_vs2022\\Studio\\RelWithDebInfo\\Data\\Studio\\Script\\ae\\mcpTest.lua"

#returns lua error on fail
@mcp.tool("runLuaInAtomontage", "Run lua code in Atomontage")
def run_lua_in_atomontage(lua_code: str) -> str:
    """Run lua code in Atomontage"""
    set_file_content(lua_code, filepath)
    return "success"

@mcp.tool("getServerHierarchy", "Get the server hierarchy")
def get_server_hierarchy_tool() -> str:
    """Get the server hierarchy"""
    filepath = "serverHierarchy.txt"
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        return f"Error reading file: {e}"
    
# @mcp.tool("getLogs", "Get the latest server log")
# def get_logs_tool() -> str:
#     """Get the latest server log"""
#     return get_latest_server_log()


def get_latest_server_log() -> str:
    """Gets the path of the most recent server log file.
    
    Returns:
        str: The content of the most recent server log file, or error message if no logs found
    """
    try:
        # Get the logs directory path
        logs_dir = Path("D:/atomontage/UserData/Logs")
        
        # Get all server log files
        server_logs = glob.glob(str(logs_dir / "Server*.log"))
        
        if not server_logs:
            return "No server log files found"
            
        # Get the most recent file based on modification time
        latest_log = max(server_logs, key=os.path.getmtime)
        
        # Read and return the content
        with open(latest_log, 'r', encoding='utf-8') as f:
            return f.read()
            
    except Exception as e:
        return f"Error reading log file: {e}"



# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!" 

# Add a resource to return server hierarchy
@mcp.resource("resource://serverHierarchy")
def get_server_hierarchy() -> str:
    """Get the server hierarchy"""

    print("get_server_hierarchy")
    with open("serverHierarchy.txt", "r", encoding="utf-8") as f:
        return f.read()



def set_file_content(content: str, filepath: str) -> bool:
    """Sets the content of a file to the provided string.
    
    Args:
        content: The string content to write to the file
        filepath: The path to the file to write to
        
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    except Exception as e:
        print(f"Error writing to file: {e}")
        return False


mcp.run("sse")