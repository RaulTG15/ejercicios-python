
# Programa que calcule cuántos billetes tiene que dar en base a una cantidad

cantidad = int(input("Introduce la cantidad: "))

billetes_500 = cantidad // 500
residuo = cantidad % 500

billetes_200 = residuo // 200
residuo = residuo % 200

billetes_100 = residuo // 100
residuo = residuo % 100

billetes_50 = residuo // 50
residuo = residuo % 50

billetes_20 = residuo // 20
residuo = residuo % 20

print(f"Debes dar {billetes_500} billetes de 500, "
      f"{billetes_200} billetes de 200, "
      f"{billetes_100} billetes de 100, "
      f"{billetes_50} billetes de 50, "
      f"{billetes_20} billetes de 20 "
      f"y sobran {residuo} pesos.")

