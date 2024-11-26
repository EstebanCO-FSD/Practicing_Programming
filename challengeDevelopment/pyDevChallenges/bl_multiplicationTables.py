while True:
    print("\n// Tabla de multiplicar //\n")

    inputNumber = int(input("Ingrese el numero de la tabla de multiplicar: "))
    
    print(f"\nTabla de multiplicar del {inputNumber}")

    for i in range(1, 11):
        print(f"{inputNumber} x {i} = {inputNumber * i}")

    exitProgram = input("\nSi desea salir del programa presione 'q' en caso contrario cualquier otra tecla: ")

    if exitProgram.lower() == 'q':
        print("¡Programa terminado!")
        break