// Fetch todos from backend
async function loadTodos() {
    let res = await fetch("/todos");
    let todos = await res.json();

    const list = document.getElementById("todoList");
    list.innerHTML = "";

    todos.forEach(todo => {
        let li = document.createElement("li");

        li.className = todo.completed ? "completed" : "";

        li.innerHTML = `
            <span onclick="toggleTodo(${todo.id})">${todo.task}</span>
            <button onclick="deleteTodo(${todo.id})">Delete</button>
        `;

        list.appendChild(li);
    });
}

// Add todo
async function addTodo() {
    const task = document.getElementById("todoInput").value;
    if (!task) return alert("Enter task");

    await fetch("/add", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({task})
    });

    document.getElementById("todoInput").value = "";
    loadTodos();
}

// Delete todo
async function deleteTodo(id) {
    await fetch(`/delete/${id}`, {method: "DELETE"});
    loadTodos();
}

// Toggle complete
async function toggleTodo(id) {
    await fetch(`/toggle/${id}`, {method: "PUT"});
    loadTodos();
}

loadTodos();
