import listaDeCompras from './lista.js';

const itemInput = document.getElementById('itemInput');
const priceInput = document.getElementById('priceInput');
const listaItens = document.getElementById('listaItens');

window.onload = (event) => {
    atualizarLista();
}

function atualizarLista() {
    listaItens.innerHTML = '';

    listaDeCompras.listar().forEach(item => {
        const row = document.createElement('tr');
        const compradoCheckbox = document.createElement('input');
        compradoCheckbox.type = 'checkbox';
        compradoCheckbox.checked = item.comprado;

        compradoCheckbox.addEventListener('change', () => {
            console.log("clicou")
            if (compradoCheckbox.checked) {
                listaDeCompras.marcar(item);
            } else {
                listaDeCompras.desmarcar(item);
            }
            atualizarLista();
        });
        
        const nome = document.createElement('td');
        nome.textContent = `${item.codigoBarra} ${item.nome}`;
        const preco = document.createElement('td');
        preco.textContent = `R$ ${item.preco.toFixed(2)}`;
        const comprado = document.createElement('td');
        comprado.appendChild(compradoCheckbox);
        const remover = document.createElement('td');
        const btnRemover = document.createElement('button');
        btnRemover.className = 'removeButton';
        btnRemover.textContent = 'Remover';
        remover.appendChild(btnRemover);

        row.appendChild(nome);
        row.appendChild(preco);
        row.appendChild(comprado);
        row.appendChild(remover);

        const removeButton = row.querySelector('.removeButton');
        removeButton.addEventListener('click', () => {
            listaDeCompras.remover(item);
            atualizarLista();
        });

        listaItens.appendChild(row);
    });
}

function setCampos() {
    itemInput.value = '';
    priceInput.value = '';
}

function verificaEntrada() {
    const nome = itemInput.value;
    const preco = parseFloat(priceInput.value);

    if (nome && preco) {
        const novoItem = {
            codigoBarra: Date.now(),
            nome,
            preco,
            comprado: false,
        };
        listaDeCompras.adicionar(novoItem);
        setCampos();
        atualizarLista();
    }
}

document.querySelector('.btn').addEventListener('click', () => {
    verificaEntrada();
});

itemInput.addEventListener("keydown", function (event) {
    if (event.key === "Enter") verificaEntrada();
});

priceInput.addEventListener("keydown", function (event) {
    if (event.key === "Enter") verificaEntrada();
});