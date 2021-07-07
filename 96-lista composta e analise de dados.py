# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# Quantas pessoas foram cadastradas. 
# Uma listagem com as pessoas mais pesadas.
# Uma listagem com as pessoas mais leves.

pessoas = []
dados = []
contador = 0
leves = []
maior = 0
menor = 0

while True:
    dados.append(str (input ('Digite o nome: ')))
    dados.append(float (input ('Digite o peso: ')))
    if contador == 0:
        maior = dados[1]
        menor = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    
    contador += 1

    menu = str (input ('Deseja continuar? S/N: ')).strip().upper()[0]
    while menu != 'S'and menu != 'N':
        menu = str (input ('Letra Inválida. Digite S ou N: ')).strip().upper()[0]
    if menu == 'N':
        break

print (f'Foram cadastradas {contador} pessoas.')
# com o len()
# print (f'Foram cadastradas {len(pessoas)} pesssoas')

# ou imprimo um na frente do outro
print (f'Os acima de 90 kg são: ', end='')
for p in pessoas:
    if p[1] >= 90:
        print (f'{p[0]}', end=',')
    if p[1] > maior:
        maior = p[1]
    if p[1] < menor:
        menor = p[1]

print (f'\nO maior peso foi: {maior}')

# ou jogo tudo numa lista e depois imprimo a lista
for p in pessoas:
    if p[1] <= 60:
        leves.append(p[0])
print(f'As pessoas abaixo de 60 kg são: {leves}')
print (f'O peso mais leve foi: {menor}')

    




