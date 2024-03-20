
const VerificarIdade = () => {
	event.preventDefault();
    const idade = parseInt(document.getElementById('idade').value)


    if (idade < 0) {
        swal.fire({
            position: 'center',
            icon: 'error',
            title: 'Oops...',
            text: `Informe uma idade verdadeira!`
        })
    }
    else if (idade >= 0 && idade <= 12) {
        swal.fire({
            position: 'center',
            icon: 'success',
            title: `Uma pessoa de ${idade} anos é criança.`
        })
    }
    else if (idade >= 13 && idade <= 17) {
        swal.fire({
            position: 'center',
            icon: 'success',
            title: `Uma pessoa de ${idade} anos é adolescente.`
        })
    }
    else if (idade >= 18 && idade <= 59) {
        swal.fire({
            position: 'center',
            icon: 'success',
            title: `Uma pessoa de ${idade} anos é adulta.`
        })
    }
    else {
        swal.fire({
            position: 'center',
            icon: 'success',
            title: `Uma pessoa de ${idade} anos é idosa.`
        })
    }
}
document.querySelector('.submit-btn').addEventListener('click', VerificarIdade)