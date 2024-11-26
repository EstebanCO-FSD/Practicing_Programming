const inputNumber = 3;

let message = `El número validado es ${inputNumber % 2 === 0 ? "par" : "impar"}`;

if (inputNumber % 3 === 0) {
    message += " y es divisible por 3";
}

console.log(message);

