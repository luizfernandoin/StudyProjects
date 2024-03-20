
const ConverterDistancia = () => {
	event.preventDefault();
    const num1 = parseInt(document.getElementById('numero1').value)
    const num2 = parseInt(document.getElementById('numero2').value)

    if (num1 % num2 === 0) {
        swal.fire({
            position: 'center',
            icon: 'success',
            title: `O número ${num1} é multiplo de ${num2}!`
        })
    }
    else if (num1 % num2 !== 0) {
        swal.fire({
            position: 'center',
            icon: 'success',
            title: `O número ${num1} não é multiplo de ${num2}!`
        })
    }
}
document.querySelector('.submit-btn').addEventListener('click', ConverterDistancia)