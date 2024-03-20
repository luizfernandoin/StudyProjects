const celsius = document.getElementById('celsius');
const outputFa = document.getElementById('temp-fahrenheit');
const outputKe = document.getElementById('temp-kelvin');



function converterFahrenheit(tempCelsius) {
    tempFahrenheit = (tempCelsius * 9/5) + 32;

    return tempFahrenheit;
}

function converterKelvin(tempCelsius) {
    tempKelvin = tempCelsius + 273.15;
    return tempKelvin;
}

document.getElementById('celsius').addEventListener('keyup', function(){
    const tempCelsius = parseFloat(celsius.value);

    if (!isNaN(tempCelsius) && celsius.value.trim() !== "") {
        outputFa.textContent = `Fahrenheit: ${converterFahrenheit(tempCelsius)}`;
        outputKe.textContent = `Kelvin: ${converterKelvin(tempCelsius)}`;
    } else {
        outputFa.textContent = "-";
        outputKe.textContent = "Por favor, insira uma temperatura válida em Celsius.";
    }
})