function calculateFactorial(number) {
    let currentResult = 1;

    if (number === 0 || number === 1) {
        return currentResult;
    }

    for (var i = number; i > 1; i--) {
        currentResult *= i; 
    }

    return currentResult;
};

let inputNumber = 5;

if (inputNumber < 0 || !Number.isInteger(inputNumber)) {
    console.log("El numero ingresado no debe ser negativo o decimal")
} else {
    let calculationResult = calculateFactorial(inputNumber);

    console.log("Resultado del calculo factorial");
    console.log(`${inputNumber}! = ${calculationResult}`);
}
