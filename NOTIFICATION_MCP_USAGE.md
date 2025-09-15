# macOS Notification MCP Usage Guide

This guide explains how to use the macOS Notification MCP server with Qoder to receive notifications when Qoder needs your attention.

## Overview

The macOS Notification MCP server provides Qoder with the ability to send various types of notifications to your macOS system:

1. **Sound Notifications** - Play system sounds like "Ping", "Submarine", etc.
2. **Banner Notifications** - Display visual notifications in the macOS Notification Center
3. **Speech Notifications** - Convert text to speech using macOS built-in voices
4. **Voice Management** - List available system voices
5. **System Testing** - Diagnostic tool to verify all notification methods

## Available Tools

### 1. Sound Notification
```python
sound_notification(sound_name="Submarine")
```
Available sounds: Basso, Blow, Bottle, Frog, Funk, Glass, Hero, Morse, Ping, Pop, Purr, Sosumi, Submarine, Tink

### 2. Banner Notification
```python
banner_notification(
    title="Task Complete",
    message="Your analysis is ready",
    subtitle=None,      # Optional
    sound=False,        # Optional: Play sound with notification
    sound_name=None     # Optional: Specify system sound
)
```

### 3. Speech Notification
```python
speak_notification(
    text="The process has completed",
    voice=None,         # Optional: System voice to use
    rate=150,           # Optional: Words per minute (default: 150)
    volume=1.0          # Optional: Volume level 0.0-1.0
)
```

### 4. Voice Management
```python
list_available_voices()  # Lists all available text-to-speech voices
```

### 5. System Testing
```python
test_notification_system()  # Tests all notification methods
```

## Usage Examples in Qoder

When working with Qoder, you can call these tools directly:

1. **Get Attention with Sound**:
   ```
   sound_notification(sound_name="Ping")
   ```

2. **Show Important Notification**:
   ```
   banner_notification(
       title="Qoder Needs Input",
       message="Please review the code changes",
       subtitle="Code Review Request",
       sound=True,
       sound_name="Ping"
   )
   ```

3. **Speak a Message**:
   ```
   speak_notification(
       text="Qoder needs your attention for an important task",
       rate=175,
       volume=0.8
   )
   ```

## Configuration

The MCP server is configured in your Qoder configuration file:
```json
"macos-notification": {
  "command": "/Users/trose/src/macos-notification-mcp/venv/bin/macos-notification-mcp",
  "args": [],
  "cwd": "/Users/trose/src/macos-notification-mcp"
}
```

## Troubleshooting

1. **Permissions**: Ensure notifications are allowed in System Settings → Notifications
2. **Restart Qoder**: After configuration changes, restart Qoder to load the new MCP server
3. **Test Functionality**: Use the `test_notification_system()` tool to verify all notification methods work

## Implementation Details

- **Rate Limiting**: Notifications are processed one at a time with a minimum interval of 0.5 seconds
- **Queuing**: Multiple notification requests are handled sequentially
- **OS Integration**: Uses native macOS commands (afplay, osascript, say)
- **FastMCP**: Built on the FastMCP framework for AI communication