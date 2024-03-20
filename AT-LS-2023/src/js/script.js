const listaDeExercicios = {
    lista01: [
        "Lista de exercícios 01 - Funções",
        {
            titulo: "Gerador de Números",
            descricao: "Este programa cria um botão 'Gerar' que, quando clicado, gera números aleatórios entre 1 e 100 e os exibe na página.",
            link: "templates/1AT/numberRandom.html",
        },
        {
            titulo: "Calcular Potencias",
            descricao: "Realiza calculos de potências de um número informado como base, elevado a um expoente também informado, ao clicar no botão 'Calcular'.",
            link: "templates/1AT/potencia.html",
        },
        {
            titulo: "Melhor Combustível",
            descricao: "Informa ao usuário se é mais vantajoso abastecer com gasolina ou álcool, com base nos valores inseridos.",
            link: "templates/1AT/combustivel.html",
        },
        {
            titulo: "Conversor de Temperatura",
            descricao: "Este projeto converte temperaturas de Celsius para Fahrenheit e Kelvin em tempo real enquanto o usuário digita um valor no campo de texto.",
            link: "templates/1AT/temperatura.html",
        },
        {
            titulo: "Contador de Números",
            descricao: "Simulação de um rolamento de dados (1 a 6) um milhão de vezes e exibe a contagem de cada número após a simulação.",
            link: "templates/1AT/contagem.html",
        },
    ],
    lista02: [
        "Lista de exercícios 02 - Arrays",
        {
            titulo: "Maior e Menor Número",
            descricao: "Programa responsavel por identificar o maior e menor número em uma lista separada por determinado simbolo informado pelo usuario.",
            link: "templates/2AT/bigger_smaller.html",
        },
        {
            titulo: "TO DO List",
            descricao: "O usuario poderá adicionar tarefas e remove-las a qualquer momento.",
            link: "templates/2AT/to_do_list.html",
        },
        {
            titulo: "Cinema",
            descricao: "Exibe e filtra uma série de filmes armazenados em um objeto.",
            link: "templates/2AT/filter_movies.html",
        },
        {
            titulo: "Funcionarios",
            descricao: "Programa para armazenar os funcionarios de uma empresa e seus respectivos salarios.",
            link: "templates/2AT/employees.html",
        },
    ],
    lista03: [
        "Lista de exercícios 03 - Classes e Objetos",
        {
            titulo: "Lista de Eventos",
            descricao: "Insira seus eventos e respectivas data e hora, ele será exibido em ordem cronológica na tela.",
            link: "templates/3AT/event.html",
        },
        {
            titulo: "Banco de Clientes",
            descricao: "Adicione e liste clientes de um banco, onde o mesmo terá nome, saldo e documento e conseguirá realizar saques e depósitos.",
            link: "templates/3AT/banco_clientes.html",
        },
        {
            titulo: "Controle de Transações",
            descricao: "Projeto para realizar transações com descrições e valor realizando verificações no saldo da conta.",
            link: "templates/3AT/transacoes.html",
        },
    ],
    lista04: [
        "Lista de exercícios 04 - Modularidade/Armazenamento",
        {
            titulo: "Supermercado",
            descricao: "Página para construir lista de compras do supermercado, onde pode-se inserir itens, remover e marcar quando comprado.",
            link: "templates/4AT/supermercado.html",
        },
    ],
};


const containerMain = document.querySelector(".main-container");

for (prop in listaDeExercicios) {
    const section = document.createElement("section");
    section.className = "container-grid";

    const divBlckContent = document.createElement("div");
    divBlckContent.className = "blck-content-atv";

    listaDeExercicios[prop].forEach((element, index) => {
        if (index === 0){
            const h2 = document.createElement("h2");
            h2.className = "titleSection";
            h2.textContent = element;
            section.appendChild(h2);
        } else {
            const divPost = document.createElement("div");
            divPost.className = "post-index";
            divPost.innerHTML = `
                <a href="${element.link}">
                    <h3 class="title-new">${element.titulo}s</h3>
                    <p class="desc-new">${element.descricao}</p>
                </a>
            `;

            divBlckContent.appendChild(divPost);
        }
    });

    section.appendChild(divBlckContent);
    containerMain.appendChild(section);
};