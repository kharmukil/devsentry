#!/usr/bin/env bash

set -e

KEY_PATH="$HOME/Downloads/MSD7.pem"
EC2_HOST="ubuntu@3.83.79.57"
OUTPUT_DIR="collected-logs"

mkdir -p "$OUTPUT_DIR"

echo "Collecting DevSentry logs..."

scp -i "$KEY_PATH" "$EC2_HOST:/home/ubuntu/devsentry/sample-data/logs/application/app.log" \
    "$OUTPUT_DIR/application.log"

scp -i "$KEY_PATH" "$EC2_HOST:/var/log/nginx/error.log" \
    "$OUTPUT_DIR/nginx-error.log"

ssh -i "$KEY_PATH" "$EC2_HOST" \
    "sudo journalctl -u devsentry --no-pager -n 200" \
    > "$OUTPUT_DIR/devsentry-service.log"

echo "Logs collected in $OUTPUT_DIR/"
