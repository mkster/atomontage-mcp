# MCP Server Setup

This is a prototype of a simple MCP (Message Control Protocol) server that provides tools for Atomontage

## Prerequisites

1. Python 3.7 or higher
   - Download Python from [python.org](https://www.python.org/downloads/)
   - During installation, make sure to check "Add Python to PATH"

2. Pip (Python package manager)
   - Pip usually comes with Python. To verify, run:
   ```bash
   pip --version
   ```
   - If pip is not installed, download [get-pip.py](https://bootstrap.pypa.io/get-pip.py) and run:
   ```bash
   python get-pip.py
   ```

3. UV package manager - Install with:
```bash
pip install uv
```

4. Required Python packages - Install with:
```bash
uv pip install mcp-core fastapi uvicorn
```

5. In server.py replace `filepath` with your own created file

6. In atomomtage `Data\Studio\Script\ae\bootstrap.lua` add the bottom dofile your lua file that you creted for `filepath` `dofile('ae/mcpTest.lua')`


## Running the Server

### Option 1: Using VS Code
1. Open the project in VS Code
2. Press `Ctrl+Shift+B` (Windows/Linux) or `Cmd+Shift+B` (Mac) to run the default build task
   - Alternatively, press `F1` or `Ctrl+Shift+P`, type "Run Task", and select "Start MCP Server"
3. The server will start in a new terminal window

### Option 2: Using Terminal
1. Start the server using the following command in your terminal:
```bash
uv run mcp run .\server.py
```

## Connecting to Cursor

1. Open Cursor
2. Go to Settings
3. Under "MCP Server", enter the following URL:
```
http://localhost:8000/sse
```

## Important Notes

- Make sure to replace the server filepath in your settings with the actual path to your `server.py` file
- The server must be running for the MCP tools to work in Cursor
- The server runs on port 8000 by default. If this port is already in use, you'll need to stop any processes using it first

## Troubleshooting

If you get an error about port 8000 being in use:

1. Find the process using port 8000:
```bash
netstat -ano | findstr :8000
```

2. Stop the process (replace PID with the process ID from step 1):
```bash
taskkill /F /PID <PID>
```
