//Escreva um programa que leia três números inteiros e calcule a sua média aritmética.
const CalcularQuadrado = () => {
	event.preventDefault();
	//let dados = {
	//	unidade: document.getElementById("unidade").value,
	//	tamanho: parseInt(document.getElementById("tamanho").value),
	//};
    let lado = document.getElementById('lado').value

    const area = Math.pow(lado, 2)
    const perimetro = lado * 4

    swal.fire({
        position: 'center',
        icon: 'success',
        title: `Lado: ${lado}
        Área: ${area}
        Perimetro: ${perimetro}`,
    })
}
document.querySelector('.submit-btn').addEventListener('click', CalcularQuadrado)