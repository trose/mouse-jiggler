# jigglypuff: AI-Controlled Mouse Activity Manager for macOS

[![MCP Badge](https://lobehub.com/badge/mcp/trose-jigglypuff)](https://lobehub.com/mcp/trose-jigglypuff)

**Prevent screen savers, system sleep, and keep your macOS awake during AI processing tasks.** jigglypuff is a lightweight mouse jiggler and activity manager that uses imperceptible cursor movements to simulate user activity. Perfect for developers using AI agents like Qoder and Claude Desktop.

**Keywords**: mouse jiggler, cursor mover, screen saver preventer, system wakefulness, AI automation, macOS automation, MCP tools, Model Context Protocol, keep screen awake, prevent sleep, automation tools, developer utilities, notification system, user alerts, macOS notifications

Version: 1.0.0

## Features

- **Prevents screen savers and system sleep** during AI processing tasks
- **Allows system to sleep** when waiting for user input to conserve energy
- **Controlled via MCP tools** for seamless integration with AI agents
- **Lightweight and efficient** implementation with minimal system impact
- **Small, imperceptible mouse movements** that won't interfere with your work
- **Automatic jiggling rules** - Automatically enables/disables jiggling based on task status
- **Cross-AI agent compatibility** - Works with Qoder, Claude Desktop, and other MCP-compatible tools
- **User Notification System** - Sends macOS notifications when Qoder needs your attention

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

### Notification MCP Server

The project also includes a macOS Notification MCP server that allows Qoder to send notifications to your system:

1. **sound_notification** - Play system sounds to get your attention
2. **banner_notification** - Display visual notifications in macOS Notification Center
3. **speak_notification** - Convert text to speech
4. **list_available_voices** - List all available text-to-speech voices
5. **test_notification_system** - Diagnostic tool to verify all notification methods

See [NOTIFICATION_MCP_USAGE.md](NOTIFICATION_MCP_USAGE.md) for detailed usage instructions.

## Configuration

### MCP Server Configuration

The MCP servers are configured in your Qoder configuration file. The configuration includes:

1. **jigglypuff** - The main mouse jiggling server
2. **macos-notification** - The notification server for user alerts

Example configuration:
```json
{
  "mcpServers": {
    "jigglypuff": {
      "command": "/Users/trose/src/mouse-jiggler/venv/bin/python",
      "args": ["mcp_server.py"],
      "cwd": "/Users/trose/src/mouse-jiggler"
    },
    "macos-notification": {
      "command": "/Users/trose/src/macos-notification-mcp/venv/bin/macos-notification-mcp",
      "args": [],
      "cwd": "/Users/trose/src/macos-notification-mcp"
    }
  }
}
```

## Testing

Run the provided test suite to verify functionality:

```bash
source venv/bin/activate
python test_functions.py
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.