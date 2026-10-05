#Muestra en pantalla un menu 1.sumar 2. restar 3. multiplicar 4. salir
opcion = 0

while opcion != 4:
    print("Menu")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Salir")
    opcion = int(input("Ingrese una opcion: "))

    if opcion == 1:
        num1 = int(input("Ingrese el primer numero: "))
        num2 = int(input("Ingrese el segundo numero: "))
        resultado = num1 + num2
        print("El resultado de la suma es: ", resultado)
    elif opcion == 2:
        num1 = int(input("Ingrese el primer numero: "))
        num2 = int(input("Ingrese el segundo numero: "))
        resultado = num1 - num2
        print("El resultado de la resta es: ", resultado)
    elif opcion == 3:
        num1 = int(input("Ingrese el primer numero: "))
        num2 = int(input("Ingrese el segundo numero: "))
        resultado = num1 * num2
        print("El resultado de la multiplicacion es: ", resultado)
    elif opcion == 4:
        print("Saliendo del programa...")
    else:
        print("Opcion invalida, por favor ingrese una opcion valida.")