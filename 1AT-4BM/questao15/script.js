
const AnalisarTriangulo = () => {
	event.preventDefault();
    let l = {
        l1: Number(document.getElementById('lado1').value),
        l2: Number(document.getElementById('lado2').value),
        l3: Number(document.getElementById('lado3').value),
    }

    if (l.l1 === l.l2 || l.l1 === l.l3 || l.l2 === l.l3) {
        if (l.l1 === l.l2 && l.l1 === l.l3) {
            swal.fire({
                position: 'center',
                icon: 'success',
                title: `O triangulo cujo os lados são ${l.l1}, ${l.l2} e ${l.l3} é equilatero.`
            })
        }
        else {
            swal.fire({
                position: 'center',
                icon: 'success',
                title: `O triangulo cujo os lados são ${l.l1}, ${l.l2} e ${l.l3} é isósceles.`
            })
        }
    }
    else {
        swal.fire({
            position: 'center',
            icon: 'success',
            title: `O triangulo cujo os lados são ${l.l1}, ${l.l2} e ${l.l3} é escaleno.`
        })
    }
}
document.querySelector('.submit-btn').addEventListener('click', AnalisarTriangulo)