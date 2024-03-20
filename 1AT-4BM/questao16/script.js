
const AnalisarNúmero = () => {
	event.preventDefault();
    const numeros = {
        num1: parseInt(document.getElementById('numero1').value),
        num2: parseInt(document.getElementById('numero2').value),
        num3: parseInt(document.getElementById('numero3').value),
    }
    
    let maior = 0

    if (numeros.num1 >= numeros.num2 && numeros.num1 >= numeros.num3) {
        maior = numeros.num1
    }
    else if (numeros.num2 >= numeros.num1 && numeros.num2 >= numeros.num3) {
        maior = numeros.num2
    }
    else if (numeros.num3 >= numeros.num2 && numeros.num3 >= numeros.num1) {
        maior = numeros.num3
    }

    swal.fire({
        position: 'center',
        icon: 'success',
        title: `O maior número digitado foi ${maior}`
    })
}
document.querySelector('.submit-btn').addEventListener('click', AnalisarNúmero)