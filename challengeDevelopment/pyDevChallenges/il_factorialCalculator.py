while True:
    def calculateFactorial(number):
        currentResult = 1

        if (number == 0 or number == 1):
            return currentResult
        
        for i in range(number, 1, -1):
            currentResult *= i

        return currentResult
    
    print("\n// Cálculo de factorial //\n")

    inputNumber = float(input("Ingrese el numero a calcular: "))

    if inputNumber < 0 or not inputNumber.is_integer():
        print("Error: No se puede calcular el factorial de un numero negativo o decimal")
    else:
        inputNumber = int(inputNumber)
        calculationResult = calculateFactorial(inputNumber)

        print(f"\nResultado del calculo factorial\n{inputNumber}! = {calculationResult}")

    exitProgram = input("\nSi desea salir del programa presione 'q' en caso contrario cualquier otra tecla: ")

    if exitProgram.lower() == 'q':
        print("¡Programa terminado!")
        break
    