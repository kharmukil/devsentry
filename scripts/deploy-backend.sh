#!/usr/bin/env bash

set -e

KEY_PATH="$HOME/Downloads/MSD7.pem"
EC2_HOST="ubuntu@3.83.79.57"
APP_DIR="/home/ubuntu/devsentry"

echo "Deploying backend to EC2..."

ssh -i "$KEY_PATH" "$EC2_HOST" << EOF
set -e

cd "$APP_DIR"

echo "Pulling latest code..."
git pull origin main

echo "Installing dependencies..."
source .venv/bin/activate
pip install -r requirements.txt

echo "Restarting DevSentry..."
sudo systemctl restart devsentry

echo "Checking service..."
sudo systemctl is-active --quiet devsentry

echo "Backend deployment completed."
EOF

