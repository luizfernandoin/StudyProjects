const nameClient = document.getElementById("nameClient");
const cpfClient = document.getElementById("cpfClient");
const clientsList = document.querySelector(".clients-container");
const btnAdicionar = document.querySelector(".btn-adicionar");
const btnProcurar= document.querySelector(".btn-procurar");


const clients = {};

class ClienteBanco {
    constructor (nome, documento, saldo) {
        this.nome = nome;
        this.documento = documento;
        this.saldo = saldo;
    }
    
    depositar(value) {
        this.saldo += parseFloat(value);
    }

    sacar(value) {
        value = parseFloat(value)
        if (this.saldo >= value) {
            this.saldo -= value;
        }
    }
}

function cpfExiste(cpf) {
    return clients.hasOwnProperty(cpf);
}

function adicionarCliente() {
    const name = nameClient.value;
    const cpf = cpfClient.value;

    if (name && cpf) {
        if (!cpfExiste(cpf)) {
            const cliente = new ClienteBanco(name, cpf, 0);
            clients[cpf] = cliente;
    
            const card = document.createElement('li');
            card.classList.add('employee-post');
            card.innerHTML = `
                <div class="data-event">
                    <h3>${cliente.nome}</h3>
                </div>
                <div class="main-event">
                    <p class="event-meta">
                        ${cliente.saldo.toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' })}
                    </p>
                </div>
            `;
    
            clientsList.appendChild(card);
    
            nameClient.value = "";
            cpfClient.value = "";
        } else {
            Swal.fire('Usuário existente!', 'O cpf informado já possui cadastro em nosso banco.', 'error');
        }
    }
}

function procurarCliente(cpf) {
    if (cpfExiste(cpf)) {
        const cliente = clients[cpf];
        Swal.fire({
            title: 'Escolha uma operação',
            showDenyButton: true,
            confirmButtonText: 'Depositar',
            denyButtonText: 'Sacar',
            html: `
            <input
            type="number"
            class="swal2-input"
            id="range-value"
            placeholder="Informe o valor">`,
        }).then((result) => {
            const valor = Swal.getHtmlContainer().querySelector('#range-value').value;

            if (result.isConfirmed) {
                cliente.depositar(valor);
                Swal.fire('Depósito realizado!', `Valor depositado: ${valor}`, 'success');
            } else if (result.isDenied) {
                if (cliente.saldo >= valor) {
                    cliente.sacar(valor);
                    Swal.fire('Saque realizado!', `Valor sacado: ${valor}`, 'success');
                } else {
                    Swal.fire('Saldo insuficiente', 'O saldo do cliente é insuficiente para realizar o saque.', 'error');
                }
            }
        
            atualizarListaClientes();
        });        
    } else {
        Swal.fire('Cliente não encontrado', 'O CPF informado não corresponde a um cliente.', 'error');
    }
}

function atualizarListaClientes() {
    clientsList.replaceChildren();

    for (const cpf in clients) {
        const cliente = clients[cpf];

        const card = document.createElement('li');
        card.classList.add('employee-post');
        card.innerHTML = `
            <div class="data-event">
                <h3>${cliente.nome}</h3>
            </div>
            <div class="main-event">
                <p class="event-meta">
                    ${cliente.saldo.toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' })}
                </p>
            </div>
        `;

        clientsList.appendChild(card);
    }
}


btnAdicionar.addEventListener("click", adicionarCliente);
btnProcurar.addEventListener("click", () => {
    if (cpfClient.value !== "") {
        procurarCliente(cpfClient.value);
    }
});