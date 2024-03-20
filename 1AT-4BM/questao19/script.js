
const Calcular = () => {
	event.preventDefault();
    
    num1 = parseInt(document.getElementById('numero1').value)
    num2 = parseInt(document.getElementById('numero2').value)
    operador = document.getElementById('operadores').value

    if (operador === '+') {
        resultado = num1 + num2
        swal.fire({
            position: 'center',
            icon: 'success',
            title: `${num1} + ${num2} = ${resultado}`
        })
    }
    else if (operador === '-') {
        resultado = num1 - num2
        swal.fire({
            position: 'center',
            icon: 'success',
            title: `${num1} - ${num2} = ${resultado}`
        })
    }
    else if (operador === '*') {
        resultado = num1 * num2
        swal.fire({
            position: 'center',
            icon: 'success',
            title: `${num1} * ${num2} = ${resultado}`
        })
    }
    else {
        resultado = num1 / num2
        swal.fire({
            position: 'center',
            icon: 'success',
            title: `${num1} / ${num2} = ${resultado}`
        })
    }
}
document.querySelector('.submit-btn').addEventListener('click', Calcular)