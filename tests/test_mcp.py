#!/usr/bin/env python3
import json
import subprocess
import time

# Start the MCP server
server_process = subprocess.Popen(
    ['python', 'mcp_server.py'],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True
)

# Send initialization request
init_request = {
    "jsonrpc": "2.0",
    "id": 1,
    "method": "initialize",
    "params": {
        "capabilities": {}
    }
}
server_process.stdin.write(json.dumps(init_request) + '\n')
server_process.stdin.flush()

# Read the response
response = server_process.stdout.readline()
print("Initialization response:", response)

# Send tools list request
tools_request = {
    "jsonrpc": "2.0",
    "id": 2,
    "method": "tools/list"
}
server_process.stdin.write(json.dumps(tools_request) + '\n')
server_process.stdin.flush()

# Read the response
response = server_process.stdout.readline()
print("Tools list response:", response)

# Terminate the server
server_process.terminate()