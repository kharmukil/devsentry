import requests

from fastapi import APIRouter, Request
from slowapi import Limiter
from slowapi.util import get_remote_address

from backend.app.ai.tool_controller import ToolController
from backend.app.memory.memory import ConversationMemory
from backend.app.models.chat import ChatRequest, ChatResponse
from backend.app.rag.rag_service import RAGService


# Create the API router for chat-related endpoints.
router = APIRouter()


# Create the conversation memory service.
# This stores recent messages for each session.
memory = ConversationMemory()


# Create the RAG service.
# It retrieves relevant DevSentry project information
# from the sample-data/project-data directory.
rag = RAGService("sample-data/project-data")


# Create the controlled DevOps tool controller.
# Only tools registered by the controller can be executed.
tool_controller = ToolController()


# Local Ollama API endpoint.
# The EC2 reverse SSH tunnel makes Windows Ollama
# available to the EC2 application through localhost.
OLLAMA_URL = "http://127.0.0.1:11434/api/generate"


# Local Qwen model running through Ollama.
OLLAMA_MODEL = "qwen2.5:3b"


# Create a rate limiter based on the client's IP address.
#
# This prevents a single client from sending unlimited
# requests to the AI endpoint.
limiter = Limiter(key_func=get_remote_address)


@router.post("/chat", response_model=ChatResponse)
@limiter.limit("10/minute")
def chat(request: ChatRequest, http_request: Request):
    """
    Main DevSentry conversational endpoint.

    The endpoint:
    1. Receives the user's message.
    2. Handles explicit DevOps tool requests.
    3. Stores conversation history.
    4. Retrieves relevant project information using RAG.
    5. Builds the AI prompt.
    6. Sends the prompt to Ollama/Qwen.
    7. Stores the AI response.
    8. Returns the response to the frontend.

    The http_request parameter is used by SlowAPI for
    identifying the client and enforcing the rate limit.
    """

    # Remove unnecessary whitespace from the user's message.
    message = request.message.strip()


    # ---------------------------------------------------------
    # CONTROLLED TOOL EXECUTION
    # ---------------------------------------------------------
    #
    # Users can explicitly request an approved tool using:
    #
    # /tool tool_name
    #
    # Example:
    #
    # /tool check_disk_usage
    #
    # The ToolController validates the requested tool.
    if message.startswith("/tool "):

        # Extract the tool name after "/tool ".
        tool_name = message[6:].strip()

        try:
            # Execute only a tool registered in ToolController.
            result = tool_controller.execute_tool(tool_name)

            # Convert dictionary results into readable text.
            if isinstance(result, dict):
                assistant_response = str(result)

            else:
                assistant_response = result

        except ValueError as error:
            # Return controlled validation errors instead of
            # allowing the API request to crash.
            assistant_response = str(error)


        # Store the user's tool request in conversation memory.
        memory.add_message(
            request.session_id,
            "user",
            message,
        )


        # Store the tool result as the assistant response.
        memory.add_message(
            request.session_id,
            "assistant",
            assistant_response,
        )


        # Return the tool result immediately.
        return ChatResponse(
            response=assistant_response,
            session_id=request.session_id,
        )


    # ---------------------------------------------------------
    # CONVERSATION MEMORY
    # ---------------------------------------------------------

    # Store the current user message.
    memory.add_message(
        request.session_id,
        "user",
        message,
    )


    # Retrieve recent conversation history.
    #
    # Only the latest 10 messages are sent to the model

    # Build the retrieved knowledge context.
    context_parts = []

    for chunk in retrieved_chunks:

            f"{chunk['content']}"

    # Join multiple retrieved documents into one context block.
    context = "\n\n".join(context_parts)


    # ---------------------------------------------------------
    # AI PROMPT

    # Build the prompt sent to Qwen through Ollama.
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


    # Add recent conversation history to the prompt.
    for history_message in history:

        prompt_parts.append(
            f"{history_message['role'].upper()}: "
            f"{history_message['content']}"
        )


    # Tell the model that it should generate the assistant response.
    prompt_parts.append("ASSISTANT:")


    # Combine all prompt sections.
    prompt = "\n".join(prompt_parts)


    # ---------------------------------------------------------
    # OLLAMA REQUEST
    # ---------------------------------------------------------

    payload = {
        "model": OLLAMA_MODEL,
        "prompt": prompt,
        "stream": False,
    }


    # Send the request to Ollama.
    #
    # The 120-second timeout prevents the FastAPI request
    # from waiting forever if the local model becomes unavailable.
    response = requests.post(
        OLLAMA_URL,
        json=payload,
        timeout=120,
    )


    # Raise an exception if Ollama returned an HTTP error.
    response.raise_for_status()


    # Convert the Ollama JSON response into a Python dictionary.
    data = response.json()


    # Extract the generated assistant response.
    assistant_response = data["response"].strip()


    # ---------------------------------------------------------
    # STORE AI RESPONSE
    # ---------------------------------------------------------

    # Store the assistant's answer in conversation memory.
    memory.add_message(
        request.session_id,
        "assistant",
        assistant_response,
    )


    # Return the final response to the frontend.
    return ChatResponse(
        response=assistant_response,
        session_id=request.session_id,
    ) 


