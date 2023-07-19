socket = io();


// Get the required elements
var messageInput = document.getElementById('message-input');
var sendButton = document.getElementById('send-button');
var messageContainer = document.getElementById('message-container');

// Event listener for the send button
sendButton.addEventListener('click', function() {
    var message = messageInput.value;
    var user_name = messageContainer.getAttribute("data-username");
    if (message) {
        socket.emit("message", message);
        displayMessage(user_name + ' (you): ' + message);
        messageInput.value = '';
    }
});

socket.addEventListener("message", function(msg){
    displayMessage(msg);
})

// Function to display a message in the message container
function displayMessage(message, user_param) {
    var messageElement = document.createElement('div');
    messageElement.textContent = message;
    messageContainer.appendChild(messageElement);
    messageContainer.scrollTop = messageContainer.scrollHeight;
    if (user_param){
        messageElement.style.position= "relative";
        messageElement.style.right = "0";
    };
}
