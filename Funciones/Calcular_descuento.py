#Funcion que calcula el descuento de un producto
def calcular_descuento(precio):
    if precio>=1000:
        descuento=precio*0.15
    elif precio>=500 and precio<1000:
        descuento=precio*0.10
    else:
        descuento=0
    return descuento

precio=float(input("Ingrese el precio del producto: "))
descuento=calcular_descuento(precio)
precio_final=precio-descuento
print(f"El descuento aplicado es: ${descuento:.2f}")
print(f"El precio final del producto es: ${precio_final:.2f}")