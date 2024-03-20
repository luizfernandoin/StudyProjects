//Escreva um programa que leia três números inteiros e calcule a sua média aritmética.
const AnalisarNumero = () => {
	event.preventDefault();
    let num = Number(document.getElementById('numero').value)

	let dados_numero = {
        dobro: num * 2,
        triplo: num * 3,
        quadrado: Math.pow(num, 2),
        cubo: Math.pow(num, 3),
        raiz: Math.sqrt(num)
	};

    swal.fire({
        position: 'center',
        icon: 'success',
        title: `Número: ${num}
        Dobro: ${dados_numero.dobro}
        Triplo: ${dados_numero.triplo}
        Quadrado: ${dados_numero.quadrado}
        Cubo: ${dados_numero.cubo}
        Raiz: ${dados_numero.raiz}`
    })
}
document.querySelector('.submit-btn').addEventListener('click', AnalisarNumero)