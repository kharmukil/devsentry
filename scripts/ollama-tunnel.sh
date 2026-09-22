#!/usr/bin/env bash

KEY_PATH="$HOME/Downloads/MSD7.pem"
EC2_HOST="ubuntu@3.83.79.57"

while true; do
    ssh \
        -o ServerAliveInterval=60 \
        -o ServerAliveCountMax=3 \
        -o ExitOnForwardFailure=yes \
        -N \
        -R 11434:127.0.0.1:11434 \
        -i "$KEY_PATH" \
        "$EC2_HOST"

    echo "Tunnel disconnected. Retrying in 5 seconds..."
    sleep 5
done
