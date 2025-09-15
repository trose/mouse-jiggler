#!/usr/bin/env python3
"""
Test script to validate the jigglypuff rule compliance tools.
"""

import sys
import os
import subprocess
import time

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(__file__))

def test_rule_compliance_tools():
    """Test that the rule compliance tools work correctly."""
    try:
        # Import the MCP server module
        import mcp_server
        
        # Test enable_jiggling_before_tasks
        print("Testing enable_jiggling_before_tasks...")
        result = mcp_server.enable_jiggling_before_tasks()
        print(f"Result: {result}")
        
        # Give it a moment to start
        time.sleep(1)
        
        # Check status
        status = mcp_server.check_jiggly_status()
        print(f"Status after enabling: {status}")
        assert "jiggling" in status, "Jiggling should be active after enabling"
        
        # Test disable_jiggling_after_tasks
        print("Testing disable_jiggling_after_tasks...")
        result = mcp_server.disable_jiggling_after_tasks()
        print(f"Result: {result}")
        
        # Check status again
        status = mcp_server.check_jiggly_status()
        print(f"Status after disabling: {status}")
        assert "sleeping" in status, "Jiggling should be inactive after disabling"
        
        print("✅ All rule compliance tests passed!")
        return True
        
    except Exception as e:
        print(f"❌ Rule compliance test failed: {e}")
        return False

if __name__ == "__main__":
    success = test_rule_compliance_tools()
    sys.exit(0 if success else 1)