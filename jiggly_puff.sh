#!/bin/bash
# jiggly_puff.sh

# Configuration
INTERVAL=${1:-30}  # Default to 30 seconds
OFFSET=${2:-1}     # Mouse movement offset in pixels
LOG_FILE="/tmp/mouse_jiggler.log"

# Log startup
echo "$(date): Mouse jiggler started with interval=${INTERVAL}s, offset=${OFFSET}px" >> "$LOG_FILE"

# Trap SIGTERM to log shutdown
trap 'echo "$(date): Mouse jiggler stopped" >> "$LOG_FILE"; exit 0' SIGTERM

while true; do
    # Move mouse slightly and back
    cliclick m:+$OFFSET,+0 w:100 m:-$OFFSET,-0
    
    # Log activity
    echo "$(date): Mouse jiggled" >> "$LOG_FILE"
    
    # Wait for next jiggle
    sleep $INTERVAL
done