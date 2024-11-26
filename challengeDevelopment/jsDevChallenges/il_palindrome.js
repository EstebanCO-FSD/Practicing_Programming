function checkPalindrome(str) {
    str = str.toLowerCase();

    return str === str.split('').reverse().join('');
}

let inputString = "Anna";
let validationResult = checkPalindrome(inputString);

console.log(`La palabra ingresada ${validationResult ? "" : "NO"} es un palindromo`);
console.log(inputString);

