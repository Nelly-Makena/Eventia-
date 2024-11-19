document.addEventListener("DOMContentLoaded", function () {
    const passwordInput = document.getElementById("password");
    const confirmPasswordInput = document.getElementById("confirm-password");
    const passwordHelp = document.getElementById("password-help");
    const confirmPasswordHelp = document.getElementById("confirm-password-help");

    // Password validation logic
    passwordInput.addEventListener("input", function () {
        const password = passwordInput.value;
        let message = "";
        if (password.length < 8) {
            message = "Password must be at least 8 characters long.";
        } else if (!/[A-Z]/.test(password)) {
            message = "Password must contain at least one uppercase letter.";
        } else if (!/[a-z]/.test(password)) {
            message = "Password must contain at least one lowercase letter.";
        } else if (!/\d/.test(password)) {
            message = "Password must contain at least one number.";
        } else if (!/[!@#$%^&*(),.?":{}|<>]/.test(password)) {
            message = "Password must contain at least one special character.";
        } else {
            message = "Password is valid.";
        }
        passwordHelp.textContent = message;
        passwordHelp.style.color = message === "Password is valid." ? "green" : "red";
    });

    // Confirm password validation
    confirmPasswordInput.addEventListener("input", function () {
        if (confirmPasswordInput.value !== passwordInput.value) {
            confirmPasswordHelp.textContent = "Passwords do not match.";
            confirmPasswordHelp.style.color = "red";
        } else {
            confirmPasswordHelp.textContent = "Passwords match.";
            confirmPasswordHelp.style.color = "green";
        }
    });
});
