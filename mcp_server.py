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
        result = f"jigglypuff is already jiggling with PID {jiggler_process.pid}"
        return result
    
    try:
        # Get the directory of this script
        script_dir = os.path.dirname(os.path.abspath(__file__))
        script_path = os.path.join(script_dir, "jiggly_puff.sh")
        
        # Start the jiggler process
        jiggler_process = subprocess.Popen(["bash", script_path, str(interval), str(offset)])
        logger.info(f"jigglypuff started jiggling with PID {jiggler_process.pid}")
        
        result = f"jigglypuff started jiggling successfully with PID {jiggler_process.pid}, interval={interval}s, offset={offset}px"
        return result
        
    except Exception as e:
        logger.error(f"Failed to wake up jigglypuff: {e}")
        error_msg = f"Error waking up jigglypuff: {e}"
        return error_msg

@mcp.tool()
def put_jiggly_to_sleep() -> str:
    """Put jigglypuff to sleep to stop jiggling the cursor."""
    global jiggler_process
    
    # Check if running
    if not jiggler_process or jiggler_process.poll() is not None:
        result = "jigglypuff is already sleeping"
        return result
    
    try:
        # Terminate the process
        jiggler_process.terminate()
        jiggler_process.wait(timeout=5)  # Wait up to 5 seconds
        pid = jiggler_process.pid
        jiggler_process = None
        
        logger.info(f"jigglypuff with PID {pid} put to sleep")
        result = f"jigglypuff with PID {pid} put to sleep successfully"
        return result
        
    except subprocess.TimeoutExpired:
        # Force kill if not responding
        jiggler_process.kill()
        jiggler_process.wait()
        pid = jiggler_process.pid
        jiggler_process = None
        
        logger.warning(f"jigglypuff with PID {pid} force put to sleep")
        result = f"jigglypuff with PID {pid} force put to sleep"
        return result
    
    except Exception as e:
        logger.error(f"Error putting jigglypuff to sleep: {e}")
        error_msg = f"Error putting jigglypuff to sleep: {e}"
        return error_msg

@mcp.tool()
def check_jiggly_status() -> str:
    """Check the current status of jigglypuff."""
    global jiggler_process
    
    if not jiggler_process:
        result = "jigglypuff is sleeping (no process)"
        return result
    
    if jiggler_process.poll() is None:
        result = f"jigglypuff is jiggling with PID {jiggler_process.pid}"
        return result
    else:
        result = f"jigglypuff is sleeping (process exited with code {jiggler_process.returncode})"
        return result

# New tools for rule compliance
@mcp.tool()
def enable_jiggling_before_tasks() -> str:
    """ALWAYS use jigglypuff MCP to enable jiggling before beginning tasks.
    
    This tool implements the rule: ALWAYS use jigglypuff MCP enable jiggling before beginning tasks.
    """
    logger.info("Enabling jiggling before tasks as per rules")
    result = wake_up_jiggly()
    return result

@mcp.tool()
def disable_jiggling_after_tasks() -> str:
    """ALWAYS disable jiggling when task complete.
    
    This tool implements the rule: ALWAYS disable jiggling when task complete.
    """
    logger.info("Disabling jiggling after tasks as per rules")
    result = put_jiggly_to_sleep()
    return result

# Add prompts for user interaction
@mcp.prompt()
def jigglypuff_help() -> str:
    """Get help and guidance for using jigglypuff effectively.
    
    This prompt provides comprehensive guidance on how to use jigglypuff
    for different scenarios and best practices.
    """
    return """# jigglypuff Usage Guide

## What is jigglypuff?
jigglypuff is an AI-controlled mouse activity manager that prevents screen savers and system sleep during AI processing tasks by making imperceptible cursor movements.

## When to Use jigglypuff
- **Before starting AI tasks**: Always enable jiggling before beginning long-running AI operations
- **During code generation**: Keep your system awake while AI agents write code
- **During file processing**: Prevent sleep during large file operations
- **During API calls**: Maintain system activity during network operations

## Best Practices
1. **Enable before tasks**: Use `enable_jiggling_before_tasks()` at the start of AI operations
2. **Disable after completion**: Use `disable_jiggling_after_tasks()` when tasks finish
3. **Check status**: Use `check_jiggly_status()` to verify current state
4. **Custom settings**: Use `wake_up_jiggly(interval, offset)` for specific needs

## Tool Overview
- `wake_up_jiggly(interval, offset)`: Start jiggling with custom settings
- `put_jiggly_to_sleep()`: Stop jiggling immediately
- `check_jiggly_status()`: Check if jiggling is active
- `enable_jiggling_before_tasks()`: Rule-compliant task start
- `disable_jiggling_after_tasks()`: Rule-compliant task end

## Configuration Tips
- **Interval**: 30 seconds (default) works well for most tasks
- **Offset**: 1 pixel (default) is imperceptible but effective
- **Energy saving**: jigglypuff allows system sleep when not actively jiggling

Remember: jigglypuff is designed to work seamlessly with AI agents like Qoder and Claude Desktop!"""

@mcp.prompt()
def jigglypuff_troubleshooting() -> str:
    """Get troubleshooting help for common jigglypuff issues.
    
    This prompt provides solutions for common problems users might encounter.
    """
    return """# jigglypuff Troubleshooting Guide

## Common Issues and Solutions

### "jigglypuff is already jiggling"
- **Cause**: Another jiggling process is already running
- **Solution**: Use `check_jiggly_status()` to verify, then `put_jiggly_to_sleep()` if needed

### "Failed to wake up jigglypuff"
- **Cause**: Missing dependencies or permissions
- **Solutions**:
  1. Ensure `cliclick` is installed: `brew install cliclick`
  2. Check accessibility permissions in System Preferences
  3. Verify the `jiggly_puff.sh` script exists and is executable

### "jigglypuff is sleeping (process exited)"
- **Cause**: The jiggling process stopped unexpectedly
- **Solution**: Simply call `wake_up_jiggly()` to restart


### High CPU usage
- **Cause**: Very short interval settings
- **Solution**: Use longer intervals (30+ seconds) for better efficiency

## System Requirements
- macOS 10.15+ (Catalina or later)
- Homebrew package manager
- Python 3.11+
- cliclick CLI tool
- Accessibility permissions for Terminal

## Getting Help
If issues persist, check the logs in your terminal or contact the maintainer."""

# Add resources for context data management
@mcp.resource("jigglypuff-config")
def get_jigglypuff_config() -> str:
    """Get the current jigglypuff configuration and status.
    
    This resource provides access to the current configuration state
    and system information for jigglypuff.
    """
    global jiggler_process
    
    config = {
        "server_name": "jigglypuff",
        "version": "1.0.0",
        "status": "unknown",
        "process_id": None,
        "default_interval": 30,
        "default_offset": 1,
        "max_interval": 300,
        "min_interval": 5,
        "max_offset": 10,
        "min_offset": 1,
        "platform": "macOS",
        "dependencies": ["cliclick", "bash", "osascript"]
    }
    
    if jiggler_process:
        if jiggler_process.poll() is None:
            config["status"] = "jiggling"
            config["process_id"] = jiggler_process.pid
        else:
            config["status"] = "stopped"
            config["exit_code"] = jiggler_process.returncode
    else:
        config["status"] = "sleeping"
    
    import json
    return json.dumps(config, indent=2)

@mcp.resource("jigglypuff-rules")
def get_jigglypuff_rules() -> str:
    """Get the jigglypuff usage rules and best practices.
    
    This resource provides the official rules and guidelines
    for using jigglypuff with AI agents.
    """
    rules = {
        "primary_rules": [
            "ALWAYS use jigglypuff MCP to enable jiggling before beginning tasks",
            "ALWAYS disable jiggling when task complete"
        ],
        "secondary_rules": [
            "Check jiggly status before starting new tasks",
            "Use appropriate interval settings for task duration"
        ],
        "best_practices": [
            "Start with default settings (30s interval, 1px offset)",
            "Monitor system performance with custom intervals",
            "Use rule-compliant tools for automated workflows",
            "Check status regularly during long-running tasks"
        ],
        "compliance_tools": [
            "enable_jiggling_before_tasks()",
            "disable_jiggling_after_tasks()"
        ]
    }
    
    import json
    return json.dumps(rules, indent=2)

# Log the tools, prompts, and resources that were registered
logger.info("Tools, prompts, and resources registered successfully")

if __name__ == "__main__":
    mcp.run(transport='stdio')