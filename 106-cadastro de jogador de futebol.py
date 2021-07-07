# Crie um programa que gerencie o aproveitamento de um jogador de futebol. 
# O programa vai ler o nome do jogador e quantas partidas ele jogou. 
# Depois vai ler a quantidade de gols feitos em cada partida. 
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

status = {'nome': str (input ('Nome: '))}
partidas = int (input (f'Quantas partidas {status["nome"]} jogou?: '))

gols = []
for jogo in range(0, partidas):
    gols.append(int (input (f'Quantos gols na partida {jogo+1}?: ')))

total = 0
for partida in gols:
    total += partida
# ou usar a função de soma
# sum(gols)

print ('=' * 40)
status['gols'] = gols[:]
status['total'] = total
print (status)
print ('=' * 40)

for item in status:
    print (f'O campo {item} tem o valor {status[item]}')
print ('=' * 40)

print (f'O jogador {status["nome"]} jogou {partidas} partidas.')
for partida, gol in enumerate(gols):
    print (f'Na partida {partida+1} fez {gol} gols.')

print (f'Foi um total de {total} gols.')

