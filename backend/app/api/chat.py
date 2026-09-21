import requests
from fastapi import APIRouter

from backend.app.memory.memory import ConversationMemory
from backend.app.models.chat import ChatRequest, ChatResponse

router = APIRouter()

OLLAMA_URL = "http://127.0.0.1:11434/api/generate"
OLLAMA_MODEL = "qwen2.5:3b"

memory = ConversationMemory()


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    memory.add_message(
        request.session_id,
        "user",
        request.message,
    )

    history = memory.get_history(request.session_id)

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

    memory.add_message(
        request.session_id,
        "assistant",
        assistant_response,
    )

    return ChatResponse(
        response=assistant_response,
        session_id=request.session_id,
    )
