a = int(input("Informe a velovidade de do veículo: "))

if a > 110:
    b = a - 110
    b = b * 5
    print ("Veículo multado no valor de", b, "Reais")

else:
    print ("O veículo não foi multado")
