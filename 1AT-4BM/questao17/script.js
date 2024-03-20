
const AnalisarNúmero = () => {
	event.preventDefault();
    const numeros = {
        num1: parseInt(document.getElementById('numero1').value),
        num2: parseInt(document.getElementById('numero2').value),
        num3: parseInt(document.getElementById('numero3').value),
    }
    
    let maior = 0
    let menor = 0

    if (numeros.num1 >= numeros.num2 && numeros.num1 >= numeros.num3) {
        maior = numeros.num1
        if (numeros.num2 >= numeros.num3) {
            menor = numeros.num3
        }
        else {
            menor = numeros.num2
        }
    }
    else if (numeros.num2 >= numeros.num1 && numeros.num2 >= numeros.num3) {
        maior = numeros.num2
        if (numeros.num1 >= numeros.num3) {
            menor = numeros.num3
        }
        else {
            menor = numeros.num1
        }
    }
    else if (numeros.num3 >= numeros.num2 && numeros.num3 >= numeros.num1) {
        maior = numeros.num3
        if (numeros.num2 >= numeros.num1) {
            menor = numeros.num1
        }
        else {
            menor = numeros.num2
        }
    }

    swal.fire({
        position: 'center',
        icon: 'success',
        title: `O maior número digitado foi ${maior} e o menor foi ${menor}`
    })
}
document.querySelector('.submit-btn').addEventListener('click', AnalisarNúmero)