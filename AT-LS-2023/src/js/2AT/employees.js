const nameEmployee = document.getElementById("nameEmployee");
const salaryEmployee = document.getElementById("salaryEmployee");
const employeeList = document.querySelector(".employees-container");
const nameMaxSalary = document.getElementById("nameMaxSalary");
const totalSalaryElement = document.getElementById("totalSalary");

const employees = [];

function addEmployee() {
    const name = nameEmployee.value;
    const salary = parseFloat(salaryEmployee.value);

    if (name && !isNaN(salary)) {
        const employee = { name, salary };
        employees.push(employee);

        const card = document.createElement('li');
        card.classList.add('employee-post');
        card.innerHTML = `
            <div class="data-event">
                <h3>${name}</h3>
            </div>
            <div class="main-event">
                <p class="event-meta">
                    ${salary.toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' })}
                </p>
            </div>
        `;

        employeeList.appendChild(card);

        nameEmployee.value = "";
        salaryEmployee.value = "";

        updateNameMaxSalary();
        updateTotalSalary();
    }
}

function updateNameMaxSalary() {
    const employeeWithMaxSalary = employees.reduce((max, employee) => (max.salary > employee.salary ? max : employee), employees[0]);
    nameMaxSalary.textContent = employeeWithMaxSalary.name;
}

function updateTotalSalary() {
    const totalSalary = employees.reduce((total, employee) => total + employee.salary, 0);
    totalSalaryElement.textContent = totalSalary.toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' });
}

document.querySelector(".btn").addEventListener("click", addEmployee);
