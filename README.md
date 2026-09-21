# DevSentry

AI-powered DevOps assistant for cloud troubleshooting and incident analysis.

## Overview

DevSentry is an AI-powered conversational DevOps assistant designed to help developers and DevOps engineers investigate infrastructure and application problems.

It combines natural-language conversation, project and infrastructure information, log analysis, retrieval-augmented generation (RAG), controlled DevOps tools, conversation memory, and an LLM.

## Core Use Cases

DevSentry should be able to help investigate:

- EC2 application returning 502 errors
- Failed deployments
- Backend crashes
- Application and Nginx errors
- Resource and disk usage issues
- Configuration problems
- Questions about project and infrastructure information
- Incident report generation

## Target Architecture

User → CloudFront → S3 frontend → EC2/FastAPI backend → AI controller → RAG + tools + memory → LLM → response

## Technology Stack

- Frontend: HTML, CSS, JavaScript
- Backend: Python + FastAPI
- AI: LLM API/model
- Compute: AWS EC2
- Storage: AWS S3
- CDN: AWS CloudFront
- OS: Ubuntu Linux
- Automation: Bash
- Terminal: Git Bash
- Version control: Git + GitHub
- API: REST
- Retrieval: RAG
- Data: Application, Nginx, deployment, and system logs

## Initial DevOps Tools

The first version will use controlled, read-only tools such as:

- EC2 status checks
- Application log reading
- Nginx log reading
- Running process checks
- Disk usage checks
- Memory checks
- Deployment analysis
- Incident report generation

## Project Goals

The project will be developed phase by phase:

1. Requirements and design
2. Development environment
3. Chat MVP
4. Conversation memory
5. Log ingestion
6. RAG
7. DevOps tool calling
8. Incident analysis
9. AWS deployment
10. Git Bash automation
11. Security and reliability
12. Monitoring
13. Testing and demonstration
14. Documentation and portfolio

## AWS Components

The final deployment will include:

- Amazon EC2
- Amazon S3
- Amazon CloudFront

AWS resources will be introduced after local development and testing.

## Security Principles

- Never commit secrets
- Never commit AWS credentials
- Never commit AI API keys
- Use least-privilege access
- Start with read-only DevOps tools
- Do not allow arbitrary shell commands from the LLM
- Validate tool inputs
- Log tool execution safely
- Protect sensitive information in logs

## Project Status

🚧 Development in progress
