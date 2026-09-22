@router.post("/chat", response_model=ChatResponse)
@limiter.limit("10/minute")
def chat(request: Request, chat_request: ChatRequest):
    """
    Main DevSentry conversational endpoint.

    SlowAPI uses the HTTP Request object to identify
    the client and enforce the rate limit.
    """

    message = chat_request.message.strip()

    if message.startswith("/tool "):

        tool_name = message[6:].strip()

        try:
            result = tool_controller.execute_tool(tool_name)

            if isinstance(result, dict):
                assistant_response = str(result)
            else:
                assistant_response = result

        except ValueError as error:
            assistant_response = str(error)

        memory.add_message(
            chat_request.session_id,
            "user",
            message,
        )

        memory.add_message(
            chat_request.session_id,
            "assistant",
            assistant_response,
        )

        return ChatResponse(
            response=assistant_response,
            session_id=chat_request.session_id,
        )

    memory.add_message(
        chat_request.session_id,
        "user",
        message,
    )

    history = memory.get_history(
        chat_request.session_id
    )[-10:]

    retrieved_chunks = rag.retrieve(
        message,
        top_k=3,
    )

    context_parts = []

    for chunk in retrieved_chunks:
        context_parts.append(
            f"Source: {chunk['source']}\n"
            f"{chunk['content']}"
        )

    context = "\n\n".join(context_parts)

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

    for history_message in history:
        prompt_parts.append(
            f"{history_message['role'].upper()}: "
            f"{history_message['content']}"
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
        chat_request.session_id,
        "assistant",
        assistant_response,
    )

    return ChatResponse(
        response=assistant_response,
        session_id=chat_request.session_id,
    )
