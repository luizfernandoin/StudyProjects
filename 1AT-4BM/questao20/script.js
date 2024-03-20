
const Calcular = () => {
	event.preventDefault();
    
    mes = parseInt(document.getElementById('mes').value)

    let trimestre = 0

    if (mes > 0 && mes <= 3) {
        trimestre = 1
    }
    else if (mes > 3 && mes <= 6) {
        trimestre = 2
    }
    else if (mes > 6 && mes <= 9) {
        trimestre = 3
    }
    else if (mes > 9 && mes <= 12) {
        trimestre = 4
    }
    
    if (trimestre !== 0) {
        swal.fire({
            position: 'center',
            icon: 'success',
            title: `O mês referido esta no ${trimestre}º Trimestre!`
        })
    }
        
}
document.querySelector('.submit-btn').addEventListener('click', Calcular)