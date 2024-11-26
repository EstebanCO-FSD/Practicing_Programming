from random import *

while True:
    print("\n// Adivina el número //\n")
    print("¡Adivina el numero del 1 al 100!\n")

    inputNumber = int(input("Ingresa el numero: "))
    randomNumber = randint(1, 100)

    if inputNumber > randomNumber:
        text = "mayor"
    elif inputNumber < randomNumber:
        text = "menor"

    if inputNumber == randomNumber:
        message = "El numero ingresado es igual al numero generado (¡Ganaste!)"
    else:
        message = f"El numero ingresado es {text} al numero generado"

    print("Numero generado: " + str(randomNumber))
    print(message)

    exitGame = input("\nPara finalizar el juego precione 'q' o si no cualquier otra tecla: ")

    if exitGame.lower() == "q":
        print("¡Juego finalizado!")
        break