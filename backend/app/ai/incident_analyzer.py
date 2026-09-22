from backend.app.models.incident import IncidentReport


class IncidentAnalyzer:
    def analyze(
        self,
        evidence: dict,
        knowledge: list[dict] | None = None,
    ) -> IncidentReport:
        application_logs = evidence["application_logs"]
        nginx_logs = evidence["nginx_logs"]
        deployment = evidence["deployment"]

        confirmed_evidence = []
        hypotheses = []
        recommended_checks = []

        if "upstream connection refused" in nginx_logs.lower():
            confirmed_evidence.append(
                "Nginx reported an upstream connection refusal."
            )

        if "502" in nginx_logs:
            confirmed_evidence.append(
                "Nginx access logs contain HTTP 502 responses."
            )

        if "port 8000 is already in use" in deployment.lower():
            confirmed_evidence.append(
                "Deployment logs report that port 8000 was already in use."
            )

        if "database timeout" in application_logs.lower():
            confirmed_evidence.append(
                "Application logs contain a database timeout."
            )

        if knowledge:
            recommended_checks.append(
                "Review the retrieved DevSentry troubleshooting knowledge "
                "when investigating the incident."
            )

        hypotheses.append(
            "The backend application may not have been available "
            "on the expected upstream port."
        )

        recommended_checks.extend(
            [
                "Check whether the backend process is running.",
                "Check which process is listening on the expected port.",
                "Review the most recent deployment for startup failures.",
            ]
        )

        return IncidentReport(
            title="DevSentry Incident Analysis",
            summary=(
                "The available logs contain evidence of application, "
                "Nginx, and deployment-related failures."
            ),
            confirmed_evidence=confirmed_evidence,
            hypotheses=hypotheses,
            recommended_checks=recommended_checks,
        )
