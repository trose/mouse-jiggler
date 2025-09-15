# jigglypuff: AI-Controlled Mouse Activity Manager for macOS

[![MCP Badge](https://lobehub.com/badge/mcp/trose-jigglypuff)](https://lobehub.com/mcp/trose-jigglypuff)

**Prevent screen savers, system sleep, and keep your macOS awake during AI processing tasks.** jigglypuff is a lightweight mouse jiggler and activity manager that uses imperceptible cursor movements to simulate user activity. Perfect for developers using AI agents like Cursor, Qoder and Claude Desktop.

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

#### Core Tools
1. **wake_up_jiggly** - Initiates the cursor jiggling process
   - `interval`: Time between jiggles in seconds (5-300, default: 30)
   - `offset`: Mouse movement offset in pixels (1-10, default: 1)
   - Returns: Status message with PID and settings

2. **put_jiggly_to_sleep** - Terminates the running cursor jiggling process
   - Returns: Confirmation message with PID

3. **check_jiggly_status** - Checks current cursor jiggling state
   - Returns: Current status (jiggling, sleeping, or stopped)

#### Rule-Compliant Tools
4. **enable_jiggling_before_tasks** - Implements the rule: ALWAYS use jigglypuff MCP to enable jiggling before beginning tasks
   - Automatically starts jiggling with default settings

5. **disable_jiggling_after_tasks** - Implements the rule: ALWAYS disable jiggling when task complete
   - Automatically stops jiggling

### MCP Prompts

The server provides helpful prompts for user interaction:

1. **jigglypuff_help** - Comprehensive usage guide and best practices
2. **jigglypuff_troubleshooting** - Solutions for common issues and problems

### MCP Resources

The server exposes resources for context data management:

1. **jigglypuff-config** - Current configuration and system status (JSON format)
2. **jigglypuff-rules** - Official usage rules and best practices (JSON format)

## Configuration

### MCP Server Configuration

The configuration includes:

1. **jigglypuff** - The main mouse jiggling server

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

## Testing

Run the provided test suite to verify functionality:

```bash
source venv/bin/activate

# Run individual test files
python tests/test_functions.py
python tests/test_comprehensive.py

# Or run all tests (if you have pytest installed)
pytest tests/
```

## LobeHub Integration

This MCP server is registered with [LobeHub](https://lobehub.com/mcp/trose-jigglypuff) and includes:

- ✅ **MCP Tools**: 5 tools for mouse jiggling control
- ✅ **MCP Prompts**: 2 prompts for help and troubleshooting  
- ✅ **MCP Resources**: 2 resources for configuration and rules
- ✅ **Installation Methods**: Multiple deployment options
- ✅ **README Documentation**: Comprehensive usage guide
- ✅ **MIT License**: Open source licensing

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
