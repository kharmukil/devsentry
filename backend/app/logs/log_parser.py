import re


class LogParser:
    LOG_PATTERN = re.compile(
        r"^(?P<timestamp>\S+ \S+) "
        r"(?P<level>INFO|WARNING|ERROR) "
        r"(?P<message>.*)$"
    )

    def parse_line(self, line: str) -> dict:
        match = self.LOG_PATTERN.match(line.strip())

        if not match:
            return {
                "timestamp": None,
                "level": "UNKNOWN",
                "message": line.strip(),
            }

        return {
            "timestamp": match.group("timestamp"),
            "level": match.group("level"),
            "message": match.group("message"),
        }

    def parse_file(self, file_path: str) -> list[dict]:
        from pathlib import Path

        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError(f"Log file not found: {file_path}")

        return [
            self.parse_line(line)
            for line in path.read_text(encoding="utf-8").splitlines()
            if line.strip()
        ]

    def summarize(self, records: list[dict]) -> dict:
        summary = {
            "total": len(records),
            "INFO": 0,
            "WARNING": 0,
            "ERROR": 0,
        }

        for record in records:
            level = record["level"]

            if level in summary:
                summary[level] += 1

        return summary