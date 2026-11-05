const API_URL = "http://127.0.0.1:8000";


async function apiRequest(endpoint, options = {}) {

    const token = sessionStorage.getItem("access");

    const response = await fetch(`${API_URL}${endpoint}`, {

        ...options,

        headers: {

            "Content-Type": "application/json",

            ...(token && {
                "Authorization": `Bearer ${token}`
            }),

            ...options.headers

        }

    });

    const data = await response.json();

    if (!response.ok) {
        throw new Error(data.detail || "API request failed");
    }

    return data;
}