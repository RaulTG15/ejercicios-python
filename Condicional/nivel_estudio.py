edad = int(input("Introduce tu edad: "))

if edad < 3:
    print("No estudia")
elif edad <= 5:
    print("Preescolar")
elif edad <= 11:
    print("Primaria")
elif edad <= 14:
    print("Secundaria")
elif edad <= 17:
    print("Preparatoria")
elif edad <= 22:
    print("Universidad")
else:
    print("Posgrado")