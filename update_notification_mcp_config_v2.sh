#!/bin/bash
# Script to update Qoder's MCP configuration with the correct macOS notification MCP path

CONFIG_FILE="$HOME/Library/Application Support/Qoder/SharedClientCache/mcp.json"

# Check if the config file exists
if [ ! -f "$CONFIG_FILE" ]; then
    echo "Error: Qoder MCP configuration file not found at $CONFIG_FILE"
    exit 1
fi

# Create a backup of the original config
cp "$CONFIG_FILE" "$CONFIG_FILE.backup.$(date +%s)"
echo "Backup created at $CONFIG_FILE.backup.$(date +%s)"

# Update the macos-notification MCP server configuration with the correct path
sed -i '' '/"macos-notification"/,/^    }/c\
    "macos-notification": {\
      "command": "/Users/trose/src/macos-notification-mcp/venv/bin/macos-notification-mcp",\
      "args": [],\
      "cwd": "/Users/trose/src/macos-notification-mcp"\
    }' "$CONFIG_FILE"

echo "Successfully updated macos-notification MCP server path in Qoder configuration"
echo "Please restart Qoder for the changes to take effect"