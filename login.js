document.getElementById('loginLink').addEventListener('click', function(event) {
    event.preventDefault();
    window.location.href = 'login.html'; // Redirect to the login page
});

document.getElementById('signupLink').addEventListener('click', function(event) {
    event.preventDefault();
    window.location.href = 'signup.html'; // Redirect to the signup page
});
