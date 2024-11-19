function togglePassword(fieldId) {
    const passwordField = document.getElementById(fieldId);
    const type = passwordField.type === "password" ? "text" : "password";
    passwordField.type = type;
}
