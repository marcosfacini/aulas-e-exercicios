
""" numeros = [2, 5, 9, 1]

# mudar elemento
numeros[2] = 3

# adicionar elemento ao final da lista
numeros.append(7)

# ordenar os elementos
numeros.sort()

# ordenanado ao contrário
numeros.sort(reverse = True)

# saber a quantidade de elementos
print (len(numeros))

# inserir elemento no meio da lista - primeiro numero no parenteses é a posição que vai entrar, e o segundo número é o elemnto em si
numeros.insert(2, 0)

# eliminar ultimo elemento
numeros.pop()

# escolher o elemento a ser eliminado colocando sua posição dentro do parenteese
numeros.pop(2) 

print (numeros)
"""

""" lista = [1, 2, 3, 4, 5]
lista.insert(2, 2)
# remove a primeira ocorrencia do elemento na lista
lista.remove(2)
if 6 in lista:
    lista.remove(6)
else:
    print ('Não encontrei o numero 6')
print (lista) """

""" valores = []
valores.append(2)
valores.append(4)
valores.append(6)
valores.append(8)

# para cada elemento (ele) na minha lista (valores):
for ele in valores:
    print (f'{v}...', end=' ')

# enumerate dá a posição e depois o elemento para cada item da lista
for posicao, elemento in enumerate(valores):
    print (f'Na posição {posicao} encontrei o valor {elemento}')
print ('FIM') """

# INPUT PARA LISTA:
""" nomes = []
for nome in range (0, 4):
    nomes.append(str (input ('Digite um nome: ')))
for n in nomes:
    print (f'O nome é: {n}') """

""" # quando se altera uma lista, também se altera a outra, porque elas ficam ligadas
a = [1, 2, 3, 4]
b = a
b[2] = 8
print (a)
print (b)

# para criar uma copia adicionar o [:]
a = [1, 2, 3, 4]
b = a[:]
b[2] = 8
print (a)
print (b) """

""" # listas dentro de listas:
pessoas = ['Pedro', 25]
grupos = []
# dois pontos dentro do colchetes faz uma cópia da lista [:]
grupos.append(pessoas[:])
print (grupos)

# colchetes dentro de colchetes separados por vírgula
grupos = [['Clara', 89] , ['João', 14] , ['José' , 54]]

# primeiro colchetes é refete a lista em questão e o segundo colchetes é o elemento dentro dessa lista
print (grupos[1][0])

# mostra a lista toda dessa posição
print (grupos[0]) """

""" igrediente = ['leite', 'ovos', 'acucar']
receitas = []
receitas.append(igrediente[:])
igrediente[0] = 'pimenta'
receitas.append(igrediente[:])
print (receitas)

receitas.append(['tomate', 'sal'])
print (receitas) """

""" # for
grupos = [['Clara', 89] , ['João', 14] , ['José' , 54]]
for pessoa in grupos:
    print (f'{pessoa[0]} tem {pessoa[1]} anos') """

# inserindo dados direto no append em listas compostas
galera = []
dado = []
for c in range (0, 3):
    dado.append(str (input ('Nome: ')))
    dado.append(int (input ('Idade: ')))
    galera.append(dado[:])
    dado.clear()

print (galera)

for pessoa in galera:
    if pessoa[1] > 18:
        print (f'{pessoa[0]} é maior de idade.')
    else:
        print (f'{pessoa[0]} é menor de idade.')

""" # um append soh, porem desse jeito cria uma lista dentro da outra
lista = []
nome = str (input ('Nome: '))
idade = int (input ('Idade: '))
nota = float (input ('Nota: '))
lista.append([nome, idade, nota])

print (lista) """







