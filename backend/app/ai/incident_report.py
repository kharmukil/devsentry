from backend.app.models.incident import IncidentReport


class IncidentReportGenerator:
    def generate(self, report: IncidentReport) -> str:
        lines = [
            f"# {report.title}",
            "",
            "## Summary",
            report.summary,
            "",
            "## Confirmed Evidence",
        ]

        for evidence in report.confirmed_evidence:
            lines.append(f"- {evidence}")

        lines.extend(
            [
                "",
                "## Hypotheses",
            ]
        )

        for hypothesis in report.hypotheses:
            lines.append(f"- {hypothesis}")

        lines.extend(
            [
                "",
                "## Recommended Checks",
            ]
        )

        for check in report.recommended_checks:
            lines.append(f"- {check}")

        return "\n".join(lines)
