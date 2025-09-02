#!/bin/bash
# demo_rules.sh - Demonstrate the jigglypuff rules in action

echo "🤖 jigglypuff Rules Demo"
echo "========================"
echo

# Check initial status
echo "1. Checking initial jigglypuff status:"
python mcp_server.py <<EOF
{"jsonrpc": "2.0", "id": 1, "method": "tools/call", "params": {"name": "check_jiggly_status", "arguments": {}}}
EOF

echo
echo "2. Enabling jiggling (as if starting a task):"
python mcp_server.py <<EOF
{"jsonrpc": "2.0", "id": 2, "method": "tools/call", "params": {"name": "enable_jiggling_before_tasks", "arguments": {}}}
EOF

echo
echo "3. Checking status after enabling:"
python mcp_server.py <<EOF
{"jsonrpc": "2.0", "id": 3, "method": "tools/call", "params": {"name": "check_jiggly_status", "arguments": {}}}
EOF

echo
echo "4. Disabling jiggling (as if completing a task):"
python mcp_server.py <<EOF
{"jsonrpc": "2.0", "id": 4, "method": "tools/call", "params": {"name": "disable_jiggling_after_tasks", "arguments": {}}}
EOF

echo
echo "5. Final status check:"
python mcp_server.py <<EOF
{"jsonrpc": "2.0", "id": 5, "method": "tools/call", "params": {"name": "check_jiggly_status", "arguments": {}}}
EOF

echo
echo "✅ Demo complete! The rules have been demonstrated."