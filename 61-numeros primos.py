# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

# Números primos são aqueles divisíveis APENAS por 1 e por eles mesmos.
# ou seja, se um número for divisivel por mais de 2 números ou por menos de 2 numeros, como é o caso do 1, ele não é primo.

contador = 0
numero = int (input ('Digite um número: '))
for c in range (1, numero+1):
    if numero % c == 0:
        contador += 1
        print ('\33[34m', end=' ')
    else:
        print ('\33[m', end=' ')    
    print ('{}'.format(c), end=' ')
if contador == 2:
    print (f'\n\33[mO número {numero} é primo.')    
else:
    print (f'\n\33[mO número {numero} não é primo.')    