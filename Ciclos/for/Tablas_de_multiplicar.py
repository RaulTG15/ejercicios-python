#Programa que calcule las tablas de multiplicar mediante ciclos
tabla=int(input("Ingrese la tabla de multiplicar que desea calcular: "))
for i in range(1,11):
    resultado=tabla*i
    print(f"{tabla} x {i} = {resultado}")