# Instrucciones:
# 1. Pedir el nombre del juego, precio, edad del comprador y cantidad de juegos.
# 2. Calcular el subtotal de la compra.
# 3. Si compra 3 o más juegos, aplicar un descuento del 10%.
# 4. Si el subtotal supera $1,500, aplicar un descuento adicional del 5%.
# 5. Si el total después de descuentos supera $2,000, aplicar un impuesto del 8%.
# 6. Mostrar el subtotal, descuento, impuesto y total a pagar.

impuesto = 0
total = 0
cantidad_juegos = int(input("Ingrese la cantidad de juegos a comprar: "))
for i in range(cantidad_juegos):
    nombre_juego = str(input("Ingrese el nombre del juego: "))
    precio = float(input("Ingrese el precio del juego: "))
    total+=precio
    edad_comprador = int(input("Ingrese la edad del comprador: "))


if cantidad_juegos >= 3:
    descuento= total * 0.10
    total = total-descuento
else:
    descuento = 0

if total > 1500:
    descuento_adicional = total * 0.05
    descuento += descuento_adicional
    total= total - descuento_adicional
else:
    descuento_adicional = 0

if total > 2000:
    impuesto = total * 0.08
    total += impuesto

print(f"Descuento: ${descuento:.2f}")
print(f"Impuesto: ${impuesto:.2f}")
print(f"Total a pagar: ${total:.2f}")