var person = {
    name: 'John',
    age: 30,
    gender:'male',
    address: {
        street: '123 Main St',
        city: 'New York',
        state: 'NY',
        zip: '10001'
    }
};

person["code"] = [];

console.log(person.address.zip);
console.log(person["address"]["zip"]);


var listLetterAndNumeric = [["A", "B", "C", "D", "E"],[1, 2, 3, 4, 5]];

console.log(listLetterAndNumeric[0])
console.log(listLetterAndNumeric[1])
console.log(listLetterAndNumeric[0][0] + " : " + listLetterAndNumeric[1][0])
