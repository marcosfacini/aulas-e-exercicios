
# keys são as chaves/titulos ex: nome, sexo, idade
# values são os valores/significados ex: Marcos, Masculino, 28
# item é o dicionário todo

# dicionario = {'Nome': 'Marcos', 'Sexo': 'Masculino', 'Idade': 28}
""" print (dicionario)
print (dicionario['Idade'])

# aspas duplas dentro das chaves e referencia a posição com colchetes
print (f'O {dicionario["Nome"]} tem {dicionario["Idade"]} anos.')

# mostrando apenas os keys/titulos
print (dicionario.keys())

# mostrando apenas os valores/significados
print (dicionario.values())

# mostrando o dicionário completo
print (dicionario.items()) """

""" # para cada chave no dicionário:
for key in dicionario.keys():
    print (key)

# para cada valor no dicionario:
for value in dicionario.values():
    print (value)

# no dicionario nao se ultilizado o enumerate, se usa o .items()
# para mostrar cada chave e valor:
for key, value in dicionario.items():
    print (f'{key} = {value}')

# para deletar uma chave junto com o seu valor:
del dicionario['Sexo']
print (dicionario) """

# para mudar o valor de uma chave
""" dicionario['Nome'] = 'João'
print(dicionario) """

# adicionar mais um elemento ao dicionário - não se usa o append()
""" dicionario['peso'] = 74.5
print (dicionario) """

# criar um dicionario dentro de uma lista
""" brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print (brasil)
print (brasil[1])
print (brasil[0]['uf']) """

# metodo copy() no append para copiar um dicionario para dentro de uma lista
estado = {}
brasil = []
for c in range(0, 3):
    estado['uf'] = str (input ('Estado: '))
    estado['sigla'] = str (input ('Sigla: '))
    brasil.append(estado.copy())
""" print (brasil)

# para mostrar cada elemento de dicionario dentro da lista
for estado in brasil:
    print (estado)

# um for dentro de outro para mostrar os keys e values dentro de uma lista separadamente
for estado in brasil:
    for key, value in estado.items():
        print (f'A chave {key} tem o valor {value}') """

# ou acessar só os valores
# laço de fora e para a lista e o laco de dentro para o dicionario
for estado in brasil:
    for value in estado.values():
        print (value, end=' ')
    print()

# jeito mais simples de printar key e value juntos sem o .items()
# num dicionário simples que não está dentro de uma lista
# nesse caso {nome} representa o key e {info[nome]} representa o value
info = {'nome1': 'marcos', 'nome2': 'mayara', 'nome3': 'vitoria'}
for nome in info:
    print (f'{nome} = {info[nome]}')