while True:
    def getFibonacciSeries(number):
        fibinacciSeries = []

        for i in range(0, number):
            if i <= 1:
                fibinacciSeries.append(i)
            else:
                fibinacciSeries.append(fibinacciSeries[i - 1] + fibinacciSeries[i - 2])

        return fibinacciSeries
    
    print("\n// Fibonacci //\n")

    inputNumber = int(input("Ingresa los (n) numeros de la serie que deseas conocer: "))
    resultingSerie = getFibonacciSeries(inputNumber)

    print(f"\nLos primeros {inputNumber} de la serie Fibonacci son:")
    print(", ".join(map(str, resultingSerie)))

    exitProgram = input("\nSi desea salir del programa presione 'q' en caso contrario cualquier otra tecla: ")

    if exitProgram.lower() == 'q':
        print("¡Programa terminado!")
        break