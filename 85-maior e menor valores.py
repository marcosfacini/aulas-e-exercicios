# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. 
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint
numeros = (randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100))
print ('Os números são: ', end='')
for n in numeros:
    print (n, end=' ')
print (f'\nO maior número é: {max(numeros)}')
print (f'O menor valor é: {min(numeros)}')


# tuple() coloca dentro de uma tupla
# é possível ultilizar o método sample
""" from random import sample
a = tuple(sample(range(1, 100), 5))
print(f'Os números sorteados são: {a}')
print(f'O maior valor é {max(a)} e o menor é {min(a)}.') """


