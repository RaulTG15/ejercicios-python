#Programa que solicite 10 numeros y sume los pares con pares y impares con impares
pares=0
impares=0

for i in range(10):
    numero=int(input("Ingresa un numero:"))

    if numero %2== 0:
        pares+=numero
    else:
        impares+=numero

print(f"La suma de los numeros pares: {pares}")
print(f"La suma de los numeros impares: {impares}")