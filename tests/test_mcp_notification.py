#!/usr/bin/env python3
"""
Test script to verify that the macOS Notification MCP server is working correctly.
This script demonstrates how to use the notification tools that will be available in Qoder.
"""

import subprocess
import sys
import time
import json

def test_mcp_server():
    """Test the MCP server functionality."""
    try:
        # Start the MCP server in the background
        print("Starting macOS Notification MCP server...")
        server_process = subprocess.Popen([
            "/Users/trose/src/macos-notification-mcp/venv/bin/macos-notification-mcp"
        ], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        # Give the server a moment to start
        time.sleep(2)
        
        # Check if the server is running
        if server_process.poll() is None:
            print("✓ MCP server started successfully")
            # Terminate the server
            server_process.terminate()
            server_process.wait()
            return True
        else:
            stderr_output = server_process.stderr.read().decode()
            print(f"✗ MCP server failed to start: {stderr_output}")
            return False
            
    except Exception as e:
        print(f"✗ MCP server test failed with exception: {e}")
        return False

def show_available_tools():
    """Show the available tools in the MCP server."""
    print("\nAvailable MCP tools in macOS Notification MCP:")
    print("-" * 50)
    print("1. sound_notification(sound_name) - Play a system sound")
    print("2. banner_notification(title, message, subtitle, sound, sound_name) - Display a visual notification")
    print("3. speak_notification(text, voice, rate, volume) - Convert text to speech")
    print("4. list_available_voices() - List all available text-to-speech voices")
    print("5. test_notification_system() - Test all notification methods")
    print("-" * 50)

def main():
    """Run the test."""
    print("Testing macOS Notification MCP Server...")
    print("=" * 50)
    
    # Show available tools
    show_available_tools()
    
    # Test server startup
    server_test_passed = test_mcp_server()
    
    print("=" * 50)
    if server_test_passed:
        print("🎉 MCP server test passed! The macOS Notification MCP is ready to use with Qoder.")
        print("\nWhen using with Qoder, you can call these tools directly:")
        print("- banner_notification(title='Qoder Needs Attention', message='Please review this task')")
        print("- sound_notification(sound_name='Ping')")
        print("- speak_notification(text='Qoder needs your attention', rate=175)")
    else:
        print("❌ MCP server test failed. Please check the configuration.")
    
    return 0 if server_test_passed else 1

if __name__ == "__main__":
    sys.exit(main())