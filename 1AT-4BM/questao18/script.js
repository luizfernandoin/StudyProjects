
const AnalisarNúmero = () => {
	event.preventDefault();
    
    num1 = parseInt(document.getElementById('numero1').value)
    num2 = parseInt(document.getElementById('numero2').value)
    num3 = parseInt(document.getElementById('numero3').value)


    if (num1 > num2 && num1 < num3 || num1 > num3 && num1 < num2) {
        intermediario = num1
        swal.fire({
            position: 'center',
            icon: 'success',
            title: `Número Intermediario: ${num1}`
        })
    }
    else if (num2 > num1 && num2 < num3 || num2 > num3 && num2 < num1) {
        intermediario = num2
        swal.fire({
            position: 'center',
            icon: 'success',
            title: `Número Intermediario: ${num2}`
        })
    }
    else if (num3 > num1 && num3 < num2 || num3 > num2 && num3 < num1) {
        intermediario = num3
        swal.fire({
            position: 'center',
            icon: 'success',
            title: `Número Intermediario: ${num3}`
        })
    }
    else {
        swal.fire({
            position: 'center',
            icon: 'success',
            title: `Não possuem intermediarios.`
        })
    }

}
document.querySelector('.submit-btn').addEventListener('click', AnalisarNúmero)