import { fetchDashboardData } from "./api.js";
const usersContainer = document.getElementById("users");
const postsContainer = document.getElementById("posts");
const refreshBtn = document.getElementById("refreshBtn");
function displayUsers(users) {
    usersContainer.innerHTML = "";
    users.forEach(user => {
        const card = document.createElement("article");
        card.className = "card";
        const name = document.createElement("h3");
        name.textContent = user.name;

        const email = document.createElement("p");
        email.textContent = `Email: ${user.email}`;

        const city = document.createElement("p");
        city.textContent = `City: ${user.address.city}`;

        card.append(name, email, city);
        usersContainer.appendChild(card);
    });
}
function displayPosts(posts) {
    postsContainer.innerHTML = "";

    posts.slice(0, 10).forEach(post => {
        const card = document.createElement("article");
        card.className = "card";

        const title = document.createElement("h3");
        title.textContent = post.title;

        const description = document.createElement("p");
        description.textContent = post.body;

        card.append(title, description);
        postsContainer.appendChild(card);
    });
}


async function loadDashboard() {

    usersContainer.innerHTML =
        '<p class="loading">Loading users...</p>';

    postsContainer.innerHTML =
        '<p class="loading">Loading posts...</p>';


    refreshBtn.disabled = true;
    refreshBtn.textContent = "Loading...";

    try {

        const { users, posts } = await fetchDashboardData();


        displayUsers(users);
        displayPosts(posts);

    } catch (error) {

        usersContainer.innerHTML = "";

        postsContainer.innerHTML = "";

        const usersError = document.createElement("p");
        usersError.className = "error";
        usersError.textContent =
            `Could not load users: ${error.message}`;

        const postsError = document.createElement("p");
        postsError.className = "error";
        postsError.textContent =
            `Could not load posts: ${error.message}`;

        usersContainer.appendChild(usersError);
        postsContainer.appendChild(postsError);

        console.error("Dashboard error:", error);

    } finally {

        refreshBtn.disabled = false;
        refreshBtn.textContent = "Refresh Data";
    }
}

refreshBtn.addEventListener("click", loadDashboard);

loadDashboard();


