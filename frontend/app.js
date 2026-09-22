const chatForm = document.getElementById("chat-form");
const messageInput = document.getElementById("message-input");
const messages = document.getElementById("messages");

let sessionId = localStorage.getItem("devsentry_session_id");

if (!sessionId) {
    sessionId =
            "session-" +
            Date.now() +
            "-" +
            Math.random().toString(36).substring(2, 10);
    localStorage.setItem("devsentry_session_id", sessionId);
}

function addMessage(role, text) {
    const message = document.createElement("div");

    message.className = `message ${role}`;
    message.textContent = text;

    messages.appendChild(message);
}

chatForm.addEventListener("submit", async (event) => {
    event.preventDefault();

    const message = messageInput.value.trim();

    if (!message) {
        return;
    }

    addMessage("user", message);

    messageInput.value = "";

    addMessage("assistant", "Thinking...");

    try {
        const response = await fetch("/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                message: message,
                session_id: sessionId
            })
        });

        if (!response.ok) {
            throw new Error(`HTTP ${response.status}`);
        }

        const data = await response.json();

        messages.lastElementChild.textContent = data.response;

    } catch (error) {
        messages.lastElementChild.textContent =
            "Unable to connect to DevSentry backend.";
        console.error(error);
    }
});
