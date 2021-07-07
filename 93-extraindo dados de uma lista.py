# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# Quantos números foram digitados.
# A lista de valores, ordenada de forma decrescente.
# Se o valor 5 foi digitado e está ou não na lista.

lista = []
while True:
    lista.append(int (input ('Digite um valor: ')))

    menu = str (input ('Deseja continuar? S/N: ')).strip().upper()[0]
    if menu != 'S' and menu != 'N':
        menu = str (input ('Letra Inválida. Digite S ou N: ')).strip().upper()[0]
    if menu == 'N':
        break

print (f'Foram digitados {len(lista)} números.')

if 5 in lista:
    print (f'O número 5 foi digitado na posição: {lista.index(5)+1}')
else:
    print (f'O número 5 não foi digitado.')

lista.sort(reverse = True)
print (f'Ordem decrescente dos valores digitados: {lista}')
