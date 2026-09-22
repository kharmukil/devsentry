from pathlib import Path


class LogTool:
    ALLOWED_LOGS = {
        "application": Path("sample-data/logs/application/app.log"),
    }

    def read_application_logs(self) -> str:
        log_path = self.ALLOWED_LOGS["application"]

        if not log_path.exists():
            raise FileNotFoundError(
                f"Application log not found: {log_path}"
            )

        return log_path.read_text(encoding="utf-8")
