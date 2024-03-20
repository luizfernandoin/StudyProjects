function calcularMelhorCombustivel(priceGas, priceAlcool) {
    let resultado;
    if (priceGas === priceAlcool){
        resultado = 'Preços iguais';
    } else {
        if (priceGas < priceAlcool) {
            resultado = 'Gasolina';
        } else {
            resultado = 'Alcool';
        }
    }

    document.querySelector(".result").classList.add("show")
    document.querySelector(".value").textContent = resultado;
}


document.querySelector(".btn").addEventListener('click', function(){
    const baseInput = document.getElementById('gasolina');
    const expoenteInput = document.getElementById('alcool');
    const base = parseFloat(baseInput.value);
    const expoente = parseInt(expoenteInput.value);

    calcularMelhorCombustivel(base, expoente);
});