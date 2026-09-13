async function sendMessage() {

    const input = document.getElementById("user-input");
    const chatBox = document.getElementById("chat-box");

    const message = input.value.trim();

    if (message === "") {
        return;
    }

    // Show user message
    chatBox.innerHTML += `
        <div class="message user">
            <strong>You:</strong>
            <p>${message}</p>
        </div>
    `;

    input.value = "";

    // Show loading message
    chatBox.innerHTML += `
        <div class="message bot" id="loading">
            <strong>AI Helpdesk:</strong>
            <p>Analyzing your problem...</p>
        </div>
    `;

    chatBox.scrollTop = chatBox.scrollHeight;

    try {

        const response = await fetch(
            "http://127.0.0.1:8000/ask",
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify({
                    message: message
                })
            }
        );

        const data = await response.json();

        // Remove loading message
        document.getElementById("loading").remove();

        // Show AI response
        chatBox.innerHTML += `
            <div class="message bot">
                <strong>AI Helpdesk:</strong>
                <p>${data.answer}</p>
            </div>
        `;

        chatBox.scrollTop = chatBox.scrollHeight;

    } catch (error) {

        document.getElementById("loading").remove();

        chatBox.innerHTML += `
            <div class="message bot">
                <strong>Error:</strong>
                <p>Unable to connect to the AI Helpdesk server.</p>
            </div>
        `;

        console.error(error);
    }
}


function handleKeyPress(event) {

    if (event.key === "Enter") {
        sendMessage();
    }
}