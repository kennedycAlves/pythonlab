contador = int(input("Informe a quatidade de alunos: "))
contador2 = contador
contador = 1
acumulador = 0 
while contador <= contador2:
    soma = int(input("Informe o peso do aluno: "))
    acumulador = acumulador + soma
    contador = contador + 1
print("Soma total de peso dos alunos é igual a: ",acumulador," Kg") 
