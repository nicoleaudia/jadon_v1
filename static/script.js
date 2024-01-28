document.getElementById('chat-form').addEventListener('submit', function(event) {
    event.preventDefault();

    const userInput = document.getElementById('user-input').value;

    // Send the user input to Flask server
    fetch('/process_input', {  // Assuming '/process_input' is your Flask route
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ userInput: userInput })
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
        // You can update your chat-log with the response here
    })
    .catch((error) => {
        console.error('Error:', error);
    });
    
    // Process the user input here
    console.log(userInput); // Just a placeholder action

    // Clear the input field after the message is sent
    document.getElementById('user-input').value = '';
});



