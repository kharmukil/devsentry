const chatForm = document.getElementById("chat-form");
const messageInput = document.getElementById("message-input");
const messages = document.getElementById("messages");

function addMessage(role, text) {
    const message = document.createElement("div");
    message.className = "message " + role;
    message.textContent = text;
    messages.appendChild(message);
    messages.scrollTop = messages.scrollHeight;
}

chatForm.addEventListener("submit", async function (event) {
    event.preventDefault();

    const message = messageInput.value.trim();

    if (!message) {
        return;
    }

    addMessage("user", message);
    messageInput.value = "";

    const thinking = document.createElement("div");
    thinking.className = "message assistant";
    thinking.textContent = "Thinking...";
    messages.appendChild(thinking);

    try {
        const response = await fetch("/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                message: message,
                session_id: "browser-demo"
            })
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(
                data.detail || `HTTP ${response.status}`
            );
        }

        thinking.textContent = data.response;
    } catch (error) {
        thinking.textContent = "Error: " + error.message;
        console.error("DevSentry chat error:", error);
    }
});
