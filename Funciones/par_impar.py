def par_impar(numero):
    if numero % 2 == 0:
        return "Par"
    else:
        return "Impar"


numero = int(input("Introduce un número: "))

resultado = par_impar(numero)

print(f"El número es {resultado}")