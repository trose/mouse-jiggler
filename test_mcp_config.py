#!/usr/bin/env python3
"""
Test script to verify MCP configuration for jigglypuff.
"""

import json
import os
import sys

def validate_mcp_config():
    """Validate the MCP configuration file structure."""
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
        
        print("✅ MCP configuration validation passed!")
        print(f"   Command: {jigglypuff_config['command']}")
        print(f"   Args: {jigglypuff_config['args']}")
        print(f"   Working Directory: {jigglypuff_config['cwd']}")
        
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
    success = validate_mcp_config()
    sys.exit(0 if success else 1)