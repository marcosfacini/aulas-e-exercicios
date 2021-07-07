# Crie um programa que leia o nome e o preço de vários produtos. 
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# qual é o total gasto na compra.
# quantos produtos custam mais de R$1000.
# qual é o nome do produto mais barato. 

total = contador_preco = contador_barato = preco_barato = 0 
nome_barato = ''
while True:
    nome = str (input ('Digite o nome do produto: '))
    preco = float (input ('Digite o preço do produto: R$'))
    contador_barato +=1

    total += preco
    if preco > 1000:
        contador_preco += 1
    if contador_barato == 1 or preco < preco_barato:
        nome_barato = nome
        preco_barato = preco

    opcao = str (input ('Deseja continuar? S/N: ')).strip().upper()[0]
    while opcao != 'S' and opcao != 'N':
        opcao = str (input ('Digite S ou N: ')).strip().upper()[0]
    if opcao == 'N':
        print ('Obrigado pelas informações.')
        break

print (f'O total gasto foi de {total:.2f}')
print (f'{contador_preco} produtos custam mais de R$ 1.000,00')
print (f'O produto mais barato é {nome_barato} custando R${preco_barato:.2f}')