# DevSentry Troubleshooting Knowledge

## HTTP 502 Bad Gateway

A 502 Bad Gateway error can occur when a reverse proxy such as Nginx cannot successfully communicate with the upstream application.

Useful evidence includes:

- Nginx access logs
- Nginx error logs
- Application logs
- Running application processes
- Application listening ports
- Recent deployment logs

An Nginx message such as "upstream connection refused" indicates that the proxy attempted to connect to the upstream service but the connection was refused.

Possible areas to investigate include:

- Whether the backend application is running
- Whether the backend is listening on the expected port
- Whether the configured upstream address is correct
- Whether a recent deployment changed the application
- Whether the application failed during startup

The log evidence should be checked before deciding on a root cause.

## HTTP 500 Internal Server Error

A 500 response generally indicates that the server encountered an error while processing a request.

Useful evidence includes:

- Application error logs
- Request timestamps
- Stack traces
- Database connection errors
- Recent deployment information

The exact root cause should be determined from the available evidence rather than assumed from the HTTP status code alone.

## Database Connection Problems

Database-related errors may appear as:

- Connection timeout
- Connection refused
- Authentication failure
- Connection pool exhaustion

When investigating database problems, compare the application error timestamp with deployment and system events.

## Deployment Failures

When an application fails after deployment, investigate:

- Deployment logs
- Application startup logs
- Port conflicts
- Dependency installation errors
- Configuration changes
- Application process status

A deployment message such as "Port 8000 is already in use" indicates a port conflict and should be investigated as deployment evidence.

## Evidence-Based Troubleshooting

DevSentry should distinguish between:

### Confirmed Evidence

Information directly supported by logs, configuration, or tool results.

### Hypothesis

A possible explanation that requires additional evidence or verification.

DevSentry should avoid presenting a hypothesis as a confirmed root cause.