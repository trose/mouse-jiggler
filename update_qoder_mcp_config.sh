#!/bin/bash
# Script to update Qoder's MCP configuration to include macOS notification MCP server

CONFIG_FILE="$HOME/Library/Application Support/Qoder/SharedClientCache/mcp.json"

# Check if the config file exists
if [ ! -f "$CONFIG_FILE" ]; then
    echo "Error: Qoder MCP configuration file not found at $CONFIG_FILE"
    exit 1
fi

# Create a backup of the original config
cp "$CONFIG_FILE" "$CONFIG_FILE.backup.$(date +%s)"
echo "Backup created at $CONFIG_FILE.backup.$(date +%s)"

# Check if macos-notification server is already configured
if grep -q '"macos-notification"' "$CONFIG_FILE"; then
    echo "macos-notification MCP server is already configured in Qoder"
    exit 0
fi

# Add the macos-notification MCP server configuration
# Find the position of the closing brace for the mcpServers object and insert our config before it
# This approach finds the last "}" that closes the mcpServers object
sed -i '' '/^[[:space:]]*}[[:space:]]*$/ {
    $!{
        N
        /\n[[:space:]]*}/!{
            P
            D
        }
        s/\n[[:space:]]*}[[:space:]]*$/,\n    "macos-notification": {\n      "command": "\/Users\/trose\/src\/mouse-jiggler\/venv\/bin\/macos-notification-mcp",\n      "args": [],\n      "cwd": "\/Users\/trose\/src\/mouse-jiggler"\n    }\n  }/
    }
}' "$CONFIG_FILE"

echo "Successfully added macos-notification MCP server to Qoder configuration"
echo "Please restart Qoder for the changes to take effect"