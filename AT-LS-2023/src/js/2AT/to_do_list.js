const taskInput = document.getElementById("taskInput");
const taskList = document.getElementById("taskList");

taskInput.addEventListener("keydown", function (event) {
    if (event.key === "Enter" && taskInput.value.trim() !== "") {
        addTask(taskInput.value);
        taskInput.value = "";
    }
});

function addTask(taskText) {
    const taskItem = document.createElement("li");
    taskItem.className = "taskItem";

    const taskTextElement = document.createElement("span");
    taskTextElement.textContent = taskText;

    const removeTask = document.createElement("span");
    removeTask.className = "removeTask";
    removeTask.innerHTML = '<i class="bi bi-x-lg"></i>';

    removeTask.addEventListener("click", function () {
        taskList.removeChild(taskItem);
    });

    taskItem.appendChild(taskTextElement);
    taskItem.appendChild(removeTask);

    taskList.appendChild(taskItem);
}
