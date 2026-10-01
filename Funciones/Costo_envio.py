#Funncion que calclula el costo de envio
def calcular_costo_envio(total):
    if total>=1500:
        costo_envio=0
    elif total>=800:
        costo_envio=50
    else:
        costo_envio=100
    return costo_envio

total=float(input("Ingrese el total de la compra: "))
costo_envio=calcular_costo_envio(total)
total_final=total+costo_envio
print(f"El costo de envio es: ${costo_envio:.2f}")
print(f"El total final de la compra es: ${total_final:.2f}")