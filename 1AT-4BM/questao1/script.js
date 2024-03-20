//Escreva um programa que leia três números inteiros e calcule a sua média aritmética.
const CalcularMedia = () => {
	event.preventDefault();
	let numeros = {
		numero1: parseInt(document.getElementById("numero1").value),
		numero2: parseInt(document.getElementById("numero2").value),
		numero3: parseInt(document.getElementById("numero3").value),
	};

    let media = (numeros.numero1 + numeros.numero2 + numeros.numero3) / 3
    swal.fire({
        position: 'center',
        icon: 'success',
        title: `A média dos números digitados é ${media}!`,
    })
}
document.querySelector('.submit-btn').addEventListener('click', CalcularMedia)