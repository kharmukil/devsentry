import requests

from fastapi import APIRouter, Request
from slowapi import Limiter
from slowapi.util import get_remote_address

from backend.app.ai.tool_controller import ToolController
from backend.app.memory.memory import ConversationMemory
from backend.app.models.chat import ChatRequest, ChatResponse
from backend.app.rag.rag_service import RAGService


# Create the API router.
router = APIRouter()


# Store recent conversation messages in memory.
memory = ConversationMemory()


# Load the project knowledge used by RAG.
rag = RAGService("sample-data/project-data")


# Create the controlled DevOps tool controller.
tool_controller = ToolController()


# Ollama API endpoint.
OLLAMA_URL = "http://127.0.0.1:11434/api/generate"


# Qwen model running through Ollama.
OLLAMA_MODEL = "qwen2.5:3b"


# Rate limiter.
#
# SlowAPI identifies clients using their IP address.
limiter = Limiter(key_func=get_remote_address)


@router.post("/chat", response_model=ChatResponse)
@limiter.limit("10/minute")
def chat(request: Request, chat_request: ChatRequest):

    # Get the user's message from the JSON request body.
    message = chat_request.message.strip()


    # ---------------------------------------------------------
    # CONTROLLED DEVOPS TOOL
    # ---------------------------------------------------------

    # Allow explicit requests such as:
    # /tool check_disk_usage
    if message.startswith("/tool "):

        tool_name = message[6:].strip()

        try:
            # Execute only an approved tool.
            result = tool_controller.execute_tool(tool_name)

            if isinstance(result, dict):
                assistant_response = str(result)
            else:
                assistant_response = result

        except ValueError as error:
            # Return controlled validation errors.
            assistant_response = str(error)


        # Store the user's tool request.
        memory.add_message(
            chat_request.session_id,
            "user",
            message,
        )


        # Store the tool result.
        memory.add_message(
            chat_request.session_id,
            "assistant",
            assistant_response,
        )


        # Return the tool result.
        return ChatResponse(
            response=assistant_response,
            session_id=chat_request.session_id,
        )


    # ---------------------------------------------------------
    # CONVERSATION MEMORY
    # ---------------------------------------------------------

    # Store the current user message.
    memory.add_message(
        chat_request.session_id,
        "user",
        message,
    )


    # Retrieve the latest conversation messages.
    history = memory.get_history(
        chat_request.session_id
    )[-10:]


    # ---------------------------------------------------------
    # RAG RETRIEVAL
    # ---------------------------------------------------------

    # Search project knowledge relevant to the question.
    retrieved_chunks = rag.retrieve(
        message,
        top_k=3,
    )


    # Build the retrieved context.
    context_parts = []

    for chunk in retrieved_chunks:

        context_parts.append(
            f"Source: {chunk['source']}\n"
            f"{chunk['content']}"
        )


    context = "\n\n".join(context_parts)


    # ---------------------------------------------------------
    # PROMPT CONSTRUCTION
    # ---------------------------------------------------------

    prompt_parts = [
        "You are DevSentry, an AI-powered DevOps assistant.",
        "Answer clearly and explain technical concepts in simple terms.",
        "",
        "Use the following retrieved project knowledge when relevant.",
        "Do not invent information that is not supported by the context.",
        "",
        "Retrieved project knowledge:",
        context,
        "",
        "Conversation history:",
    ]


    # Add recent conversation history.
    for history_message in history:

        prompt_parts.append(
            f"{history_message['role'].upper()}: "
            f"{history_message['content']}"
        )


    # Tell the model to produce the assistant response.
    prompt_parts.append("ASSISTANT:")


    # Combine the prompt sections.
    prompt = "\n".join(prompt_parts)


    # ---------------------------------------------------------
    # OLLAMA REQUEST
    # ---------------------------------------------------------

    payload = {
        "model": OLLAMA_MODEL,
        "prompt": prompt,
        "stream": False,
    }


    # Send the prompt to Ollama.
    #
    # The timeout prevents the request from waiting forever.
    response = requests.post(
        OLLAMA_URL,
        json=payload,
        timeout=120,
    )


    # Raise an error if Ollama returns an HTTP error.
    response.raise_for_status()


    # Convert the response into JSON.
    data = response.json()


    # Extract the generated answer.
    assistant_response = data["response"].strip()


    # ---------------------------------------------------------
    # SAVE ASSISTANT RESPONSE
    # ---------------------------------------------------------

    # Store the assistant's response in conversation memory.
    memory.add_message(
        chat_request.session_id,
        "assistant",
        assistant_response,
    )


   # Return the final response.
    return ChatResponse(
        response=assistant_response,
        session_id=chat_request.session_id,
)
