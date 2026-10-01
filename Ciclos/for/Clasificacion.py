#Programa que solicite 10 numeros al usuario y los clasifique en positivo o negativo mediante ciclos
positivos=0
negativos=0
ceros=0
for i in range(10):
    numero=int(input("Ingrese un numero: "))
    if numero>0:
        positivos+=1
    elif numero<0:
        negativos+=1
    else:
        ceros+=1
print(f"Cantidad de numeros positivos: {positivos}")
print(f"Cantidad de numeros negativos: {negativos}")
print(f"Cantidad de ceros: {ceros}")