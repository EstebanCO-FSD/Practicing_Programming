while True:
    def checkPalindrome(str):
        str = str.lower()

        return str == str[::-1]

    print("\n// Palíndromos //\n")

    inputString = str(input("Ingrese la palabra a validar: "))
    validationresult = checkPalindrome(inputString)
    
    print(f"La palabra ingresada {"NO" if not validationresult else ""} es un palindromo")

    exitProgram = input("\nSi desea salir del programa presione 'q' en caso contrario cualquier otra tecla: ")

    if exitProgram.lower() == 'q':
        print("¡Programa terminado!")
        break
