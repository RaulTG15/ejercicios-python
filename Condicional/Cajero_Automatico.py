#Cajero Automatico

saldo=int(input("Ingrese su saldo: "))
retiro=int(input("Ingrese el monto a retirar: "))

if retiro>saldo:
    print("Saldo insuficiente")
elif retiro>8000:
    print("No se puede retirar mas de 8000")
elif retiro%100==0:
    if retiro>=5000:
        print("Se le cobrara una comision de 2% por retirar mas de 5000")
        comision=retiro*0.02
        saldo_final=saldo-retiro-comision
        print(retiro,"retirado con exito")
        print(comision,"de comision cobrada")
        print("Su saldo final es: ",saldo_final)
    else:
        saldo_final=saldo-retiro
        print(retiro,"retirado con exito")
        print("Su saldo final es: ",saldo_final)
else:
    print("El monto a retirar debe ser multiplo de 100")
