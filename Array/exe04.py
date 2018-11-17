cont = 0
vetNota = []
nota = 0
total = 0
media = 0
while cont < 4:
    nota = input("Informe a mota do aluno: ")
    vetNota.append(nota)
    total += int(vetNota[cont])
    cont += 1

print("notas obtidas ",vetNota)
media = total / cont
print("Media final do aluno: ",media)
