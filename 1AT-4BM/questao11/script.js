
const VerificarNumero = () => {
	event.preventDefault();
    const numero = parseInt(document.getElementById('numero').value)

    if (numero % 2 === 0) {
        swal.fire({
            position: 'center',
            icon: 'success',
            title: `O número ${numero} é par!`
        })
    }
    else if (numero % 2 === 1) {
        swal.fire({
            position: 'center',
            icon: 'success',
            title: `O número ${numero} é impar!`
        })
    }
}
document.querySelector('.submit-btn').addEventListener('click', VerificarNumero)