var names = ["Ana", "Luis", "Carlos", "María", "Pedro", "Laura", "Antonio", "maría"];
var sortedNames = {};

for (let name of names) {
    var firstLetter = name[0].toUpperCase();

    if (!sortedNames[firstLetter]) {
        sortedNames[firstLetter] = [];
    }

    sortedNames[firstLetter].push(name);
}

console.log(sortedNames);