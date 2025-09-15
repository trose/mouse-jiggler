#!/usr/bin/env python3
"""
Demo script showing how to integrate notifications with the mouse jiggler.
This demonstrates how Qoder can use both the jigglypuff MCP and the notification MCP together.
"""

import subprocess
import time
import sys

def send_notification(title, message, sound_name="Ping"):
    """Send a notification using the macOS Notification MCP."""
    try:
        cmd = [
            "/Users/trose/src/macos-notification-mcp/venv/bin/macos-notification-mcp",
            "banner-notification",
            "--title", title,
            "--message", message,
            "--sound", "true",
            "--sound-name", sound_name
        ]
        subprocess.run(cmd, timeout=5)
        return True
    except Exception as e:
        print(f"Failed to send notification: {e}")
        return False

def start_jiggling(interval=30, offset=1):
    """Start the mouse jiggler and notify the user."""
    try:
        # Start the jiggler process
        jiggler_process = subprocess.Popen([
            "bash", 
            "/Users/trose/src/mouse-jiggler/jiggly_puff.sh", 
            str(interval), 
            str(offset)
        ])
        
        # Send notification
        send_notification(
            "Mouse Jiggler Started", 
            f"Jiggling every {interval} seconds with {offset}px movement",
            "Submarine"
        )
        
        return jiggler_process
    except Exception as e:
        print(f"Failed to start jiggler: {e}")
        return None

def stop_jiggling(jiggler_process):
    """Stop the mouse jiggler and notify the user."""
    try:
        if jiggler_process:
            jiggler_process.terminate()
            jiggler_process.wait(timeout=5)
            
            # Send notification
            send_notification(
                "Mouse Jiggler Stopped", 
                "System will now be allowed to sleep",
                "Purr"
            )
            
        return True
    except Exception as e:
        print(f"Failed to stop jiggler: {e}")
        return False

def main():
    """Demo the integration."""
    print("Demo: Integrating Mouse Jiggler with Notifications")
    print("=" * 50)
    
    # Start jiggling
    print("Starting mouse jiggler...")
    jiggler = start_jiggling(interval=10, offset=1)
    
    if jiggler:
        print("Mouse jiggler started successfully!")
        print("You should have received a notification.")
        print("The mouse will jiggle every 10 seconds.")
        print()
        print("Waiting 30 seconds...")
        
        # Wait for a bit
        time.sleep(30)
        
        # Stop jiggling
        print("Stopping mouse jiggler...")
        stop_jiggling(jiggler)
        
        print("Mouse jiggler stopped!")
        print("You should have received another notification.")
    else:
        print("Failed to start mouse jiggler.")
        return 1
    
    print("=" * 50)
    print("Demo completed successfully!")
    print("In Qoder, you can use these same notification tools")
    print("to alert yourself when the AI needs your attention.")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())