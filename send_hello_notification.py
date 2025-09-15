#!/usr/bin/env python3
"""
Send a Hello World notification using the macOS Notification MCP server.
"""

import subprocess
import sys

def send_hello_notification():
    """Send a Hello World notification."""
    try:
        # Send a banner notification
        cmd = [
            "/Users/trose/src/macos-notification-mcp/venv/bin/macos-notification-mcp",
            "banner-notification",
            "--title", "Hello World",
            "--message", "This is a test notification from the MCP server!",
            "--subtitle", "macOS Notification MCP",
            "--sound", "true",
            "--sound-name", "Ping"
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
        if result.returncode == 0:
            print("✓ Hello World notification sent successfully!")
            return True
        else:
            print(f"✗ Failed to send notification: {result.stderr}")
            return False
    except Exception as e:
        print(f"✗ Failed to send notification with exception: {e}")
        return False

def main():
    """Main function."""
    print("Sending Hello World notification...")
    success = send_hello_notification()
    
    if success:
        print("🎉 Notification sent! You should see a banner notification on your Mac.")
        return 0
    else:
        print("❌ Failed to send notification.")
        return 1

if __name__ == "__main__":
    sys.exit(main())