# Crie um programa que vai ler vários números e colocar em uma lista. 
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. 
# Ao final, mostre o conteúdo das três listas geradas.

lista = []
par = []
impar = []

while True:
    numero = int (input ('Digite um número: '))
    lista += [numero]
    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)

    menu = str (input ('Deseja continuar? S/N: ')).strip().upper()[0]
    if menu == 'N':
        break
    if menu != 'S' and menu != 'N':
        menu = str (input ('Letra Inválida. Digite S ou N: ')).strip().upper()[0]

print (f'Os números digitados foram: {lista}')
print (f'Os números pares são: {par}')
print (f'Os números ímpares são: {impar}')