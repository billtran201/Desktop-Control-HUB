//#region Activity / Idle Handling
let idleTime = 0;
const idleThreshold = 60000;

function resetIdleTime() {
    idleTime = 0;
}

function handleIdle() {
    document.body.classList.add('background-idle'); // Add background-idle class to body element
}

function handleActivity() {
    resetIdleTime();
    document.body.classList.remove('background-idle'); // Remove background-idle class from body element
}

document.addEventListener("mousemove", handleActivity);
document.addEventListener("keypress", handleActivity);

setInterval(function() {
    idleTime += 1000; // Increment idle time every second

    if (idleTime >= idleThreshold) {
        handleIdle();
    }
}, 1000);
//#endregion

//#region Add event listener to close window button
document.addEventListener('DOMContentLoaded', function() {
    // Find the button by its ID
    const closeButton = document.getElementById('closeAppButton');
    
    // Add click event listener to the button
    closeButton.addEventListener('click', function() {
        // Close the Electron app

        window.close();
    });

});
//#endregion

document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('shutdownButton').addEventListener('click', function() {
        fetch('http://localhost:5000/shutdown', { method: 'POST' })
            .then(response => {
                if (response.ok) {
                    alert('Shutdown command sent!');
                } else {
                    alert('Failed to send shutdown command.');
                }
            })
            .catch(error => {
                console.error('Error:', error);
                alert('Error sending shutdown command.');
            });
    });
});
