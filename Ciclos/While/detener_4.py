#Programa que detiene la ejecución del ciclo cuando el usuario ingresa el número 4 tres veces

detener=0
while True:
    numero=int(input("Ingrese un número: "))
    if numero==4:
        detener+=1
    if detener==3:
        break
    