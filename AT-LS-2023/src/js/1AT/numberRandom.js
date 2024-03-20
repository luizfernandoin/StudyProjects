let ulAtual = document.querySelector('.list-container');
const listMainElement = document.querySelector('.list-main');

function gerarNumero() {
    const alturaDaUL = ulAtual.offsetHeight;
    const alturaDoListMain = listMainElement.offsetHeight;

    const novoLi = document.createElement('li');
    novoLi.classList.add("list-item");
    let num = Math.round(Math.random() * 100);
    novoLi.textContent = `${num}`;

    if (alturaDaUL <= alturaDoListMain) {
        ulAtual.appendChild(novoLi);
    } else {
        const novaUl = document.createElement('ul');
        novaUl.classList.add("list-container");
        novaUl.appendChild(novoLi);

        ulAtual.parentNode.appendChild(novaUl);

        ulAtual = novaUl;
    }
}

document.querySelector('.btn').addEventListener('click', gerarNumero);
