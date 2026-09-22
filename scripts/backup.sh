#!/usr/bin/env bash

# Stop immediately if any command fails.
set -e

# DevSentry S3 bucket.
BUCKET_NAME="devsentry-958075960409"

# Store backups under the backups/ prefix.
BACKUP_PREFIX="s3://${BUCKET_NAME}/backups"

# Create a timestamp so every backup is unique.
TIMESTAMP=$(date +"%Y%m%d-%H%M%S")

echo "Starting DevSentry backup..."
echo "Backup timestamp: $TIMESTAMP"

# Back up incident reports.
aws s3 sync \
    sample-data/incidents/ \
    "${BACKUP_PREFIX}/${TIMESTAMP}/incidents/"

# Back up project knowledge used by RAG.
aws s3 sync \
    sample-data/project-data/ \
    "${BACKUP_PREFIX}/${TIMESTAMP}/project-data/"

# Back up sample logs.
aws s3 sync \
    sample-data/logs/ \
    "${BACKUP_PREFIX}/${TIMESTAMP}/logs/"

echo
echo "Backup completed successfully."
echo "Location: ${BACKUP_PREFIX}/${TIMESTAMP}/"
