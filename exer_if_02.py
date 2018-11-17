minutos = int(input("Informe quantos minutos durou a aligação: "))

if minutos < 200:
    fatura = minutos * 0.20
    print ("O valor da sua fatura é :", fatura, "Reis")

if minutos >= 200 and minutos <= 400:
    fatura = minutos * 0.18
    print("O valor da sua fatura é: ", fatura, "Reais")

if minutos > 400:
    fatura = minutos * 0.15
    print("O valor de sua fatura é: ", fatura)
