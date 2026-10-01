#Programa donde tienes que adivinar el numero
import random
numero_secreto=random.randint(1,100)
while True:
    numero=int(input("Adivina el numero secreto: "))
    if numero==numero_secreto:
        print("Felicidades, adivinaste el numero secreto")
        break
    else:
        print("Intenta de nuevo")