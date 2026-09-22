#!/usr/bin/env bash

set -e

BUCKET_NAME="devsentry-958075960409"

echo "Deploying frontend to S3..."

aws s3 sync frontend/ "s3://${BUCKET_NAME}/frontend/" --delete

echo "Frontend deployment completed."
