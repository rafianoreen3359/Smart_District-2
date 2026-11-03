const taskForm = document.getElementById("task-form");
const taskInput = document.getElementById("task-input");
const taskList = document.getElementById("task-list");
const filters = document.getElementById("filters");
const taskCount = document.getElementById("task-count");

let tasks = JSON.parse(localStorage.getItem("tasks")) || [];
let currentFilter = "all";

function saveTasks() {
    localStorage.setItem("tasks", JSON.stringify(tasks));
}

function showTasks() {
    taskList.innerHTML = "";

    let filteredTasks = tasks;

    if (currentFilter === "active") {
        filteredTasks = tasks.filter(task => !task.completed);
    } else if (currentFilter === "completed") {
        filteredTasks = tasks.filter(task => task.completed);
    }

    filteredTasks.forEach(task => {
        let li = document.createElement("li");
        let span = document.createElement("span");
        let completeBtn = document.createElement("button");
        let deleteBtn = document.createElement("button");

        li.className = "task-item";

        if (task.completed) {
            li.classList.add("completed");
        }

        span.textContent = task.text;
        span.className = "task-text";

        completeBtn.textContent = task.completed ? "Undo" : "Complete";
        completeBtn.dataset.id = task.id;
        completeBtn.dataset.action = "toggle";
        completeBtn.className = "complete-btn";

        deleteBtn.textContent = "Delete";
        deleteBtn.dataset.id = task.id;
        deleteBtn.dataset.action = "delete";
        deleteBtn.className = "delete-btn";

        li.append(span, completeBtn, deleteBtn);
        taskList.appendChild(li);
    });

    let remaining = tasks.filter(task => !task.completed).length;
    taskCount.textContent = remaining + " tasks left";
}

taskForm.addEventListener("submit", function(event) {
    event.preventDefault();

    let text = taskInput.value.trim();

    if (text === "") {
        alert("Hey! Rafia Noreen Please enter a task!");
        return;
    }

    let task = {
        id: Date.now().toString(),
        text: text,
        completed: false
    };

    tasks.push(task);

    saveTasks();
    showTasks();

    taskInput.value = "";
});

taskList.addEventListener("click", function(event) {
    let id = event.target.dataset.id;
    let action = event.target.dataset.action;

    if (!id) {
        return;
    }

    if (action === "toggle") {
        tasks = tasks.map(task => {
            if (task.id === id) {
                task.completed = !task.completed;
                alert("Congratulations you completed your task!");
            }

            return task;
        });
    }

    if (action === "delete") {
        tasks = tasks.filter(task => task.id !== id);
        alert("Ohh! You Delete your task!");
    }

    saveTasks();
    showTasks();
});

filters.addEventListener("click", function(event) {
    if (!event.target.dataset.filter) {
        return;
    }

    currentFilter = event.target.dataset.filter;

    document.querySelectorAll("#filters button").forEach(button => {
        button.classList.remove("active");
    });

    event.target.classList.add("active");

    showTasks();
});

showTasks();
