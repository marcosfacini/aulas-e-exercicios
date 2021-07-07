# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. 
# Guarde esses resultados em um dicionário em Python. 
# No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep
jogos = {'jogador1': 0, 'jogador2': 0, 'jogador3': 0, 'jogador4': 0}

for key in jogos.keys():
    dado = randint(1, 6)
    jogos[key] = dado
    print (f'{key} tirou: {dado} no dado')
    sleep(1)

print ('=' * 40)
print (f'{"RANKING DOS JOGADORES:":^40}')

""" # para ordenar pelos valores em ordem decrescente com o metodo sorted(.get)
contador = 1
for i in sorted(jogos, key = jogos.get, reverse=True):
    print(f'{contador}° LUGAR: {i} que tirou {jogos[i]}')
    contador += 1 """

# com o metodo itemgetter, o numero entre parenteses se referea posição em que sera ordenado
ranking = []
from operator import itemgetter
ranking = sorted(jogos.items(), key=itemgetter(1), reverse=True) 
print (ranking)
for posicao, valor in enumerate(ranking):
    print (f'Em {posicao+1}° LUGAR ficou o {valor[0]} que tirou {valor[1]}.')
    

    
    

