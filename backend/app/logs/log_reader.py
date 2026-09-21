from pathlib import Path


class LogReader:
    def read_log(self, file_path: str) -> str:
        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError(f"Log file not found: {file_path}")

        return path.read_text(encoding="utf-8")

    def get_log_type(self, file_path: str) -> str:
        path = Path(file_path)

        if path.parent.name in {
            "application",
            "nginx",
            "deployment",
            "system",
        }:
            return path.parent.name

        return "unknown"

    def search(self, file_path: str, keyword: str) -> list[str]:
        log_text = self.read_log(file_path)

        return [
            line
            for line in log_text.splitlines()
            if keyword.lower() in line.lower()
        ]

    def filter_by_level(self, file_path: str, level: str) -> list[str]:
        return self.search(file_path, level)