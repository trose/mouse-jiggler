#!/usr/bin/env python3
# mcp_server.py

import os
import subprocess
import logging
from typing import Optional
from mcp.server.fastmcp import FastMCP

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize MCP server
mcp = FastMCP("jigglypuff")

# Log the tools that are being registered
logger.info("Registering tools...")

# Global process reference
jiggler_process: Optional[subprocess.Popen] = None

@mcp.tool()
def wake_up_jiggly(interval: int = 30, offset: int = 1) -> str:
    """Wake up jigglypuff to start jiggling the cursor.
    
    Args:
        interval: Time between jiggles in seconds (default: 30, min: 5, max: 300)
        offset: Mouse movement offset in pixels (default: 1, min: 1, max: 10)
    """
    global jiggler_process
    
    # Validate parameters
    interval = max(5, min(300, interval))  # Clamp between 5-300
    offset = max(1, min(10, offset))        # Clamp between 1-10
    
    # Check if already running
    if jiggler_process and jiggler_process.poll() is None:
        return f"jigglypuff is already jiggling with PID {jiggler_process.pid}"
    
    try:
        # Get the directory of this script
        script_dir = os.path.dirname(os.path.abspath(__file__))
        script_path = os.path.join(script_dir, "jiggly_puff.sh")
        
        # Start the jiggler process
        jiggler_process = subprocess.Popen(["bash", script_path, str(interval), str(offset)])
        logger.info(f"jigglypuff started jiggling with PID {jiggler_process.pid}")
        
        return f"jigglypuff started jiggling successfully with PID {jiggler_process.pid}, interval={interval}s, offset={offset}px"
        
    except Exception as e:
        logger.error(f"Failed to wake up jigglypuff: {e}")
        return f"Error waking up jigglypuff: {e}"

@mcp.tool()
def put_jiggly_to_sleep() -> str:
    """Put jigglypuff to sleep to stop jiggling the cursor."""
    global jiggler_process
    
    # Check if running
    if not jiggler_process or jiggler_process.poll() is not None:
        return "jigglypuff is already sleeping"
    
    try:
        # Terminate the process
        jiggler_process.terminate()
        jiggler_process.wait(timeout=5)  # Wait up to 5 seconds
        pid = jiggler_process.pid
        jiggler_process = None
        
        logger.info(f"jigglypuff with PID {pid} put to sleep")
        return f"jigglypuff with PID {pid} put to sleep successfully"
        
    except subprocess.TimeoutExpired:
        # Force kill if not responding
        jiggler_process.kill()
        jiggler_process.wait()
        pid = jiggler_process.pid
        jiggler_process = None
        
        logger.warning(f"jigglypuff with PID {pid} force put to sleep")
        return f"jigglypuff with PID {pid} force put to sleep"
    
    except Exception as e:
        logger.error(f"Error putting jigglypuff to sleep: {e}")
        return f"Error putting jigglypuff to sleep: {e}"

@mcp.tool()
def check_jiggly_status() -> str:
    """Check the current status of jigglypuff."""
    global jiggler_process
    
    if not jiggler_process:
        return "jigglypuff is sleeping (no process)"
    
    if jiggler_process.poll() is None:
        return f"jigglypuff is jiggling with PID {jiggler_process.pid}"
    else:
        return f"jigglypuff is sleeping (process exited with code {jiggler_process.returncode})"

# New tools for rule compliance
@mcp.tool()
def enable_jiggling_before_tasks() -> str:
    """ALWAYS use jigglypuff MCP to enable jiggling before beginning tasks.
    
    This tool implements the rule: ALWAYS use jigglypuff MCP enable jiggling before beginning tasks.
    """
    logger.info("Enabling jiggling before tasks as per rules")
    return wake_up_jiggly()

@mcp.tool()
def disable_jiggling_after_tasks() -> str:
    """ALWAYS disable jiggling when task complete.
    
    This tool implements the rule: ALWAYS disable jiggling when task complete.
    """
    logger.info("Disabling jiggling after tasks as per rules")
    return put_jiggly_to_sleep()

# Log the tools that were registered
logger.info("Tools registered successfully")

if __name__ == "__main__":
    mcp.run(transport='stdio')