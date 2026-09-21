from fastapi import APIRouter, HTTPException

from backend.app.ai.log_analysis import AILogAnalyzer
from backend.app.logs.log_analyzer import LogAnalyzer


router = APIRouter(prefix="/logs", tags=["logs"])

analyzer = LogAnalyzer()
ai_analyzer = AILogAnalyzer()


@router.get("/analyze")
def analyze_log(file_path: str):
    try:
        analysis = analyzer.analyze(file_path)
        explanation = ai_analyzer.analyze(analysis)

        return {
            **analysis,
            "ai_analysis": explanation,
        }

    except FileNotFoundError as error:
        raise HTTPException(
            status_code=404,
            detail=str(error),
        )