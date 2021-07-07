# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). 
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista 
# e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

from random import randint

def sorteia(lista):
    for c in range(0, 5):
        numb = randint(1, 99)
        lista.append(numb)
    print (f'Os numeros sorteados foram: {numeros}')

def somaPar(lista):
    total = 0
    print ('Os números pares são: ', end='')
    for n in numeros:
        if n % 2 == 0:
            print (n, end=' ')
            total += n
    print (f'A soma dos números pares é: {total}')

numeros = []
sorteia(numeros)
somaPar(numeros)




