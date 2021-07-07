# Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120

# usando o while:
""" numero = int(input("Fatorial de: ") )

resultado = 1
count = 1

print (f'{numero}! = ', end='')

while count <= numero:
    resultado *= count
    count += 1

print (f'{resultado}') """
    
    


""" # usando o for:
numero = int(input("Fatorial de: ") )
resultado = 1

for fator in range(1,numero+1):
    resultado *= fator

print(resultado)



# usando modulo:
from math import factorial
numero = int(input("Fatorial de: ") )
print (f'O fatorial de {numero} é {factorial(numero)}') """

# pode-se usar um if/else dentro do print
numero = int (input ('Digite um número: '))
contagem = numero
resultado = 1

print (f'{numero}! =', end=' ')
while contagem > 0:
    print (f'{contagem}', end=' ')
    print ('x' if contagem > 1 else '=', end=' ')
    resultado *= contagem
    contagem -= 1

print (resultado)

