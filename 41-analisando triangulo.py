# Desenvolva um programa que leia o comprimento de três retas 
# e diga ao usuário se elas podem ou não formar um triângulo.

print ('-=-' * 30) 
print ('Analisando triângulos')
print ('-=-' * 30)
r1 = float (input ('Digite o tamanho da primeira reta: '))
r2 = float (input ('Digite o tamanho da segunda reta: '))
r3 = float (input ('Digite o tamanho da terceira reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os seguimentos acima podem formar um triângulo')
else:
    print ('Os seguimentos a cima não podem formar um triângulo')

