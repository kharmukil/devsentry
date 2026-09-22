from pathlib import Path


class DeploymentTool:
    LOG_PATH = Path("sample-data/logs/deployment/deploy.log")

    def analyze_deployment(self) -> str:
        if not self.LOG_PATH.exists():
            raise FileNotFoundError(
                f"Deployment log not found: {self.LOG_PATH}"
            )

        return self.LOG_PATH.read_text(encoding="utf-8")
