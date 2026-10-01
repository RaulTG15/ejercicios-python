#Programa que pida un número y valla sumando hasta que el usario ingrese un 0
suma = 0
while True:
    numero = int(input("Ingrese un número (0 para salir): "))
    if numero == 0:
        break
    suma += numero
print(f"La suma total es: {suma}")