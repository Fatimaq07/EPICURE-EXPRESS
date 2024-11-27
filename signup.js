document.addEventListener('DOMContentLoaded', () => {
    const signupForm = document.getElementById('signupForm');

    signupForm.addEventListener('submit', (event) => {
        event.preventDefault();

        // Get form data
        const name = document.getElementById('name').value;
        const email = document.getElementById('email').value;
        const password = document.getElementById('password').value;
        const phone = document.getElementById('phone').value;

        // Save user data in local storage
        localStorage.setItem('userName', name);
        localStorage.setItem('userEmail', email);
        localStorage.setItem('userPassword', password);
        localStorage.setItem('userPhone', phone);

        // Redirect to login page
        window.location.href = 'login.html';
    });
});
