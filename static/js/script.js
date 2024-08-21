// Manas Chechani Project
  document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('userInput').addEventListener('keypress', function (e) {
        if (e.key === 'Enter') {
            sendMessage();
        }
    });
});

function sendMessage() {
    var userMessage = document.getElementById('userInput').value;
    var chatbox = document.getElementById('chatbox');

    fetch('/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message: userMessage, lang: 'en' }),  // Defaulting to English
    })
    .then(response => response.json())
    .then(data => {
        var botReply = data.reply;
        chatbox.innerHTML += `<p><b>You:</b> ${userMessage}</p>`;
        chatbox.innerHTML += `<p><b>Bot:</b> ${botReply}</p>`;
        document.getElementById('userInput').value = '';  // Clear input field
        chatbox.scrollTop = chatbox.scrollHeight;  // Scroll to the bottom
    })
    .catch(error => {
        console.error('Error:', error);
    });
}
