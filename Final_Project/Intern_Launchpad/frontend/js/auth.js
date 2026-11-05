const API_URL = "http://127.0.0.1:8000";

const loginForm = document.getElementById("loginForm");

loginForm.addEventListener("submit", async function (event) {

    event.preventDefault();

    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    const message = document.getElementById("message");

    try {

        const response = await fetch(`${API_URL}/api/token/`, {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                username: username,
                password: password
            })

        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.detail || "Login failed");
        }

        // Store tokens for this learning prototype
        sessionStorage.setItem("access", data.access);
        sessionStorage.setItem("refresh", data.refresh);

        message.textContent = "Login successful!";

        window.location.href = "profile.html";

    }

    catch (error) {

        message.textContent = error.message;
        message.className = "text-red-600 text-center mt-4";

    }

});