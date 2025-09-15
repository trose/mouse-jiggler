#!/usr/bin/env python3
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Test the individual functions
from mcp_server import wake_up_jiggly, put_jiggly_to_sleep, check_jiggly_status

print("Testing jigglypuff functions...")

# Check initial status
print("Initial status:", check_jiggly_status())

# Wake up jiggly
result = wake_up_jiggly(5, 1)  # 5 second interval, 1 pixel offset
print("Wake up result:", result)

# Check status after wake up
print("Status after wake up:", check_jiggly_status())

# Put jiggly to sleep
result = put_jiggly_to_sleep()
print("Put to sleep result:", result)

# Check final status
print("Final status:", check_jiggly_status())