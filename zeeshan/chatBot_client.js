const box = document.getElementById('box');
const socket = io();
const form = document.getElementById('form');
const button = document.getElementById('submit');
const activeUsertag = document.getElementById('activeUser')


// const getOtpBtn = document.getElementById('getOtpBtn');
// getOtpBtn.addEventListener('click', async () => {
//     const email = document.getElementById('email').value;
//     const response = await fetch('/send-otp', {
//         method: 'POST',
//         headers: {
//             'Content-Type': 'application/json'
//         },
//         body: JSON.stringify({ email: email })
//     });
//     if (response.ok) {
//         console.log('OTP sent successfully');
//         // After OTP is sent successfully, show the OTP input field
//         document.getElementById('otp').style.display = 'block';
//     } else {
//         console.error('Failed to send OTP');
//     }
// });


// const otpCheck = document.getElementById('otp').value



// Fetch user details and display them here we are just asking for the user detail to make them display also 
async function getUserDetail() {
    try {
        const response = await fetch('/getUserDetail');
        const data = await response.json();
        activeUsertag.innerHTML += '<br> Active User: ' + data.name + '<br>';
    } catch (error) {
        console.error('Error fetching user details:', error);
    }
}

getUserDetail();

box.innerHTML += 'Hi, how are you? I am a box and I am connected here<br>';

// Fetch active user count and display it
async function getActiveUserCount() {
    try {
        const response = await fetch('/getActiveUser');
        const data = await response.json();
        activeUsertag.innerHTML += '<br> Current No of Active User Count: ' + data + '<br>';
    } catch (error) {
        console.error('Error fetching active user count:', error);
    }
}

getActiveUserCount();


var UserName;


button.addEventListener('click', (e) => {
    e.preventDefault();


    async function getUserName() {
        const res = await fetch('/getUserName');
        UserName = await res.json();
    }

    getUserName()


    const msg = form.value;

    // Create a new message element 
    //This is the new message element which we have created to diplay 
    const messageElement = document.createElement('div');
    messageElement.classList.add('message');

    messageElement.textContent = msg;
    messageElement.id = 'sent-message'; // Add id for CSS styling

    // Append the message to the chat box
    box.appendChild(messageElement);

    // Emit the message to the server
    socket.emit('message_client', msg);
});

// Listen for incoming messages from the server
socket.on('message_server', (msg) => {
    const messageElement = document.createElement('div');
    messageElement.classList.add('message');
    contentMessage = UserName + ' : ' + msg
    messageElement.textContent = contentMessage;
    messageElement.id = 'received-message'; // Add id for CSS styling
    box.appendChild(messageElement);
});
