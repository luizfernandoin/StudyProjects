
const CalcularHipotenusa = () => {
	event.preventDefault();
    const c1 = Number(document.getElementById('cateto1').value)
    const c2 = Number(document.getElementById('cateto2').value)

    let hipo = Math.sqrt((Math.pow(c1, 2) + Math.pow(c2, 2)))
    
    swal.fire({
        position: 'center',
        icon: 'success',
        title: `Hipotenusa: ${hipo}`
    })
}
document.querySelector('.submit-btn').addEventListener('click', CalcularHipotenusa)