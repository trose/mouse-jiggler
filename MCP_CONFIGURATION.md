# MCP Configuration Guide for jigglypuff

This guide provides detailed instructions for configuring jigglypuff with various MCP-compatible clients.

## Table of Contents
- [Qoder Configuration](#qoder-configuration)
- [Claude Desktop Configuration](#claude-desktop-configuration)
- [Generic MCP Client Configuration](#generic-mcp-client-configuration)
- [Testing the Configuration](#testing-the-configuration)

## Qoder Configuration

To register jigglypuff with Qoder, you need to update your global MCP configuration file.

### 1. Locate the Configuration File

The Qoder MCP configuration file is typically located at:
```
~/.config/qoder/mcp.json
```

On macOS, this would be:
```
/Users/your-username/.config/qoder/mcp.json
```

### 2. Update the Configuration

Add the jigglypuff server configuration to the `mcpServers` section of your `mcp.json` file:

```json
{
  "mcpServers": {
    "jigglypuff": {
      "command": "/Users/trose/src/mouse-jiggler/venv/bin/python",
      "args": ["mcp_server.py"],
      "cwd": "/Users/trose/src/mouse-jiggler"
    }
  }
}
```

**Important**: Make sure to:
1. Update the paths to match your actual installation directory
2. Ensure the virtual environment is properly set up with all dependencies installed

### 3. Enable Automatic Rules (Optional)

To enable the automatic jiggling rules, add the following to your Qoder configuration:

```json
{
  "jigglypuffRules": {
    "enableOnTaskStart": true,
    "disableOnTaskComplete": true
  }
}
```

### 4. Restart Qoder

After updating the configuration, restart Qoder to load the new MCP server.

## Claude Desktop Configuration

To configure jigglypuff with Claude Desktop, add the following to your configuration file:

Location: `~/Library/Application Support/Claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "jigglypuff": {
      "command": "/Users/trose/src/mouse-jiggler/venv/bin/python",
      "args": ["mcp_server.py"]
    }
  }
}
```

**Important**: Update the paths to point to the actual location of your installation.

## Generic MCP Client Configuration

For other MCP clients, you'll need to follow their specific documentation for adding MCP servers. The general configuration parameters are:

- **Command**: Full path to Python interpreter in virtual environment
- **Arguments**: Path to the `mcp_server.py` file
- **Working Directory**: The directory where jigglypuff is installed
- **Transport**: stdio (standard input/output)

Example configuration:
```json
{
  "mcpServers": {
    "jigglypuff": {
      "command": "/Users/trose/src/mouse-jiggler/venv/bin/python",
      "args": ["mcp_server.py"],
      "cwd": "/Users/trose/src/mouse-jiggler"
    }
  }
}
```

## Testing the Configuration

After configuring your MCP client, you can test the connection by:

1. Starting your MCP client (Qoder, Claude Desktop, etc.)
2. Calling the `check_jiggly_status` tool
3. Verifying that the tool returns "jigglypuff is sleeping (no process)"

You can also test the full functionality by:
1. Calling the `wake_up_jiggly` tool
2. Checking the status with `check_jiggly_status` (should show "jiggling")
3. Calling the `put_jiggly_to_sleep` tool
4. Checking the status again (should show "sleeping")

If you encounter any issues:
1. Verify that the paths in your configuration are correct
2. Ensure that Python and all dependencies are properly installed in the virtual environment
3. Check that accessibility permissions are granted for your terminal application
4. Confirm that the jigglypuff virtual environment is set up correctly