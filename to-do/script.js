const input = document.getElementById("input");
const form = document.getElementById("form");
const list = document.getElementById("to-do");

form.addEventListener("submit", (e) => {
    e.preventDefault();

    const li = document.createElement("li");
    li.textContent = input.value;

    list.appendChild(li);

    input.value = "";
})