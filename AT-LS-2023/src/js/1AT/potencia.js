const calcularPotencia = (base, expoente) => {
    if (!isNaN(base) && !isNaN(expoente)) {
        const resultado = Math.pow(base, expoente);
        document.querySelector(".result").classList.add("show")
        document.querySelector(".value").textContent = resultado;
    } else {
        const resultado = 'Digite valores válidos para base e expoente.';
    }
}
    

document.querySelector(".btn").addEventListener('click', function(){
    const baseInput = document.getElementById('base');
    const expoenteInput = document.getElementById('expoente');
    const base = parseFloat(baseInput.value);
    const expoente = parseInt(expoenteInput.value);

    calcularPotencia(base, expoente);
});