precio=int(input("Ingresa el precio del producto:"))
tipo_producto=str(input("Ingresa el tipo de producto:"))

if tipo_producto =="tecnologico":
    if precio < 15000:
        precio_final=precio-precio*0.08
    else:
        precio_final=precio-precio*0.12
else:
    if precio < 10000:
        precio_final=precio-precio*0.05
    else:
        precio_final=precio-precio*0.10
print(F"El precio final del producto es: {precio_final}")