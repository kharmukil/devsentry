import requests
from fastapi import APIRouter

from backend.app.models.chat import ChatRequest, ChatResponse

router = APIRouter()

OLLAMA_URL = "http://127.0.0.1:11434/api/generate"
OLLAMA_MODEL = "qwen2.5:3b"

conversation_history = {}


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    history = conversation_history.setdefault(request.session_id, [])

    history.append({
        "role": "user",
        "content": request.message,
    })

    prompt_parts = [
        "You are DevSentry, an AI-powered DevOps assistant.",
        "Answer clearly and explain technical concepts in simple terms when appropriate.",
        "",
    ]

    for message in history:
        prompt_parts.append(
            f"{message['role'].upper()}: {message['content']}"
        )

    prompt_parts.append("ASSISTANT:")

    prompt = "\n".join(prompt_parts)

    payload = {
        "model": OLLAMA_MODEL,
        "prompt": prompt,
        "stream": False,
    }

    response = requests.post(
        OLLAMA_URL,
        json=payload,
        timeout=120,
    )

    response.raise_for_status()

    data = response.json()
    assistant_response = data["response"].strip()

    history.append({
        "role": "assistant",
        "content": assistant_response,
    })

    return ChatResponse(
        response=assistant_response,
        session_id=request.session_id,
    )
