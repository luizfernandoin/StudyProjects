const descricao = document.getElementById("descricao");
const valorTransacao = document.getElementById("valor-transacao");
const transactionTableBody = document.getElementById("transactionTableBody");
const saldoTotal = document.getElementById("saldoTotal");
const btnDepositar = document.querySelector(".btn-depositar");
const btnSacar = document.querySelector(".btn-sacar");


const transacoes = [];

class Transacao {
    constructor(descricao, valor) {
        this.descricao = descricao;
        this.valor = parseFloat(valor);
    }

    calcularSaldo() {
        const saldo = transacoes.reduce((total, transacao) => total + transacao.valor, 0);
        saldoTotal.textContent = saldo.toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' });
    }
}

function adicionarTransacao(descricao, valor) {
    if (!descricao || isNaN(valor)) {
        Swal.fire('Erro', 'Por favor, preencha todos os campos corretamente.', 'error');
    } else {
        const transacao = new Transacao(descricao, valor);
        transacoes.push(transacao);
        renderizarTabela(transacao);
        transacao.calcularSaldo();
    }
}

function renderizarTabela(transacao) {
    const row = document.createElement('tr');
    const cellDescricao = document.createElement('td');
    cellDescricao.textContent = transacao.descricao;
    cellDescricao.classList.add('descricao');
    const cellValor = document.createElement('td');
    cellValor.textContent = transacao.valor.toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' });

    if (transacao.valor < 0) {
        cellValor.classList.add('despesa');
    } else {
        cellValor.classList.add('receita');
    }

    row.appendChild(cellDescricao);
    row.appendChild(cellValor);
    transactionTableBody.appendChild(row);
}


function limparCampos() {
    descricao.value = '';
    valorTransacao.value = '';
}

function mensagem(mensagem, status) {
    Swal.fire(status.charAt(0).toUpperCase() + status.slice(1), mensagem,`${status.toLowerCase()}r`);
}


btnDepositar.addEventListener('click', () => {
    const descricaoTransacao = descricao.value;
    const valor = parseFloat(valorTransacao.value);
    
    (valor < 0) ? mensagem("O valor do deposito não pode ser negativo!", "erro") : adicionarTransacao(descricaoTransacao, valor);
    limparCampos();
});

btnSacar.addEventListener('click', () => {
    const descricaoTransacao = descricao.value;
    let valor = -parseFloat(valorTransacao.value);

    if (valor > 0) valor = -valor;

    adicionarTransacao(descricaoTransacao, valor);
    limparCampos();
});