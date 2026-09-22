import re


# Patterns for sensitive values that should never appear in logs.
SENSITIVE_PATTERNS = [
    # API keys, tokens, secrets, and passwords.
    re.compile(
        r"(?i)(api[_-]?key|token|secret|password)\s*[:=]\s*[^\s,;]+"
    ),

    # AWS-style access key IDs.
    re.compile(r"\bAKIA[0-9A-Z]{16}\b"),

    # Private-key blocks.
    re.compile(
        r"-----BEGIN [A-Z ]*PRIVATE KEY-----.*?"
        r"-----END [A-Z ]*PRIVATE KEY-----",
        re.DOTALL,
    ),
]


def sanitize_log(message: str) -> str:
    """
    Remove or mask sensitive information before writing to logs.
    """

    sanitized = message

    for pattern in SENSITIVE_PATTERNS:
        sanitized = pattern.sub("[REDACTED]", sanitized)

    return sanitized
