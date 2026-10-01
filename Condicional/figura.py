#programa que pida el numero de lados de una figura y los tamaños de los lados
#si el numero de lado es 3 que calcule el area de un triangulo
#si tiene 4 que calcule el area de un cuadrado 

lado=int(input("Ingresa el número de lados de la figura: "))
tamano_lado=float(input("Ingresa el tamaño del lado: "))
if lado == 3:
    area=(tamano_lado*tamano_lado)/2
    print(F"El área del triángulo es: {area}")
if lado == 4:
    area=tamano_lado*tamano_lado
    print(F"El área del cuadrado es: {area:.2f}")