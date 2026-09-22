from pathlib import Path


class NginxTool:
    ALLOWED_LOGS = {
        "error": Path("sample-data/logs/nginx/error.log"),
        "access": Path("sample-data/logs/nginx/access.log"),
    }

    def read_nginx_logs(self, log_type: str = "error") -> str:
        if log_type not in self.ALLOWED_LOGS:
            raise ValueError(
                "Invalid Nginx log type. Use 'error' or 'access'."
            )

        log_path = self.ALLOWED_LOGS[log_type]

        if not log_path.exists():
            raise FileNotFoundError(
                f"Nginx log not found: {log_path}"
            )

        return log_path.read_text(encoding="utf-8")
