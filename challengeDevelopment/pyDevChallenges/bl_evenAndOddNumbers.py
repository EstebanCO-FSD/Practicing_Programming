while True:
    print("\n// Números pares e impares //\n")

    inputNumber = int(input("Digite el numero a validar: "))
    message = f"El número validado es {'par' if inputNumber % 2 == 0 else 'impar'}"

    if inputNumber % 3 == 0:
        message += " y es divisible por 3"

    print(message)

    exitProgram = input("\nPresione 'q' para salir del programa o cualquier otra tecla para continuar: ").strip().lower()

    if exitProgram.lower() == 'q':
        print("¡Programa terminado!")
        break