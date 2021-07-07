# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, 
# cadastrando tudo em uma lista composta.

from random import randint
from time import sleep

lista = []
total = []

num_jogos = int (input ('Quantos jogos você quer?: '))
print (f'Os {num_jogos} jogos gerados foram: ')

for jogo in range (1, num_jogos+1):
    contador = 0
    while True:
        numero = randint(1, 60)
        if numero not in lista:
            lista.append(numero)
            contador += 1
        if contador == 6:
            break
    lista.sort()
    total.append(lista[:])
    lista.clear()

for posicao, numero in enumerate(total):
    print (f'{posicao+1}º Jogo: {total[posicao]}')
    sleep(1)

# ou usar o metodo sample do random
""" for jogo in range (0, num_jogos):
    print (f'{jogo+1}º Jogo: {sample(range(1, 61), 6)}')
    sleep(1) """

