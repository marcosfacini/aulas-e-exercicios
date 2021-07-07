# Faça um programa que leia o nome completo de uma pessoa, 
# mostrando em seguida o primeiro e o último nome separadamente.

nome = str (input ('Qual é o seu nome completo?: ')).split()
print (f'O seu primeiro nome é: {nome[0]}')
# posição [-1] se refere a ultima da lista
print (f'O seu ultimo nome é: {nome[-1]}')