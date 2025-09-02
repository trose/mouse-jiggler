#!/usr/bin/env python3
"""
Test script to verify configuration paths for jigglypuff MCP.
"""

import json
import os
import sys

def validate_config_paths():
    """Validate that the paths in the MCP configuration are correct."""
    config_path = os.path.join(os.path.dirname(__file__), 'updated_mcp_config.json')
    
    try:
        with open(config_path, 'r') as f:
            config = json.load(f)
        
        # Check that mcpServers exists
        assert 'mcpServers' in config, "Configuration must have 'mcpServers' key"
        assert isinstance(config['mcpServers'], dict), "'mcpServers' must be a dictionary"
        
        # Check jigglypuff server configuration
        assert 'jigglypuff' in config['mcpServers'], "Configuration must include 'jigglypuff' server"
        
        jigglypuff_config = config['mcpServers']['jigglypuff']
        assert 'command' in jigglypuff_config, "jigglypuff config must have 'command'"
        assert 'args' in jigglypuff_config, "jigglypuff config must have 'args'"
        assert 'cwd' in jigglypuff_config, "jigglypuff config must have 'cwd'"
        
        # Check that the Python command path exists
        python_path = jigglypuff_config['command']
        assert os.path.exists(python_path), f"Python path does not exist: {python_path}"
        assert os.access(python_path, os.X_OK), f"Python path is not executable: {python_path}"
        
        # Check that the working directory exists
        cwd_path = jigglypuff_config['cwd']
        assert os.path.exists(cwd_path), f"Working directory does not exist: {cwd_path}"
        assert os.path.isdir(cwd_path), f"Working directory is not a directory: {cwd_path}"
        
        # Check that the server script exists in the working directory
        script_name = jigglypuff_config['args'][0]
        script_path = os.path.join(cwd_path, script_name)
        assert os.path.exists(script_path), f"Server script does not exist: {script_path}"
        
        print("✅ MCP configuration path validation passed!")
        print(f"   Python executable: {python_path}")
        print(f"   Working directory: {cwd_path}")
        print(f"   Server script: {script_path}")
        
        return True
        
    except FileNotFoundError:
        print(f"❌ Configuration file not found at {config_path}")
        return False
    except json.JSONDecodeError as e:
        print(f"❌ Invalid JSON in configuration file: {e}")
        return False
    except AssertionError as e:
        print(f"❌ Configuration validation failed: {e}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

if __name__ == "__main__":
    success = validate_config_paths()
    sys.exit(0 if success else 1)