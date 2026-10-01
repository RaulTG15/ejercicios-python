#programa que suma 5 números ingresados por el usuario
suma=0
for i in range(1,6):
    numero=int(input("Ingrese un número: "))    
    suma+=numero
print("La suma de los números ingresados es:", suma)