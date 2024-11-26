import os

def showMenu():
    menu = {
        "\nBasic Level": [
            "1. Números pares e impares",
            "2. Adivina el número",
            "3. Tabla de multiplicar"
        ],
        "\nIntermediate Level": [
            "4. Palíndromos",
            "5. Cálculo de factorial"
        ],
        "\nAdvanced Level": [],
        "\nExit": [
            "Ingrese (x) para salir"
        ]
    }

    print("\n=====================================")
    print("Menú de retos")
    print("=====================================")

    for level, options in menu.items():
        print(level + ":")
        for option in options:
            print(option)

    print("\n=====================================\n")

def main():
    while True:
        showMenu()

        option = input("Ingrese la opción deseada: ")

        if option == "1":
            os.system("python pyDevChallenges/bl_evenAndOddNumbers.py")
        elif option == "2":
            os.system("python pyDevChallenges/bl_randomNumberGame.py")
        elif option == "3":
            os.system("python pyDevChallenges/bl_multiplicationTables.py")
        elif option == "4":
            os.system("python pyDevChallenges/il_palindrome.py")
        elif option == "5":
            os.system("python pyDevChallenges/il_factorialCalculator.py")
        elif option.lower() == "x":
            print("\nPrograma terminado!")
            break
        else:
            print("\nOpción inválida. Intente nuevamente.")



if __name__ == "__main__":
    main()