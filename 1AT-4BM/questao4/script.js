//Escreva um programa que leia o valor do raio de uma circunferência e calcule a sua área e o seu comprimento.
//pi = 3.14159265359
//A = pi * Math.pow(r, 2)
//A = pi * Math.pow(d/2, 2)

//Escreva um programa que leia três números inteiros e calcule a sua média aritmética.
const CalcularCircunferencia = () => {
	event.preventDefault();
    let medida = Number(document.getElementById('medida').value)
    let pi = 3.14159265359
    let raio = 0


    if (document.getElementById('unidade').value === 'Raio') {
        raio = medida}
    else if (document.getElementById('unidade').value === 'Diametro') {
        raio = medida / 2
    }
    
    let perimetro = 2 * pi * raio
    let area = pi * Math.pow(raio, 2)

    swal.fire({
        position: 'center',
        icon: 'success',
        title: `Área: ${area}
        Perimetro: ${perimetro}`
    })
}
document.querySelector('.submit-btn').addEventListener('click', CalcularCircunferencia)