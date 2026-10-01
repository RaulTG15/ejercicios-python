#Sacar el promedio de 3 calificaciones
Calificacion1=int(input("Introduce la calificacion numero 1: "))
Calificacio2=int(input("Introduce la calificacion numero 2: "))
Calificacion3=int(input("Introduce la calificacion numero 3: "))

promedio=(Calificacion1+Calificacio2+Calificacion3)/3
if promedio>=6:
    print("Aprobado")
else:
    print("Reprobado")