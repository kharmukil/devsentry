from backend.app.tools.dispatcher import ToolDispatcher


class IncidentEvidenceCollector:
    def __init__(self):
        self.dispatcher = ToolDispatcher()

    def collect(self) -> dict:
        return {
            "application_logs": self.dispatcher.execute(
                "read_application_logs"
            ),
            "nginx_logs": self.dispatcher.execute(
                "read_nginx_logs"
            ),
            "deployment": self.dispatcher.execute(
                "analyze_deployment"
            ),
        }
