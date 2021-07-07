# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# Quantas vezes apareceu o valor 9.
# Em que posição foi digitado o primeiro valor 3.
# Quais foram os números pares.

n1 = int (input ('Digite o primeiro valor: '))
n2 = int (input ('Digite o segundo valor: '))
n3 = int (input ('Digite o terceiro valor: '))
n4 = int (input ('Digite o quarto valor: '))

tupla = (n1, n2, n3, n4)

print (f'O valor 9 apareceu {tupla.count(9)} vezes.')
if 3 in tupla:
    print (f'O valor 3 foi digitado na {tupla.index(3)+1}º posição.') 
else:
    print('O número 3 não foi digitado.')
print ('Os números pares são: ', end='')

if n1 % 2 == 0:
    print (n1, end=' ')
if n2 % 2 == 0:
    print (n2, end=' ')
if n3 % 2 == 0:
    print (n3, end=' ')
if n4 % 2 == 0:
    print (n4, end=' ')

# usando o for e colocando os números de input direto na tupla
números = (int (input ('Digite o primeiro valor: ')), int (input ('Digite o segundo valor: ')), 
int (input ('Digite o terceiro valor: ')), int (input ('Digite o quarto valor: ')))

print (f'O valor 9 apareceu {números.count(9)} vezes.')
if 3 in números:
    print (f'O número 3 apareceu na posição {números.index(3)+1}')
else:
    print ('O número 3 não apareceu.')

print ('Os valores pares foram: ', end='')
for n in números:
    if n % 2 == 0:
        print (n, end=' ')




