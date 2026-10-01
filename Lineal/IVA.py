#Programa que calcule el IVA
precio=int(input("Introduce el precio: "))
iva=precio*0.16
precio_final=precio+iva
print(f"El IVA de {precio} es de {iva} el total a pagar es de {precio_final}")