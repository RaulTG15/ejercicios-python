#Programa que de las tablas de multiplicar del 1 al 10 con while
i = 1
numero = int(input("Ingrese el número de la tabla que desea: "))
while i <=10:
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
    i+=1