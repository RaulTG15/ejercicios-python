#El usuario inicia con un saldo de 1000 y puede elegir entre retirar o depositar o salir el progrma debe de hacer las operaciones correspondientes y mostrar el saldo final y el ciclo se termina hasta que el usuario solicite salir
saldo = 1000
opcion = 0
while opcion != 3:
    print("Menu")
    print("1. Retirar")
    print("2. Depositar")
    print("3. Salir")
    opcion = int(input("Ingrese una opcion: "))

    if opcion == 1:
        retiro = int(input("Ingrese la cantidad a retirar: "))
        if retiro > saldo:
            print("No tiene suficiente saldo para realizar el retiro.")
        else:
            saldo -= retiro
            print("Retiro exitoso. Su saldo actual es: ", saldo)

    elif opcion == 2:
        deposito = int(input("Ingrese la cantidad a depositar: "))
        saldo += deposito
        print("Deposito exitoso. Su saldo actual es: ", saldo)
        
    elif opcion == 3:
        print("Saliendo del programa...")
    else:
        print("Opcion invalida, por favor ingrese una opcion valida.")