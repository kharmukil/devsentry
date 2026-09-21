from backend.app.logs.log_parser import LogParser
from backend.app.logs.log_reader import LogReader


class LogAnalyzer:
    def __init__(self):
        self.reader = LogReader()
        self.parser = LogParser()

    def analyze(self, file_path: str) -> dict:
        log_text = self.reader.read_log(file_path)
        records = self.parser.parse_file(file_path)
        summary = self.parser.summarize(records)

        return {
            "file": file_path,
            "log_type": self.reader.get_log_type(file_path),
            "line_count": len(log_text.splitlines()),
            "summary": summary,
            "records": records,
        }