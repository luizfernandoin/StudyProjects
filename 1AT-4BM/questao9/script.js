
const TamanhoPalavra = () => {
	event.preventDefault();
    const palavra = document.getElementById('palavra').value
    
    let lenpalavra = palavra.length

    swal.fire({
        position: 'center',
        icon: 'success',
        title: `Tamanho: ${lenpalavra}`
    })
}
document.querySelector('.submit-btn').addEventListener('click', TamanhoPalavra)