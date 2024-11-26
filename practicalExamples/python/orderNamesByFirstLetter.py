names = ["Ana", "Luis", "Carlos", "María", "Pedro", "Laura", "Antonio", "maría"]
sortedNames = {}

for name in names:
    firstLetter = name[0].upper()
    
    if (firstLetter not in sortedNames):
        sortedNames[firstLetter] = []

    sortedNames[firstLetter].append(name)

print(sortedNames)