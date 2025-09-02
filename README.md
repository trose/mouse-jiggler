# jigglypuff: AI-Controlled Mouse Activity Manager for macOS

**Prevent screen savers, system sleep, and keep your macOS awake during AI processing tasks.** jigglypuff is a lightweight mouse jiggler and activity manager that uses imperceptible cursor movements to simulate user activity. Perfect for developers using AI agents like Qoder and Claude Desktop.

**Keywords**: mouse jiggler, cursor mover, screen saver preventer, system wakefulness, AI automation, macOS automation, MCP tools, Model Context Protocol, keep screen awake, prevent sleep, automation tools, developer utilities

Version: 1.0.0

## Features

- **Prevents screen savers and system sleep** during AI processing tasks
- **Allows system to sleep** when waiting for user input to conserve energy
- **Controlled via MCP tools** for seamless integration with AI agents
- **Lightweight and efficient** implementation with minimal system impact
- **Small, imperceptible mouse movements** that won't interfere with your work
- **Automatic jiggling rules** - Automatically enables/disables jiggling based on task status
- **Cross-AI agent compatibility** - Works with Qoder, Claude Desktop, and other MCP-compatible tools

## Prerequisites

- macOS system (10.15+ recommended)
- Homebrew package manager
- Python 3.11+
- cliclick CLI tool for mouse automation
- MCP-compatible AI agent (Qoder, Claude Desktop, Cursor, etc.)

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/trose/jigglypuff.git
   cd jigglypuff
   ```

2. **Install dependencies:**
   ```bash
   # Install cliclick using Homebrew
   brew install cliclick
   
   # Create a virtual environment
   python3 -m venv venv
   source venv/bin/activate
   
   # Install Python MCP SDK
   pip install mcp
   ```

3. **Configure accessibility permissions:**
   - Open System Preferences > Security & Privacy > Privacy
   - Select "Accessibility" from the left sidebar
   - Click the lock icon and authenticate
   - Add your terminal application (Terminal.app, iTerm2, etc.) to the list

4. **Make scripts executable:**
   ```bash
   chmod +x jiggly_puff.sh mcp_server.py
   ```

## Usage

### Running the MCP Server

To start the MCP server that exposes the jigglypuff tools:

```bash
source venv/bin/activate
python mcp_server.py
```

The server will listen on stdio transport for MCP-compatible clients.

### MCP Tools

The server exposes several tools for AI agent integration:

1. **wake_up_jiggly** - Initiates the cursor jiggling process
   - `interval`: Time between jiggles in seconds (5-300, default: 30)
   - `offset`: Mouse movement offset in pixels (1-10, default: 1)

2. **put_jiggly_to_sleep** - Terminates the running cursor jiggling process

3. **check_jiggly_status** - Checks current cursor jiggling state

4. **enable_jiggling_before_tasks** - Implements the rule: ALWAYS use jigglypuff MCP to enable jiggling before beginning tasks

5. **disable_jiggling_after_tasks** - Implements the rule: ALWAYS disable jiggling when task complete

### Direct Script Usage

You can also run the jigglypuff script directly for manual control:

```bash
./jiggly_puff.sh [interval] [offset]
```

- `interval`: Time between jiggles in seconds (default: 30)
- `offset`: Mouse movement offset in pixels (default: 1)

Example:
```bash
# Jiggle every 30 seconds with 2-pixel movements
./jiggly_puff.sh 30 2

# Jiggle every 60 seconds with 1-pixel movements
./jiggly_puff.sh 60 1
```

## MCP Client Configuration

### Qoder Integration

To register jigglypuff with Qoder, you need to update your global MCP configuration file.

1. Locate your Qoder MCP configuration file at `~/.config/qoder/mcp.json`
2. Add the jigglypuff server configuration to the `mcpServers` section:

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

Make sure to update the paths to match your actual installation directory.

To enable the automatic jiggling rules, add the following to your Qoder configuration:

```json
{
  "jigglypuffRules": {
    "enableOnTaskStart": true,
    "disableOnTaskComplete": true
  }
}
```

For more detailed configuration instructions, see [MCP_CONFIGURATION.md](MCP_CONFIGURATION.md).

### Claude Desktop Integration

Add to `~/Library/Application Support/Claude/claude_desktop_config.json`:

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

### Other MCP Clients

For other MCP clients:
- Follow the client-specific documentation for adding MCP servers
- The server implements the standard MCP protocol
- Command: `/Users/trose/src/mouse-jiggler/venv/bin/python mcp_server.py`
- Transport: stdio

## Rules Configuration

jigglypuff includes built-in rules for automatic operation:

1. **enable_jiggling_before_tasks**: Automatically enables jiggling when tasks begin
2. **disable_jiggling_after_tasks**: Automatically disables jiggling when tasks complete

These rules are defined in `jigglypuff_rules.json` and can be customized as needed.

MCP clients can automatically invoke these rules by calling the appropriate tools:
- Call `enable_jiggling_before_tasks` when beginning a task
- Call `disable_jiggling_after_tasks` when completing a task

Alternatively, clients can use the generic tools:
- Call `wake_up_jiggly` to enable jiggling
- Call `put_jiggly_to_sleep` to disable jiggling

## Testing

Run the test suite to verify functionality:

```bash
source venv/bin/activate
python test_functions.py
```

This will test all three functions:
1. Check initial status (should be sleeping)
2. Wake up jigglypuff
3. Check status (should be jiggling)
4. Put jigglypuff to sleep
5. Check final status (should be sleeping)

## Troubleshooting

### Accessibility Permissions

If you see the warning "WARNING: Accessibility privileges not enabled", you need to grant accessibility permissions to your terminal application:
1. Open System Preferences > Security & Privacy > Privacy
2. Select "Accessibility" from the left sidebar
3. Click the lock icon and authenticate
4. Add your terminal application (Terminal.app, iTerm2, etc.) to the list

### cliclick Not Found

If you get "command not found: cliclick", make sure Homebrew is installed and cliclick is installed:
```bash
brew install cliclick
```

### MCP SDK Issues

If you have issues with the MCP SDK, make sure you're using a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```

## Related Tools and Keywords

**Alternative names and related searches**: 
- Mouse activity simulator
- Cursor movement automation
- Screen awake utility
- System sleep preventer
- AI agent helper tool
- MCP automation server
- macOS productivity tool
- Developer automation utility
- Terminal-based mouse mover
- Background activity generator

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.