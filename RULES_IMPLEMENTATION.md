# jigglypuff Rules Implementation

This document describes how the requested rules have been implemented in the jigglypuff project.

## Requested Rules

1. ALWAYS use jigglypuff MCP to enable jiggling before beginning tasks
2. ALWAYS disable jiggling when task complete

## Implementation Details

### 1. Rules Configuration File

A new configuration file `jigglypuff_rules.json` has been created to define the rules in a structured format:

```json
{
  "rules": [
    {
      "name": "enable_jiggling_before_tasks",
      "description": "ALWAYS use jigglypuff MCP to enable jiggling before beginning tasks",
      "trigger": {
        "type": "task_start"
      },
      "actions": [
        {
          "type": "mcp_call",
          "server": "jigglypuff",
          "tool": "wake_up_jiggly",
          "parameters": {
            "interval": 30,
            "offset": 1
          }
        }
      ]
    },
    {
      "name": "disable_jiggling_after_tasks",
      "description": "ALWAYS disable jiggling when task complete",
      "trigger": {
        "type": "task_complete"
      },
      "actions": [
        {
          "type": "mcp_call",
          "server": "jigglypuff",
          "tool": "put_jiggly_to_sleep"
        }
      ]
    }
  ]
}
```

### 2. Dedicated MCP Tools

Two new tools have been added to the MCP server (`mcp_server.py`) to directly implement the rules:

1. `enable_jiggling_before_tasks()` - Implements the first rule
2. `disable_jiggling_after_tasks()` - Implements the second rule

These tools are MCP-callable functions that wrap the existing jiggling control functions.

### 3. Documentation

The rules have been documented in multiple places:

1. **README.md** - Updated to explain the rules and how to use them
2. **RULES_IMPLEMENTATION.md** - This document explaining the implementation
3. **Demo script** - A shell script demonstrating the rules in action

### 4. Testing

A test script (`test_rules.py`) has been created to validate the rules configuration file.

## Usage

MCP clients can implement the rules in two ways:

### Option 1: Direct Tool Calls

Call the dedicated rule tools:
- `enable_jiggling_before_tasks` when starting a task
- `disable_jiggling_after_tasks` when completing a task

### Option 2: Generic Tools

Use the generic tools with appropriate timing:
- `wake_up_jiggly` when starting a task
- `put_jiggly_to_sleep` when completing a task

## Verification

To verify the rules implementation, run the demo script:

```bash
./demo_rules.sh
```

This will demonstrate the rule compliance tools in action.