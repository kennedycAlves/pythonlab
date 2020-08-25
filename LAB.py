
Marcadores

%d para numeros inteiros
%s para strings
%f para flooat

Ex:
>>> a = 42
>>> print ('O numero %d é muito legal' %a)
O numero 42 é muito legal
>>> a = "abacate"
>>> print ('O numero %s é muito legal' %a)
O numero abacate é muito legal
>>> pi = 3.1415
>>> print ("O valor de pi é: %f " %pi)
O valor de pi é: 3.141500 
>>> print ("O valor de pi é: %.2f " %pi)
O valor de pi é: 3.14 
>>>  

converter um numero para string

>>> a = 42
>>> str(a) + "mamão"
'42mamão'
>>> 

>>> a = str(2 ** 1000000)
>>> len(a)
301030

Fatiamento de strings

>>> x = "0123456789"
>>> print(x[0])
0
>>> print(x[0:2])
01
>>> print(x[1:2])
1
>>> print(x[0:8])
01234567
>>> 



primeiro número antes dos : é referente ao início 
segundo número depois dos : até onde deve ir, no caso do exemplo  print(x[0:2]), podemos ver que é 2, entende-se então que será mostrado o número anterior a ele. 

>>> print(x[:3])
012
>>> print(x[4:])
456789
>>> print(x[4:-1])
45678
>>> print(x[4:-2])
4567
>>> print(x[-4:-1])
678
>>> print(x[:])
0123456789
>>> 

Print moderno
strVar1 = str(input("Informe seu nome: "))
intVar1 = int(input("Informe o primeiro numero: "))
intVar2 = int(input("Informe o segundo número: "))
 
 
print("{0} {1} + {2} é igual a: {3}: ".format(strVar1, intVar1, intVar2, soma(intVar1, intVar2)))
 
print tudo na mesma linha
 
print("strings", end=' ')

Incremento no fatiamento 

>>> texto = "Batatinha quando nasce"
>>> texto[::2]
'Bttnaqad ac'
 
- Salta de dois em imprimindo as strings

>>> texto[::-1]
'ecsan odnauq ahnitataB'
>>> 

- Vai de trás para frente nas stringscon

Find e replace de string

>>> s = "um tigre, dois tigre, três tigre"
>>> s.find('tigre')
3
>>> s.find('tigre', 4)
15
>>> s.find('tigre', 15)
15
>>> s.find('tigre', 16)
27
>>> 

caso retorne -1 é porque a string a ser buscada não foi encontrada.

Replace

Faz a substituição de strings.

Ex:

>>> s.replace('tigre', 'gato')
'um gato, dois gato, três gato'
>>> s
'um tigre, dois tigre, três tigre'


para que seja de forma efetiva, é necessário realizar a atribuição na variável.

>>> s = s.replace('tigre', 'gato')
>>> s
'um gato, dois gato, três gato'



Atribuição múltipla

>>> a = 10
>>> b = 50
>>> a, b = b, a
>>> a
50
>>> b
10

>>> a, b, c = 'OBA'
>>> a
'O'
>>> b
'B'
>>> c
'A'

Listas(array)

lista = ["dado1", "dado2", "dado3"]

len(lista)

conta quantos dados existem dentro da lista

>>> len(lista)
3

append

Usado para adicionar um dado ao final da lista, utilizado quando se deseja adicionar um dado a lista.

Ex:
>>> lista.append("dado4")
>>> lista
['dado1', 'dado2', 'dado3', 'dado4']
>>> 

Só adiciona um argumento por append, para que seja possível adicionar vários argumento, mas dessa forma, esses elementos adicionais se tornam uma lista aparte.
>>> lista.append([1, 2, 3])
>>> lista
>> lista
['K', 'e', 'n', 'n', 'e', 'd', 'y', [1, 2, 3]]



extend

Adiciona uma coleção de novos dados ao final da lista, fazendo com que eles se tornem parte dessa lista. Utilizado par adicionar mais de um dado a lista, não aceitando somente a um dado a ser adicionado.

Ex:
>>> lista.extend(["dado5", "dados6"])
>>> lista
['dado1', 'dado2', 'dado3', 'dado5', 'dados6']
>>> 


Podendo também receber dados de outra lista

Ex:
>>> lista2 = ["dados7", "dados8", "dados9"]
>>> lista.extend(lista2)
>>> lista
['dado1', 'dado2', 'dado3', 'dado5', 'dados6', 'dados7', 'dados8', 'dados9']
>>> 

>>> lista.extend([10, 20,30])
>>> lista
['K', 'e', 'n', 'n', 'e', 'd', 'y', [1, 2, 3], 10, 20, 30] 


>>> lista.extend('Costa Alves')
>>> lista
['K', 'e', 'n', 'n', 'e', 'd', 'y', [1, 2, 3], 10, 20, 30, 'C', 'o', 's', 't', 'a', ' ', 'A', 'l', 'v', 'e', 's']


insert

Insere um dado em uma posição informada, não substituindo o dados que está atualmente nessa posição, fazendo com esse dado seja deslocado para direita.

Ex:

lista
['K', 'e', 'n', 'n', 'e', 'd', 'y', [1, 2, 3], 10, 20, 30, 'C', 'o', 's', 't', 'a', ' ', 'A', 'l', 'v', 'e', 's']
>>> lista.insert(7, 'inset')
>>> lista
['K', 'e', 'n', 'n', 'e', 'd', 'y', 'inset', [1, 2, 3], 10, 20, 30, 'C', 'o', 's', 't', 'a', ' ', 'A', 'l', 'v', 'e', 's']

reverse

Inverter um alista

Ex:
>>> lista.reverse()
>>> lista
['s', 'e', 'v', 'l', 'A', ' ', 'a', 't', 's', 'o', 'C', 30, 20, 10, [1, 2, 3], 'inset', 'y', 'd', 'e', 'n', 'n', 'e', 'K']



pop
 
Usado para remover dados ao final da lista ou pode remover um elemento informado a posição do seu Índice 
 
Ex:
 
>>> lista.pop()
'dado4'
>>> lista
['dado1', 'dado2', 'dado3']
>>>

Removendo um dado de um determinado campo
lista.pop(2)

clear

limpa todos os campos de uma lista.

Ex:

>>> lista
['K', 'e', 'n', 'n', 'e', 'd', 'y', 'inset', [1, 2, 3], 10, 20, 30, 'C', 'o', 's', 't', 'a', ' ', 'A', 'l', 'v', 'e', 's']
>>> lista.clear()
>>> lista
[]

remove

Remove dados de uma lista, 

Ex:

>>> lista.remove("dado1")
>>> lista
['dado2', 'dado3', 'dado5', 'dados6', 'dados7', 'dados8', 'dados9']
>>> 


insert

Insere dados apontando a posição desejada.

Ex:
>>> lista.insert(0, "dado1")
>>> lista
['dado1', 'dado2', 'dado3', 'dado5', 'dados6', 'dados7', 'dados8', 'dados9']
>>> 

count

Conta a ocorrência de strings em uma lista

Ex:
>>> lista = list('Kennedy')
>>> lista
['K', 'e', 'n', 'n', 'e', 'd', 'y']
>>> lista.count('n')
2

Print na posição e o dado de uma lista

print('Produtos dentro de seu carrinho:')
print('ID / Produto')
for indice, listaprods in enumerate(carrinho):
    print(indice, listaprods)

Resultado:

Produtos dentro de seu carrinho:
ID / Produto
0 calça
1 brusa
2 gravata
3 calça
4 sair

index
Encontra o index de um elemento na lista
 Ex: print lista.index(5)

Podemos também imprimir um range de index.

Ex: print(lista.index(5, 1)

Nesse exemplo o index ira buscar um dado "5" depois do index 1


Ex: print(lista.index(5 , 6, 9)

Nesse exemplo o dado número 5 irá ser buscado entre o indexes 6 ao 9

Calculando Itens da lista

lista = [1, 2, 3, 4, 5, 6]

print(sum(lista)) #soma
print(max(lista)) #maior valor da lista
print(min(lista)) #menor valor da lista
print(len(lista)) #qtd de itens da lista

Desempacotamento de lista

lista = [1, 2, 3]
num1, num2, num3 = lista
print(num1)
print(num2)
print(num3)

Caso exista um maior número de elementos do que variáveis para receber os valores, teremos um erro, e vice e versa. 


Deque

Tipo de lista mais robusto, podendo tratar dado no primeiro ou ultimo index


from collections import deque

lista = deque('Kennedy')

print(lista)
deque(['K', 'e', 'n', 'n', 'e', 'd', 'y'])

lista.appendleft('K')

print(lista)
deque(['K', 'K', 'e', 'n', 'n', 'e', 'd', 'y'])


lista.append('Y')

print(lista)
deque(['K', 'K', 'e', 'n', 'n', 'e', 'd', 'y', 'Y'])

lista.pop()

print(lista)
deque(['K', 'K', 'e', 'n', 'n', 'e', 'd', 'y'])

lista.popleft()

print(lista)
deque(['K', 'e', 'n', 'n', 'e', 'd', 'y'])


Tuplas

Tipo de de lista, mas que não pode ser alterada, sua sintaxe utiliza o "()" e, vez de "[]" da lista.

Ex: 
>>> tupla = (1, 2, 3, 4)
>>> tupla[0] = 10
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    tupla[0] = 10
TypeError: 'tuple' object does not support item assignment
>>> lista[0] = 10
>>> lista
[10, 2, 3, 4, 5]
>>> 

Tipos de Tuplas

tupla1 = (1, 2, 3, 4, 5, 6)
print(tupla1)
print(type(tupla1))


tupla1 = (1, 2, 3, 4, 5, 6)
print(tupla1)
print(type(tupla1))

tupla2 = 1, 2, 3, 4, 5, 6
print(tupla2)
print(type(tupla2))

tupla3 = (4)                #Modo errado de inserir um valor unitário a uma tupla, dessa forma se torna um INT
print(tupla3)
print(type(tupla3))

tupla4 = (4,)
print(tupla4)
print(type(tupla4))         #Tupla para receber somente um valor


#Rage de tuplas
tupla5 = tuple(range(0, 10))
print(tupla5)

#Desempacotamento de Tupla
dados = ('Kennedy', 'Costa Alves')
nome, sobrenome = dados
print(nome)
print(sobrenome)

Named Tuples 
são utilizadas para determinar mais de um dado a uma tupla

from collections import namedtuple


#Primeira forma
cachorro1 = namedtuple('cachorro', 'nome, raca, idade')


#segunda formar
cachorro2 = namedtuple('cachorr', ['idade', 'raca', 'nome'])

#Usando

Arya = cachorro1(idade=2, raca='PitBull', nome='Arya')

#Acessando Dados

print(Arya.nome)
print(Arya.idade)
print(Arya.raca)

sansa = cachorro2(idade=1, raca='PitBull', nome='Sansa')

print(sansa.nome)
print(sansa.idade)
print(sansa.raca)

print(sansa.index('PitBull')) #retorna o indice 
print(sansa.count('PitBull')) #verifica a existencia do dado



Conjuntos

um tipo de lista que não permite repetições. utiliza-se as "{}" para se inserir dados aos índices.

Ex:

>>> conjunto = {2, 2, 2, "kennedy", "kennedy"}
>>> conjunto
{2, 'kennedy'}

Transformar uma lista em um conjunto.

>>> lista2 = [2, 2, 2, 10, 10, 10, "oi", "oi", "oi",]
>>> lista2
[2, 2, 2, 10, 10, 10, 'oi', 'oi', 'oi']

>>> set(lista2)
{'oi', 2, 10}


Adicionar um novo índice ao conjunto.

>>> conjunto.add("max")
>>> conjunto
{2, 'kennedy', 'max'}

caso um índice já exista e venha ocorrer uma nova adição, ele irá desconsiderar.

#Deep Copy persiste os dados do conjunto principal, pois o python agrega um novo endereço de memória.
conjunto = {1, 2, 3, 4}
print(conjunto)
conjuntoCopy = conjunto.copy()
conjuntoCopy.add(5)
print(conjuntoCopy)

#shallow copy , ambos os conjutos são modificados, por conta do python mapear o mesmo endereço de memória a ambos os conjuntos.
conjunto2 = {1, 2, 3, 4}
novo = conjunto
novo.add(5)
print(novo)
print(conjunto)


Dicionários

pode ser intendido como uma lista que possui um geristro chave que possui um valor específico.

Ex:

>>> dicio = {"kennedy":25, "khezia":21, "keila":50}
>>> dicio
{'kennedy': 25, 'khezia': 21, 'keila': 50}

dicio['kennedy']

>>> dicio['kennedy']
25

>>> dicio.keys()
dict_keys(['kennedy', 'khezia', 'keila'])


>>> dicio.values()
dict_values([25, 21, 50])

#Método Matemático de Conjuntos

#Imagine que temos dois conjuntos: Um contendo estudantes di curso de Python e em contendo estudantes do curso de Java.

#Precisamos gerar um conjuntos com nomes de estudantes únicos.

#Fórmula 1 - Utilizando union
#Utilizar para remover duplicidades

estudantes_python = {'Kennedy', 'Khezia', 'Doriel', 'Keila', 'Alice', 'Bianca',}
estudantes_java =   {'Kennedy', 'João', 'Doriel', 'Matheu'}

unicos1 = estudantes_java.union(estudantes_python)
print(unicos1)

#segunda forma
unicos2 = estudantes_java | estudantes_python
print(unicos2)

#utilizado para mostrar o mesmo dado pertencente aos dois conjuntos
ambos1 = estudantes_python.intersection(estudantes_java)
print(ambos1)

#segunda forma
ambos2 = estudantes_java & estudantes_python
print(ambos2)

#gerar um conjunto de estudantes que não estão no outro cuso
so_python = estudantes_python.difference(estudantes_java)
print(so_python)

so_java = estudantes_java.difference(estudantes_python)
print((so_java))




Verificar se uma chave existe:

>>> dicio.values()
dict_values([25, 21, 50])

>>> 'doriel' in dicio
False

Deletando um índice

>>> del dicio["kennedy"]
>>> dicio.values
<built-in method values of dict object at 0x014FAA20>
>>> dicio.values()
dict_values([21, 50])
>>> dicio.keys()
dict_keys(['khezia', 'keila'])
>>> 

usando get

com a utilização do get no dicionário, caso a chave não exista ele não erá dar erro, mas sim deixara o campo como None, ou também poderá inserir um dado de aviso, por exemplo:

aises = {'br': 'Brasil', 'py': 'Paraguai', 'eua': 'Estados Unidos'}

entrada = input(str('Informe o pais: '))
pais = paises.get(entrada, 'Não encontrado')
print(f'Pais {pais} encontrado')

Tuplas com Dicionários

localidades = {
    (72.34343, 71.24233): 'Vicente Pires',
    (27.4482, 22.3009): 'Aguas lindas',
}

print(localidades)
{(72.34343, 71.24233): 'Vicente Pires', (27.4482, 22.3009): 'Aguas lindas'}


#Adicionar elementos em um dicionário

receita = {'Jan': 100, 'Mar': 500, 'Abr': 1000}
print(receita)
print(type(receita))

Atualizando o valor de uma chave existente
receita['Jan'] = 200
print(receita)

Passando um valor de um dicionário para outro
novo_dado = {'Mai': 800}
receita.update(novo_dado)
print(receita)

OU

receita.update({'Mai':1000})

Podemos entender que atualizar ou adicionar novos dados um dicionário é a mesma forma.
Não podemos ter chaves repetidas também.

#Removendo dados
#Primeira forma
receita.pop('Mar')
print(receita)

#Segunda forma
del receita['Mai']
print(receita)


Utilizando o for para trabalhar com dicionários.

receita = {'jan':100, 'fev':200, 'mar':400}

#Imprimindo somente as chaves
for chave in receita:
    print(chave)

#Modo paythonico
for chave in receita.keys():
    print(chave)

#Imprimindo o valor das chaves
for chave in receita:
    print(receita[chave])


#Modo pythonico
for chave in receita.values():
    print(chave)



#Imprimindo as chaves e seus respectivos valores
for chave in receita:
    print(f'{chave}:{receita[chave]}')

for chave, valor in receita.items():
    print(f'Chave:{chave} Valor:{valor}')


#calculando valores do dicionário
print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita))


fromkeys

Utilizado quando se deseja transformar um dado padrão em todas as keys ou values do dicionário.

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

dicionario = {}.fromkeys(lista, 'dict')
print(dicionario)
dicionario2 = {}.fromkeys('key', lista)
print(dicionario2)

Resultado:

{1: 'dict', 2: 'dict', 3: 'dict', 4: 'dict', 5: 'dict', 6: 'dict', 7: 'dict', 8: 'dict', 9: 'dict'}
{'k': [1, 2, 3, 4, 5, 6, 7, 8, 9], 'e': [1, 2, 3, 4, 5, 6, 7, 8, 9], 'y': [1, 2, 3, 4, 5, 6, 7, 8, 9]}

Defaultdict
Utilizado para quando ocorrer o acesso a indexe que não existe no dict, ele não retornar um keyerror, mas cria uma nove chave contendo um valor padrão

#Ex:

from collections import defaultdict

dicionario = defaultdict(lambda: 0) #setando o valor padrão, para quando um valor não existente no dict for acionado.

dicionario['Cruso'] = 'Programação em Python'

print(dicionario)

print(dicionario['outro']) #Teríamos um erro caso esse fosse um dicionário comum.

print(dicionario) #Uma nova chave foi criada

Resultado:
defaultdict(<function <lambda> at 0x7f6816ca5268>, {'Cruso': 'Programação em Python'})
0
defaultdict(<function <lambda> at 0x7f6816ca5268>, {'Cruso': 'Programação em Python', 'outro': 0})


Strings

Strings são imutáveis, ou seja, não podem ser modificadas. Pra que se possa mudar uma string de uma variável, é necessário transforma-la em uma lista, como o Ex abaixo:

>>> nome = 'kennedy'
>>> nome[0]
'k'

Tranformando uma texto em campos de uma lista
>>> lista = list(nome)
>>> lista
['k', 'e', 'n', 'n', 'e', 'd', 'y']
>>> lista[0] = 'v'
>>> lista
['v', 'e', 'n', 'n', 'e', 'd', 'y']
>>> nome
'kennedy'

Join
pode tornar uma lista em strings normal de uma variável ou juntar  strings com ou sem um caracter.
podemos inserir espaços entre a junção das intrigs vindas de uma lista usando ' ', ou '' para juntar todas sem espaços.

>>> nome = ' '.join(lista)
>>> nome
'vennedy'
>>> 
>>> len(nome)
7

>>> data2
['28', '02', '2019']
>>> '/'.join(data2)
'28/02/2019'

>>> var = 'Kennedy Costa Alves'
>>> lista = var.split()
>>> lista
['Kennedy', 'Costa', 'Alves']
>>> var = '@'.join(lista)
>>> lista
['Kennedy', 'Costa', 'Alves']
>>> var
'Kennedy@Costa@Alves'


lista = str(list(range(1, 100)))
>>> lista
'[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]'
>>> junta = '@'.join(lista[0::5])
>>> junta
'[@,@4@ @,@9@,@ @1@4@,@ @1@9@,@ @2@4@,@ @2@9@,@ @3@4@,@ @3@9@,@ @4@4@,@ @4@9@,@ @5@4@,@ @5@9@,@ @6@4@,@ @6@9@,@ @7@4@,@ @7@9@,@ @8@4@,@ @8@9@,@ @9@4@,@ @9@9'



Para persistir a mudança

>>> data = '/'.join(data2)
>>> data
'28/02/2019'


split
divide strings com base em um delimitador, por padrão utiliza o espaço como delimitador.

>>> data = '28/02/2019'
>>> data.split('/')
['28', '02', '2019']
>>> 

Verificar primeiro ou ultimo caracter de uma string

>>> texto = 'prog.py'
>>> texto.startswith('p')
True
>>> texto.endswith('y')
True
>>> texto.startswith('r')
False
>>> texto.endswith('p')
False
>>> 

Tornando string maiúsculas ou minusculas

>>> texto = "Sim"
>>> texto.lower()
'sim'
>>> texto.upper()
'SIM'

Counter

O Counter é um módulo que deve ser importado de collections. Ele é utilizado para contar quantas vezes ouve ocorrência de uma determinada string.
Ex:

from collections import Counter

texto = """A final do Campeonato Europeu de Futebol de 2004 foi uma partida de futebol 
realizada em 4 de julho de 2004 no Estádio da Luz em Lisboa, Portugal. Ela foi disputada 
entre a anfitriã Portugal e a Grécia para decidirem o vencedor do Campeonato Europeu de 
Futebol de 2004, com os gregos saindo-se vitoriosos (imagem, o gol da vitória). Esta foi 
a primeira aparição na final para ambas as seleções. Portugal havia anteriormente participado 
das edições de 1984, 1996 e 2000 do torneio, com seu melhor resultado tendo sido alcançar as s
emifinais em 1984 e 2000. Já a Grécia só tinha participado em 1980, tendo sido eliminada na primeira fase.
Portugal classificara-se automaticamente para a competição como anfitrião, enquanto a Grécia 
garantira sua participação ao ficar em primeiro de seu grupo nas eliminatórias. Os dois países f
oram sorteados para o mesmo grupo na competição, o Grupo A, enfrentando-se na partida de abertura, 
na qual a Grécia venceu por 2–1. Os portugueses se recuperaram da derrota, venceram seus dois jogos 
seguintes e terminaram a fase de grupos em primeiro lugar, com os gregos ficando em segundo após um 
empate e uma derrota, passando de fase nos critérios de desempate. Portugal enfrentou e derrotou a 
Inglaterra e os Países Baixos na fase eliminatória para chegar a final, já a Grécia passou pela França e 
República Tcheca. """


textoSplit = texto.split()

textoCounter = Counter(textoSplit)
print(textoCounter)

Resultado:
Counter({'de': 13, 'a': 11, 'e': 8, 'em': 7, 'na': 6, 'Grécia': 5, 'para': 5, 'Portugal': 4, 'o': 4, 'do': 3, 'foi': 3, 'da': 3, 'com': 3, 'os': 3, 'fase': 3, 'final': 2, 'Campeonato': 2, 'Europeu': 2, 'Futebol': 2, '2004': 2, 'uma': 2, 'partida': 2, 'gregos': 2, 'primeira': 2, 'as': 2, 'participado': 2, 'seu': 2, 'tendo': 2, 'sido': 2, 'primeiro': 2, 'grupo': 2, 'Os': 2, 'dois': 2, 'derrota,': 2, 'A': 1, 'futebol': 1, 'realizada': 1, '4': 1, 'julho': 1, 'no': 1, 'Estádio': 1, 'Luz': 1, 'Lisboa,': 1, 'Portugal.': 1, 'Ela': 1, 'disputada': 1, 'entre': 1, 'anfitriã': 1, 'decidirem': 1, 'vencedor': 1, '2004,': 1, 'saindo-se': 1, 'vitoriosos': 1, '(imagem,': 1, 'gol': 1, 'vitória).': 1, 'Esta': 1, 'aparição': 1, 'ambas': 1, 'seleções.': 1, 'havia': 1, 'anteriormente': 1, 'das': 1, 'edições': 1, '1984,': 1, '1996': 1, '2000': 1, 'torneio,': 1, 'melhor': 1, 'resultado': 1, 'alcançar': 1, 's': 1, 'emifinais': 1, '1984': 1, '2000.': 1, 'Já': 1, 'só': 1, 'tinha': 1, '1980,': 1, 'eliminada': 1, 'fase.': 1, 'classificara-se': 1, 'automaticamente': 1, 'competição': 1, 'como': 1, 'anfitrião,': 1, 'enquanto': 1, 'garantira': 1, 'sua': 1, 'participação': 1, 'ao': 1, 'ficar': 1, 'nas': 1, 'eliminatórias.': 1, 'países': 1, 'f': 1, 'oram': 1, 'sorteados': 1, 'mesmo': 1, 'competição,': 1, 'Grupo': 1, 'A,': 1, 'enfrentando-se': 1, 'abertura,': 1, 'qual': 1, 'venceu': 1, 'por': 1, '2–1.': 1, 'portugueses': 1, 'se': 1, 'recuperaram': 1, 'venceram': 1, 'seus': 1, 'jogos': 1, 'seguintes': 1, 'terminaram': 1, 'grupos': 1, 'lugar,': 1, 'ficando': 1, 'segundo': 1, 'após': 1, 'um': 1, 'empate': 1, 'passando': 1, 'nos': 1, 'critérios': 1, 'desempate.': 1, 'enfrentou': 1, 'derrotou': 1, 'Inglaterra': 1, 'Países': 1, 'Baixos': 1, 'eliminatória': 1, 'chegar': 1, 'final,': 1, 'já': 1, 'passou': 1, 'pela': 1, 'França': 1, 'República': 1, 'Tcheca.': 1})

class 'collections.Counter'>

A função .most_common mostra as strings que mais tiveram ocorrência no Count

Ex: Lista as 10 string mais recorrentes.

print(textoCounter.most_common(10))
[('de', 13), ('a', 11), ('e', 8), ('em', 7), ('na', 6), ('Grécia', 5), ('para', 5), ('Portugal', 4), ('o', 4), ('do', 3)]
<class 'list'>


if

idade = 15
if idade >= 18:
    print("maior de idade")
else:
    print("menor de idade")

---------------------------------------------------------------------------------
a = int(input("Informe a velovidade de do veículo: "))

if a > 110:
    b = a - 110
    b = b * 5
    print ("Veículo multado no valor de", b, "Reais")

else:
    print ("O veículo não foi multado")


For

for i in range(10):
    print("Imprime")

Imprime
Imprime
Imprime
Imprime
Imprime
Imprime
Imprime
Imprime
Imprime
Imprime


podemos passar mais parâmetros para o range, sendo "0" ponto de início, ponto final "10" e o passo. Ex:

for i in range(0, 10, 2):
    print("Imprime")

Imprime
Imprime
Imprime
Imprime
Imprime


Controlando o loot até qye ele atinja um valor

numeric = 15
for cont in range(numeric,5,-1):
    print(cont)
    
print("Your count is finished!")


while

cont = 1
while cont <= 10:
    print("imprime")
    cont = cont + 1


Funções

def media(num, num2):
    media = (num + num2) / 2
    return media

print(media(50, 50))

= RESTART: C:/Users/oi402899/Desktop/phytonLabs/pythonlab-master/function.py =
50.0


def fatorial(fat):
    x = 1
    y = 1
    while x <= fat:
        y = y * x
        x = x + 1
    print("fatorial de %d é: %d " %(fat, y))

>>> fatorial(10)
fatorial de 10 é: 3628800 


Arquivos

função que abre os arquivos open
com os modos:

r - leitura
w - escrita( Cria o arquivo se ele não existir, caso exista ele será apagado e reescrito)
a - append
b - binário
+ (atualização)

Os métodos para ler ou escrever são:

read e write

close fecha.

Ex:

Escrevendo em um arquivo

arquivo = open('numeros.txt', 'w')
for linha in range(1, 101):
    arquivo.write('%d\n' %linha)
arquivo.close()

\n
faz pular para linha de baixo

lendo o arquivo

arquivo = open('numeros.txt', 'r')
for linha in arquivo.readlines():
    print(linha)
arquivo.close()

Executado:

1

2

3

4

5

6

7



a opção readlines faz com que cada elemento tome uma tinha, ou seja faz o read de forma linear.

rstrip
Faz com que o quando for lido uma linha ele não pule uma linha a mais deixando uma linha vazia entre uma string e outra


arquivo = open('numeros.txt', 'r')
for linha in arquivo.readlines():
    print(linha.rstrip())
arquivo.close()

Executado:

1
2
3
4
5
6
7
8
9
10

with
Podemos também realizar o read utilizando with, caso não seja passado nenhum parâmetro(r,w) etc. Ele irá realizar a operação em read.
 
Ex:
 
with open('numeros.txt') as file:
    print(file.read())


Modificando dados dentro de um arquivo

texto = open('menssagem.txt')
saida = open('cripto.txt', 'w')
for ler in texto.readlines():
    for letras in ler:
        if letras in 'aeiou':
            saida.write('*')
        else:
            saida.write(letras)
texto.close()
saida.close()

readline

Ex:
red = arquivo.readline()

print(red)

Ler linha por linha

readlines

Tranforma cada linha do texto em um campo de uma uma lista.
Ex:
red  = arquivo.readlines()

print(red)

close

fecha o arquivo,
Ex: arquivo.close()

closed

utilizado para verificar se o arquivo está aberto. Retorna True se arquivo estiver fechado e False se estiver aberto.

Ex: arquivo.closed


Importar funções

nome do arquivo onde contem as funções

import function
#from funtion import * -> Nesse caso ele importa todas as funções contidas no módulo. 

print(function.media(50, 20))



Classes

class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def getNome(self):
        return self.nome

    def setNome(self, nome):
        self.nome = nome

pessoa1 = Pessoa('Kennedy')
print(pessoa1.getNome())
pessoa1.setNome('Khezia')
print(pessoa1.getNome())


Listando vários objetos

class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def getNome(self):
        return self.nome

    def setNome(self, nome):
        self.nome = nome

p1 = Pessoa('Kennedy')
p2 = Pessoa('Khezia')
p3 = Pessoa('Keila')


listaPessoas = [p1, p2, p3]

for i in listaPessoas:
    print(i.getNome())




_____________________________________________________________________________________________________________________

class Pessoa:
    def __init__(self, nome, cpf, rg, end):
        self.nome = nome
        self.cpf = cpf
        self.rg = rg 
        self.end = end
        
    def getNome(self):
        return self.nome

    def setNome(self, nome):
        self.nome = nome


    def getCPF(self):
        return(self.cpf)

    def setCPF(self, cpf):
        self.cpf = cpf


    def getRG(self):
        return(self.rg)

    def setRG(self, rg):
        self.rg = rg

    def getEndereco(self):
        return self.end

    def setEndereco(self, end):
        self.end = end
        

p1 = Pessoa('Kennedy', "045-511-811.61", "2434753", "Quadra 19")
p2 = Pessoa('Khezia', "044-566-611.61", "55588", "Quadra 19")

lista = [p1, p2]

for i in lista:
    print(i.getNome(), i.getCPF(), i.getRG(), i.getEndereco())
    print("-------------------------------------------------------------------")


Exemplos
carrinho = []
produto = ''

while produto != 'sair':
    produto = str(input('Informe o nome do produto: '))
    print('insira sair para concluír!')
    carrinho.append(produto)
    if produto == 'sair':
        break
print('Produtos dentro de seu carrinho:')
print('ID / Produto')
for indice, listaprods in enumerate(carrinho):
    print(indice, listaprods)

modificar = str(input('Deseja alterar algum produto?'))
print("sim ou não")

while modificar == 'sim':
    id = int(input('Informe o ID do produto a ser mudado: '))
    trocaProd = str(input('Informe o novo produto: '))
    carrinho[id] = trocaProd
    print('Produto modificado!')
    modificar = str(print('Deseja modificar outro produto? (sim ou não)'))
    if modificar == 'não':
        break

print('Produtos dentro de seu carrinho:')
print('ID / Produto')
for indice, listaprods in enumerate(carrinho):
    print(indice, listaprods)

concluir = str(input("Concluír compra? (sim/não)"))
if concluir == 'sim':
    print("Compra concluída com sucesso!")




Exemplo.

carrinho = []
produto = ''

while produto != 'sair':
    produto = str(input('Informe o nome do produto: '))
    print('insira sair para concluír!')
    carrinho.append(produto)
    if produto == 'sair':
        carrinho.pop()
        break

def printProd():
    print('Produtos dentro de seu carrinho:')
    print('ID / Produto')
    for indice, listaprods in enumerate(carrinho):
        print(indice, listaprods)

def modProd():
    modificar = str(input('Deseja alterar algum produto?'))
    print("sim ou não")

    while modificar == 'sim':
        id = int(input('Informe o ID do produto a ser mudado: '))
        trocaProd = str(input('Informe o novo produto: '))
        carrinho[id] = trocaProd
        print('Produto modificado!')
        modificar = str(print('Deseja modificar outro produto? (sim ou não)'))
        if modificar == 'não':
            break

print(printProd())

print(modProd())


concluir = str(input("Concluír compra? (sim/não)"))
if concluir == 'sim':
    print("Compra concluída com sucesso!")



Executar o script python no linux

#!/usr/local/bin/python

#!/usr/bin/env python

#! /bin/sh
""":"
exec python $0 ${1+"$@"}
"""

import re
arquivo = open('/home/kennedy/ppe/Files/messages3')

arquivoRed = arquivo.read()

buscaCritico = re.findall(r'crit.', arquivoRed)
buscaErro = re.findall(r'error.', arquivoRed)
buscaEvento = re.findall(r'event.', arquivoRed)
buscaKernel = re.findall(r'kernel.', arquivoRed)
buscaWarning = re.findall(r'warning.', arquivoRed)
buscaEmerg = re.findall(r'emerg.', arquivoRed)
buscaMultpath = re.findall(r'multipathd.', arquivoRed)


cont_crit = len(buscaEvento)
cont_erro = len(buscaErro)
cont_kernel = len(buscaKernel)
cont_evento = len(buscaEvento)
cont_warning = len(buscaWarning)
cont_emerg = len(buscaEmerg)
cont_multh = len(buscaMultpath)


arquivoGreen = open('/home/kennedy/ppe/Files/messages3')

nomeHost = []
for ler in arquivoGreen.readlines():
    nomeHost.append(ler[15:24])
contHostname = len(nomeHost)

if nomeHost[0] == nomeHost[contHostname -1]:
    print(nomeHost[0].upper())
    print('-----------------------------------------')
else:
    print('Nao foi possivel identificar o hostname.')
    print('-----------------------------------------')

arquivoGreen.close()

arquivoBlue = open('/home/kennedy/ppe/Files/messages3')

selectTimeKernel = []
if buscaKernel:
    selectTimeKernel.insert(0, '')
    for ler in arquivoBlue.readlines():
        if buscaKernel[0] in ler:
            selectTimeKernel.append(ler[0:15])
    print('%d Log(s) de Kernel' %cont_kernel)
    print('Primeiro log registrado: %s ' %selectTimeKernel[1])
    print('Ultimo log registrado: %s' %selectTimeKernel[len(selectTimeKernel) -1])
    print('-----------------------------------------')
else:
    print('Sem registros de Logs de Kernel.')
    print('-----------------------------------------')

selectTimeKernel.clear()
arquivoBlue.seek(0)


selectTimeErro = []
#recorrenteErro = []

if buscaErro:
    selectTimeErro.insert(0, '')
    for ler in arquivoBlue.readlines():
        if buscaErro[0] in ler:
            selectTimeErro.append(ler[0:15])
            #recorrenteErro.append(ler[40::])
            #teste = str(recorrenteErro)
            #teste2 = teste.split()
            #teste4 = list(teste3)
            #teste5 = teste4.count(r'received.')
    #print(teste5)
    print('%d Log(s) de Erros.' %cont_erro)
    print('Primeiro log registrado: %s ' %selectTimeErro[1])
    print('Ultimo log registrado: %s' %selectTimeErro[len(selectTimeErro) -1])
    print('-----------------------------------------')
else:
    print('Sem registros de Erros Criticos.')
    print('-----------------------------------------')

selectTimeErro.clear()
arquivoBlue.seek(0)

selectTimeCritico = []
if buscaCritico:
    selectTimeCritico.insert(0, '')
    for ler in arquivoBlue.readlines():
        if buscaCritico[0] in ler:
            selectTimeCritico.append(ler[0:15])
    print('%d Log(s) Cŕiticos:' %cont_crit)
    print('Primeiro log registrado: %s ' %selectTimeCritico[1])
    print('Ultimo log registrado: %s' %selectTimeCritico[len(selectTimeCritico) -1])
    print('-----------------------------------------')
else:
    print('Sem registros de erros Criticos.')
    print('-----------------------------------------')

selectTimeCritico.clear()
arquivoBlue.seek(0)

selectTimeEvento = []
if buscaEvento:
    selectTimeEvento.insert(0, '')
    for ler in arquivoBlue.readlines():
        if buscaEvento[0] in ler:
            selectTimeEvento.append(ler[0:15])
    print('%d Log(s) de Eventos.' %cont_evento)
    print('Primeiro log registrado: %s ' %selectTimeEvento[1])
    print('Ultimo log registrado: %s' %selectTimeEvento[len(selectTimeEvento) -1])
    print('-----------------------------------------')
else:
    print('Sem registros de Eventos.')
    print('-----------------------------------------')

selectTimeEvento.clear()
arquivoBlue.seek(0)

selectTimeWarning = []

if buscaWarning:
    selectTimeWarning.insert(0, '')
    for ler in arquivoBlue.readlines():
        if buscaWarning[0] in ler:
            selectTimeWarning.append(ler[0:15])
    print('%d Log(s) de Warning.' %cont_warning)
    print('Primeiro log registrado: %s ' %selectTimeWarning[1])
    print('Ultimo log registrado: %s' %selectTimeWarning[len(selectTimeWarning) -1])
    print('-----------------------------------------')
else:
    print('Sem registros de Warning.')
    print('-----------------------------------------')

selectTimeWarning.clear()
arquivoBlue.seek(0)


selectTimeEmerg = []
if buscaEmerg:
    selectTimeEmerg.insert(0, '')
    for ler in arquivoBlue.readlines():
        if buscaEmerg[0] in ler:
            selectTimeEmerg.append(ler[0:15])
    print('%d Log(s) de Emergencia.' %cont_emerg)
    print('Primeiro log registrado: %s ' %selectTimeEmerg[1])
    print('Ultimo log registrado: %s' %selectTimeEmerg[len(selectTimeEmerg) -1])
    print('-----------------------------------------')
else:
    print('Sem registros emergenciais.')
    print('-----------------------------------------')

selectTimeEmerg.clear()
arquivoBlue.seek(0)

selectTimeMulth = []
discosErro = []
if buscaMultpath:
    selectTimeMulth.insert(0, '')
    for ler in arquivoBlue.readlines():
        if buscaMultpath[0] in ler:
            selectTimeMulth.append(ler[0:15])
            discosErro.append(ler[36:])
    transformStr = str(discosErro)
    filtra = re.findall(r'360000\w+', transformStr)
    listaFiltra = list(filtra)
    unic = set(listaFiltra)
    print('%d Log(s) de Multpath com %s Discos afetados.' %(cont_multh, len(unic)))
    print('Primeiro log registrado: %s ' %selectTimeMulth[1])
    print('Ultimo log registrado: %s' %selectTimeMulth[len(selectTimeMulth) -1])
    print('-----------------------------------------')
else:
    print('Sem registros erros de Multpath.')
    print('-----------------------------------------')

selectTimeMulth.clear()

arquivo.close()

arquivoBlue.close()




