import requests


OLLAMA_URL = "http://127.0.0.1:11434/api/generate"
OLLAMA_MODEL = "qwen2.5:3b"


class AILogAnalyzer:
    def analyze(self, analysis: dict) -> str:
        prompt = f"""
You are DevSentry, an AI-powered DevOps assistant.

Analyze the following log evidence.

Log type:
{analysis["log_type"]}

Log summary:
{analysis["summary"]}

Log records:
{analysis["records"]}

Explain:
1. What happened?
2. What errors or warnings are present?
3. What is the most likely technical cause based only on the evidence?
4. What should a DevOps engineer check next?

Clearly separate confirmed evidence from hypotheses.
Do not invent information that is not present in the logs.
"""

        response = requests.post(
            OLLAMA_URL,
            json={
                "model": OLLAMA_MODEL,
                "prompt": prompt,
                "stream": False,
            },
            timeout=120,
        )

        response.raise_for_status()

        return response.json()["response"].strip()