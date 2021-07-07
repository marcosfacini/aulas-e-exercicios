# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e 
# peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. 
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

# comando sleep da biblioteca time faz o programa finger que está pensando a quantidade de segundos indicado entre os parenteses

# é possível enfeitar as linhas de comando com tracinhos indicando quantas vezes queremos que eles apareçam

from random import randint
from time import sleep
num = randint(0, 5)
print ('-=-' * 30)
print('Eu pensei em um número entre 0 e 5...Vamos ver se você consegue adivinhar...')
print ('-=-' * 30)
chute = int (input ('Em qual número eu pensei?: '))
print ('Processando...')
sleep(3)
if chute == num:
    print ('Parabéns você acertou!')
else:
    print(f'Você não conseguiu adivinhar dessa vez...Eu pensei no {num} e você no {chute}')    
