def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    return a / b


num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))

print(f"Suma: {suma(num1, num2)}")
print(f"Resta: {resta(num1, num2)}")
print(f"Multiplicación: {multiplicacion(num1, num2)}")
print(f"División: {division(num1, num2):.2f}")