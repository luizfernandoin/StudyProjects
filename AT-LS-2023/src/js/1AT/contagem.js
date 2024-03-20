function simularRolamentoDados(totSimulacoes) {
    const contagem = {};

    for (let i = 0; i < totSimulacoes; i++) {
        const resultadoDoDado = Math.floor(Math.random() * 6) + 1;
        if (contagem[resultadoDoDado] === undefined) {
            contagem[resultadoDoDado] = 1;
        } else {
            contagem[resultadoDoDado]++;
        }
    }

    return contagem;
}

function exibirResultado(resultado) {
    const resultadoDiv = document.querySelector('.result');
    resultadoDiv.innerHTML = '';

    for (const numero in resultado) {
        if (resultado.hasOwnProperty(numero)) {
            const contagem = resultado[numero];
            const div = document.createElement('div');
            div.classList.add("value");
            div.textContent = `Número ${numero}: ${contagem} vezes`;
            document.querySelector(".result").classList.add("show")
            resultadoDiv.appendChild(div);
        }
    }
}

document.querySelector('.btn').addEventListener('click', function() {
    const resultado = simularRolamentoDados(1000000);
    exibirResultado(resultado);
});