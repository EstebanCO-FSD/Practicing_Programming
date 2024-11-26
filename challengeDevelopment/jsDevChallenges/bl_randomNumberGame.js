function getRandomNumber(max, min) {
    return Math.floor(Math.random() * (max - min + 1) + min);
}

let inputNumber = 4;
let randomNumber = getRandomNumber(1, 100);
let message = "";
let text = "";
    text += inputNumber > randomNumber ? "mayor" : "";
    text += inputNumber < randomNumber ? "menor" : "";

if (inputNumber === randomNumber) {
    message = "El numero ingresado es igual al numero generado (¡Ganaste!)";
} else {
    message = `El numero ingresado es ${text} al numero generado`;
}

console.log("Numero genarado: " + randomNumber);
console.log(message);