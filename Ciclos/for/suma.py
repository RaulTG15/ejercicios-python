#Programa que pida un numero al usuario y calcule la suma de todos los numeros desde 1 hasta el numero ingresado mediante ciclos
numero=int(input("Ingrese un numero: "))
suma=0
for i in range(1,numero+1):
    suma+=i
print(f"La suma de los numeros del 1 al {numero} es: {suma}")