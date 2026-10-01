#Programa que aplique un descuento si la compra es mayor a 1000
precio=int(input("Introduce el precio:"))
if precio>=1000:
    descuento=precio*0.10
    precio=precio-descuento
    print(f"tu descuento es de {descuento} el monto a pagar es de {precio}")