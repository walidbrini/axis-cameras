#!/bin/bash

# TCP Listener on port 5000
PORT=5000
LOGFILE="$HOME/axis_tcp.log"

echo "Starting TCP listener on port $PORT..."
echo "Logging to $LOGFILE"

# Keep listening forever
while true; do
    # Listen and append incoming messages to log file
    nc -l "$PORT" >> "$LOGFILE" 2>&1
done