def mayor(a, b):
    if a > b:
        return a
    else:
        return b


num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))

resultado = mayor(num1, num2)

print(f"El número mayor es: {resultado}")