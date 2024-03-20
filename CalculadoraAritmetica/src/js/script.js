const CalculateAverage = () => {
	event.preventDefault();
	let aluno = {
		nome: document.getElementById("name").value,
		nota1: parseInt(document.getElementById("nota1").value),
		nota2: parseInt(document.getElementById("nota2").value),
		nota3: parseInt(document.getElementById("nota3").value),
		nota4: parseInt(document.getElementById("nota4").value),
	};

    if (aluno.nome != "" && aluno.nota1 != "" && aluno.nota2 != "" && aluno.nota3 != "" && nota4 != "") {
		let media = (aluno.nota1 + aluno.nota2 + aluno.nota3 + aluno.nota4) / 4
        
        console.log(aluno.nome.value)
        if (media >= 70) {
            swal.fire({
                position: 'center',
                icon: 'success',
                title: `Parabéns, ${aluno.nome}, APROVADO(A)!`,
                text: `Média: ${media}`,
            })
        } else if (media < 40) {
            swal.fire({
                icon: 'error',
                title: `Infelizmente, ${aluno.nome}, reprovado(a)!`,
                text: `Média: ${media}`,
            }) 
        } else {
            let final = ((50 - (media * 6)) / 4) * -1
            swal.fire({
                icon: 'warning',
                title: `Ainda há esperanças, ${aluno.nome}, você irá fazer final, precisa de: ${ final }`,
                text: `Média: ${media}`,
            })
        }
    }
}
document.querySelector('.submit-btn').addEventListener('click', CalculateAverage)