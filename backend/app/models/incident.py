from pydantic import BaseModel


class IncidentReport(BaseModel):
    title: str
    summary: str
    confirmed_evidence: list[str]
    hypotheses: list[str]
    recommended_checks: list[str]
