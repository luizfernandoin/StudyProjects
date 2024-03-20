const taskList = document.getElementById("taskList");
const taskInput = document.getElementById("taskInput");
const dataHora = document.getElementById("dataHora");

const listaEventos = [];

function adicionarEvento(taskInput, dataHora) {
    if (taskInput && dataHora) {
        const evento = {
            nome: taskInput,
            dataHora: new Date(dataHora)
        };

        listaEventos.push(evento);
        listaEventos.sort((a, b) => a.dataHora - b.dataHora);

        atualizarEventos();
    }
}

function atualizarEventos() {
    taskList.replaceChildren();

    listaEventos.forEach(evento => {
        const taskItem = document.createElement("li");
        taskItem.className = "taskItem";
        const taskTextElement = document.createElement("span");

        const dataHoraFormatada = evento.dataHora.toLocaleString();
        taskTextElement.textContent = `${evento.nome} - ${dataHoraFormatada}`;

        taskItem.appendChild(taskTextElement);
        taskList.appendChild(taskItem);
    });
}

function verificaEntrada() {
    if (taskInput.value.trim() !== "" && dataHora.value !== "") {
        adicionarEvento(taskInput.value, dataHora.value);
        taskInput.value = "";
        dataHora.value = "";
    }
}


document.querySelector(".btn").addEventListener('click', () => {
    verificaEntrada();
});

taskInput.addEventListener("keydown", function (event) {
    if (event.key === "Enter") verificaEntrada();
});

dataHora.addEventListener("keydown", function (event) {
    if (event.key === "Enter") verificaEntrada();
});