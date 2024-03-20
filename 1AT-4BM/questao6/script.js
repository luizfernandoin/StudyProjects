//(TC × 9/5) + 32 = TF
//TC + 273,15 = TK


//Escreva um programa que leia três números inteiros e calcule a sua média aritmética.
const CalcularTemp = () => {
	event.preventDefault();
    const tc = Number(document.getElementById('tc').value)

    
    let tf = (tc * 9/5) + 32
    let tk = tc + 273.15

    swal.fire({
        position: 'center',
        icon: 'success',
        title: `T. Celsius: ${tc}°C
        T. Fahrenheit: ${tf}°F
        T. Kelvin: ${tk}°K`
    })
}
document.querySelector('.submit-btn').addEventListener('click', CalcularTemp)