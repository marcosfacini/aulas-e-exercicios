# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados

num = int (input ('Digite um número de 0 a 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print (f'Analisando o número {num} temos:')
print (f'Unidade: {u}')
print (f'Dezena: {d}')
print (f'Centena: {c}')
print (f'Milhar: {m}')



# em formato string tem o problema de dar erro se não digitar os 4 numeros
# num = str (input ('digite um número de 0 a 9999: '))
# print (f'Analisando o número {num} temos:')
# print (f'Unidade: {num[3]}')
# print (f'Dezena: {num[2]}')
# print (f'Centena: {num[1]}')
# print (f'Milhar: {num[0]}')
