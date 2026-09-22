# DevSentry Project Overview

## Project Purpose

DevSentry is an AI-powered DevOps assistant for cloud troubleshooting and incident analysis.

It is designed to help developers and DevOps engineers investigate application failures, infrastructure problems, deployment issues, and operational incidents.

## Current Technology Stack

- Frontend: HTML, CSS, JavaScript
- Backend: Python and FastAPI
- AI Model: Qwen 2.5 3B through Ollama
- Version Control: Git and GitHub
- Development Environment: Git Bash and VS Code

## Current Local Architecture

Browser
    ↓
FastAPI
    ↓
Chat API
    ↓
Conversation Memory
    ↓
Ollama
    ↓
Qwen 2.5 3B

## Log Analysis

DevSentry can analyze:

- Application logs
- Nginx logs
- Deployment logs
- System logs

The log analysis pipeline is:

Log File
    ↓
LogReader
    ↓
LogParser
    ↓
LogAnalyzer
    ↓
AI Log Analysis

## Troubleshooting

A future DevSentry troubleshooting workflow will combine information from application logs, Nginx logs, deployment information, system information, and other project data.

## Project Status

The local MVP currently includes:

- Chat interface
- FastAPI backend
- Ollama and Qwen integration
- Conversation memory
- Log ingestion
- Log parsing
- Log analysis
- AI-assisted log analysis

## Future Components

Planned components include:

- Retrieval-Augmented Generation (RAG)
- Controlled DevOps tools
- Incident analysis
- AWS deployment using S3, EC2, and CloudFront
- Git Bash automation
- Security controls
- Monitoring
- Testing