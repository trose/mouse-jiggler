#!/usr/bin/env python3
import json
import subprocess
import sys
import time

def test_mcp_server():
    # Start the MCP server
    server_process = subprocess.Popen(
        [sys.executable, 'mcp_server.py'],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        bufsize=1
    )
    
    try:
        # Send the initialization request
        init_request = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "initialize",
            "params": {
                "protocolVersion": "2024-01-01",
                "capabilities": {},
                "clientInfo": {
                    "name": "test-client",
                    "version": "1.0.0"
                }
            }
        }
        
        server_process.stdin.write(json.dumps(init_request) + '\n')
        server_process.stdin.flush()
        
        # Read the response
        response_line = server_process.stdout.readline()
        print("Initialization response:", response_line)
        
        # Parse the response
        try:
            response = json.loads(response_line)
            if "result" in response:
                print("Server initialized successfully")
            else:
                print("Server initialization failed:", response)
                return False
        except json.JSONDecodeError:
            print("Failed to parse response as JSON:", response_line)
            return False
        
        # Send tools list request (correct format)
        tools_request = {
            "jsonrpc": "2.0",
            "id": 2,
            "method": "tools/list"
        }
        
        server_process.stdin.write(json.dumps(tools_request) + '\n')
        server_process.stdin.flush()
        
        # Read the response
        response_line = server_process.stdout.readline()
        print("Tools list response:", response_line)
        
        # Parse the response
        try:
            response = json.loads(response_line)
            if "result" in response and "tools" in response["result"]:
                print("Tools list retrieved successfully")
                for tool in response["result"]["tools"]:
                    print(f"  - {tool['name']}: {tool.get('description', 'No description')}")
            else:
                print("Failed to get tools list:", response)
        except json.JSONDecodeError:
            print("Failed to parse response as JSON:", response_line)
            
    finally:
        # Terminate the server
        server_process.terminate()
        server_process.wait()
    
    return True

if __name__ == "__main__":
    test_mcp_server()