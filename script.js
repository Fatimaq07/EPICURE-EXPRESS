document.addEventListener('DOMContentLoaded', () => {
    // Get the buttons
    const loginBtn = document.getElementById('login-btn');
    const signupBtn = document.getElementById('signup-btn');
    
    // Redirect to login.html on click (if you want to use JavaScript for this)
    loginBtn.addEventListener('click', (event) => {
        // Prevent default behavior (if necessary)
        event.preventDefault();
        window.location.href = 'login.html';
    });

    // Redirect to signup.html on click (if you want to use JavaScript for this)
    signupBtn.addEventListener('click', (event) => {
        // Prevent default behavior (if necessary)
        event.preventDefault();
        window.location.href = 'signup.html';
    });
});
