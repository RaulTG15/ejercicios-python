#Programa que detiene la ejecución del ciclo cuando el usuario ingresa el número 3

while True:
    numero=int(input("Ingrese un número: "))
    if numero==3:
        print("¡Has ingresado el número 3! El programa se detendrá.")
        break