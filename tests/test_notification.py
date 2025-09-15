#!/usr/bin/env python3
"""
Test script to verify that the macOS Notification MCP is working correctly.
This script demonstrates how to use the notification tools that will be available in Qoder.
"""

import subprocess
import sys
import os

def test_banner_notification():
    """Test the banner notification functionality."""
    try:
        # Test banner notification
        cmd = [
            "/Users/trose/src/macos-notification-mcp/venv/bin/macos-notification-mcp",
            "banner-notification",
            "--title", "Test Notification",
            "--message", "This is a test notification from jigglypuff!",
            "--subtitle", "macOS Notification MCP Test"
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
        if result.returncode == 0:
            print("✓ Banner notification test passed")
            return True
        else:
            print(f"✗ Banner notification test failed: {result.stderr}")
            return False
    except Exception as e:
        print(f"✗ Banner notification test failed with exception: {e}")
        return False

def test_sound_notification():
    """Test the sound notification functionality."""
    try:
        # Test sound notification
        cmd = [
            "/Users/trose/src/macos-notification-mcp/venv/bin/macos-notification-mcp",
            "sound-notification",
            "--sound-name", "Ping"
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
        if result.returncode == 0:
            print("✓ Sound notification test passed")
            return True
        else:
            print(f"✗ Sound notification test failed: {result.stderr}")
            return False
    except Exception as e:
        print(f"✗ Sound notification test failed with exception: {e}")
        return False

def main():
    """Run all tests."""
    print("Testing macOS Notification MCP functionality...")
    print("=" * 50)
    
    tests = [
        test_banner_notification,
        test_sound_notification
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
    
    print("=" * 50)
    print(f"Tests passed: {passed}/{total}")
    
    if passed == total:
        print("🎉 All tests passed! The macOS Notification MCP is working correctly.")
        return 0
    else:
        print("❌ Some tests failed. Please check the configuration.")
        return 1

if __name__ == "__main__":
    sys.exit(main())