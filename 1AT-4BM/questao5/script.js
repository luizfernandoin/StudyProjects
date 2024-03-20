const CalcularÁreaTriangulo = () => {
	event.preventDefault();
    const base = Number(document.getElementById('base').value)
    const altura = Number(document.getElementById('altura').value)

    let area = (base * altura) / 2

    swal.fire({
        position: 'center',
        icon: 'success',
        title: `Área: ${area}`
    })
}
document.querySelector('.submit-btn').addEventListener('click', CalcularÁreaTriangulo)