//km = metros / 1000
//hm = metros / 100
//dam = metros / 10
//cm = metros * 100
//dm = metros * 10
//mm = metros * 1000


const ConverterDistancia = () => {
	event.preventDefault();
    const distancia = Number(document.getElementById('distancia').value)
    
    let km = distancia / 1000
    let hm = distancia / 100
    let dam = distancia / 10
    let cm = distancia * 100
    let dm = distancia * 10
    let mm = distancia * 1000

    if (distancia > 0) {
        swal.fire({
            position: 'center',
            icon: 'success',
            title: `Distancia: ${distancia} m
            Quilômetros: ${km} km
            Hectômetros: ${hm} hm
            Decâmetros: ${dam} dam
            Centimetros: ${cm} cm
            Decímetros: ${dm} dm
            Milímetros: ${mm} mm`
        })
    }
    else if (distancia <= 0) {
        swal.fire({
            position: 'center',
            icon: 'success',
            title: `O valor precisa ser maior que 0!`
        })
    }
}
document.querySelector('.submit-btn').addEventListener('click', ConverterDistancia)