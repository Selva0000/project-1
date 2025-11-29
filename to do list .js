function addTask() {
    let input = document.getElementById("taskInput");
    let taskText = input.value.trim();

    if (taskText === "") return;

    let li = document.createElement("li");
    li.textContent = taskText;

    // Toggle completion when clicking the task
    li.addEventListener("click", function () {
        this.classList.toggle("completed");
    });

    // Remove button
    let removeBtn = document.createElement("button");
    removeBtn.textContent = "❌";
    removeBtn.onclick = function () {
        this.parentElement.remove();
    };

    li.appendChild(removeBtn);
    document.getElementById("taskList").appendChild(li);

    input.value = "";
}
