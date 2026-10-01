#Programa que solicite al usuario 10 numeros y determine cual es el mayor y cual es el menor mediante ciclos
mayor=None
menor=None
for i in range(10):
    numero=int(input("Ingrese un numero: "))
    if mayor is None or numero>mayor:
        mayor=numero
    if menor is None or numero<menor:
        menor=numero
print(f"El numero mayor es: {mayor}")
print(f"El numero menor es: {menor}")