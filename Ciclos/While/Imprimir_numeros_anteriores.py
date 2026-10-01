#Programa que imprime los números anteriores a un número ingresado por el usuario

numero=int(input("Ingrese un número: "))

while numero>0:
    numero-=1
    print(numero)