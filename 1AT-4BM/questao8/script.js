//Escreva um programa que leia o valor do raio de uma circunferência e calcule a sua área e o seu comprimento.
//pi = 3.14159265359
//A = pi * Math.pow(r, 2)
//A = pi * Math.pow(d/2, 2)

//Escreva um programa que leia três números inteiros e calcule a sua média aritmética.
const ConverterPolegadas = () => {
	event.preventDefault();
    let polegadas = parseInt(document.getElementById('polegadas').value)

    let conversao = polegadas * 2.54

    swal.fire({
        position: 'center',
        icon: 'success',
        title: `Polegadas: ${polegadas}
        Valor em Centimetros: ${conversao}`
    })
}
document.querySelector('.submit-btn').addEventListener('click', ConverterPolegadas)