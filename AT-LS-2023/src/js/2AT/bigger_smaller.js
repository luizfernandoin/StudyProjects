document.querySelector(".btn").addEventListener("click", function () {
    const numbersInput = document.getElementById("numbersInput").value;
    const separatorInput = document.getElementById("separatorInput").value;
    const numbersArray = numbersInput.split(separatorInput)
        .filter((num) => num.trim() !== '')
        .map((num) => Number(num));

    if (numbersArray.length === 0 || numbersArray.some(isNaN)) {
        document.getElementById("maxNumber").textContent = "Inválido";
        document.getElementById("minNumber").textContent = "Inválido";
    } else {

        const max = Math.max(...numbersArray);
        const min = Math.min(...numbersArray);
        document.getElementById("maxNumber").textContent = max;
        document.getElementById("minNumber").textContent = min;
    }

    document.querySelector(".result").classList.add("show")
});