alumnos=int(input("Ingrese la cantidad de alumnos: "))
for i in range(alumnos):
    nombre=input("Ingrese el nombre del alumno: ")
    nota1=float(input("Ingrese la primera nota: "))
    nota2=float(input("Ingrese la segunda nota: "))
    nota3=float(input("Ingrese la tercera nota: "))
    promedio=(nota1+nota2+nota3)/3
    if promedio>=6:
        print(f"{nombre} ha aprobado con un promedio de {promedio: .2f}")
    else:
        print(f"{nombre} ha reprobado con un promedio de {promedio: .2f}")