#!/usr/bin/env bash

set -e

echo "======================================"
echo "       DevSentry Deployment"
echo "======================================"

echo
echo "[1/4] Checking local repository..."
git status --short

echo
echo "[2/4] Deploying frontend..."
./scripts/deploy-frontend.sh

echo
echo "[3/4] Deploying backend..."
./scripts/deploy-backend.sh

echo
echo "[4/4] Running health check..."
./scripts/health-check.sh

echo
echo "======================================"
echo "   DevSentry deployment successful"
echo "======================================"
