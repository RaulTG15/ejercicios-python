def positivo_negativo(numero):
    if numero > 0:
        return "Positivo"
    elif numero < 0:
        return "Negativo"
    else:
        return "Cero"


numero = float(input("Introduce un número: "))

resultado = positivo_negativo(numero)

print(f"El número es {resultado}")