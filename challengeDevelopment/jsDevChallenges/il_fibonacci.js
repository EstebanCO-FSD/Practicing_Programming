function getFibonacciSeries(number) {
    let fibonacciSeries = [];

    for (var i = 0; i < number; i++) {
        if (i <= 1) {
            fibonacciSeries.push(i);
        } else {
            fibonacciSeries.push(fibonacciSeries[i - 1] + fibonacciSeries[i - 2]);
        }
    }

    return fibonacciSeries;
}

let inputNumber = 6;
let resultingSerie = getFibonacciSeries(inputNumber);

console.log(`Los primeros ${inputNumber} numeros de la serie Fibonacci son:`);
console.log(resultingSerie.join(', '));