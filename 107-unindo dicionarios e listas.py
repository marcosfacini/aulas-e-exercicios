# Crie um programa que leia nome, sexo e idade de várias pessoas, 
# guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: 
# Quantas pessoas foram cadastradas
# A média de idade
# Uma lista com as mulheres
# Uma lista de pessoas com idade acima da média

lista = []
while True:
    pessoa = {}
    pessoa['nome'] = str (input ('Nome: '))
    pessoa['sexo'] = str (input ('Sexo: F/M: ')).upper()[0]
    while pessoa['sexo'] != 'F' and pessoa['sexo'] != 'M':
        pessoa['sexo'] = str (input ('Letra inválida. Digite F ou M: ')).upper()[0]
    pessoa['idade'] = int (input ('Idade: '))
    lista.append(pessoa)
    menu = str (input ('Deseja continuar?: S/N: ')).upper()[0]
    while menu != 'S' and menu != 'N':
        menu = str (input ('Letra Inválida. Digite S ou N: ')).upper()[0]
    if menu == 'N':
        break

print (f'Foram cadastradas {len(lista)} pessoas.')

total = 0
for p, v in enumerate(lista):
    total += lista[p]['idade']
media = total/len(lista)
print (f'A média de idade é: {media:.2f}')

""" mulheres = []
for p, v in enumerate(lista):
    if lista[p]['sexo'] == 'F':
        mulheres.append(lista[p]['nome'])
print (f'As mulheres são: {mulheres}') """

# poderia fazer sem jogar o nome na lista e sem usar o enumerate:
print ('As mulheres cadastradas foram: ', end='')
for p in lista:
    if p['sexo'] == 'F':
        print (f'{p["nome"]} ', end='') 
print ()

""" print ('As pessoas acima da média de idade são: ')
for p, v in enumerate(lista):
    if lista[p]['idade'] > media:
        print (lista[p]) """

# poderia fazer sem o enumerate e com o print formatado:
print ('As pessoas acima da média de idade são: ')
for p in lista:
    if p['idade'] > media:
        print ('    ', end='')
        for k, v in p.items():
            print (f'{k} = {v}; ', end='')
        print()




