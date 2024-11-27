document.addEventListener('DOMContentLoaded', () => {
    const userName = localStorage.getItem('userName');
    const userEmail = localStorage.getItem('userEmail');
    const userPassword = localStorage.getItem('userPassword');

    if (!userName || !userEmail || !userPassword) {
        // Redirect to sign-up page if user data does not exist
        window.location.href = 'signup.html';
    } else {
        // Redirect to login page if user data exists
        window.location.href = 'login.html';
    }
});
