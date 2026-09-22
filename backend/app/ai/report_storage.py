from pathlib import Path


class ReportStorage:
    def __init__(self, directory: str = "sample-data/incidents"):
        self.directory = Path(directory)
        self.directory.mkdir(
            parents=True,
            exist_ok=True,
        )

    def save(self, filename: str, content: str) -> str:
        safe_filename = Path(filename).name

        if not safe_filename.endswith(".md"):
            safe_filename += ".md"

        report_path = self.directory / safe_filename
        report_path.write_text(
            content,
            encoding="utf-8",
        )

        return str(report_path)
