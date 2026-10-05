#Programa que solicite al usuario numeros y determine cual es el mayor y cual es el menor mediante ciclos
mayor=None
menor=None

numero=int(input("Ingrese los numeros a evaluar: "))
for i in range(numero):
    numero=int(input("Ingrese un numero: "))
    if mayor is None or numero>mayor:
        mayor=numero
    if menor is None or numero<menor:
        menor=numero
print(f"El numero mayor es: {mayor}")
print(f"El numero menor es: {menor}")