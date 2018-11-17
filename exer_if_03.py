minutos = int(input("Informe a quantidade em minutos utilizado: "))
if minutos < 200:
    preco = 0.20
else:
    if minutos <= 400:
       preco = 0.18
if minutos > 400 and minutos < 800:
   preco = 0.18
else:
     if minutos > 800:
        preco = 0.08
print("Conta telefônica: ", minutos * preco, "Reais")
