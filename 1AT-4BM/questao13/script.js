
const VerificarNumero = () => {
	event.preventDefault();
    const numero = parseInt(document.getElementById('numero').value)

    if (numero > 0) {
        swal.fire({
            position: 'center',
            icon: 'success',
            title: `O número ${numero} é positivo.`
        })
    }
    else if (numero === 0) {
        swal.fire({
            position: 'center',
            icon: 'success',
            title: `O número ${numero} é neutro.`
        })
    }
    else {
        swal.fire({
            position: 'center',
            icon: 'success',
            title: `O número ${numero} é negativo.`
        })
    }
}
document.querySelector('.submit-btn').addEventListener('click', VerificarNumero)