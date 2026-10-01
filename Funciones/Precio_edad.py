#Funcion que calcule el precio segun la edad del cliente
def calcular_precio_edad(edad):
    if edad<12:
        precio=50
    else:
        precio=100
    return precio

edad=int(input("Ingrese la edad del cliente: "))
precio=calcular_precio_edad(edad)
print(f"El precio segun la edad del cliente es: ${precio}")    