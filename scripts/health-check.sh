#!/usr/bin/env bash

set -e

EC2_IP="3.83.79.57"

echo "Checking DevSentry EC2 health..."

if curl -fsS "http://${EC2_IP}/health"; then
    echo
    echo "DevSentry health check passed."
else
    echo
    echo "DevSentry health check failed."
    exit 1
fi
