def aprobar_reprobar(calificacion):
    if calificacion >= 6:
        return "Aprobado"
    else:
        return "Reprobado"


calificacion = float(input("Introduce la calificación: "))

resultado = aprobar_reprobar(calificacion)

print(f"El alumno está {resultado}")