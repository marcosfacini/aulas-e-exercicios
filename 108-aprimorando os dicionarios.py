# Aprimore o exercicio 106 para que ele funcione com vários jogadores, 
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

jogadores = []
while True:
    status = {}
    status['nome'] = str (input ('Nome: '))
    partidas = int (input (f'Quantas partidas {status["nome"]} jogou?: '))
    gols = []
    for jogo in range(0, partidas):
        gols.append(int (input (f'Quantos gols na partida {jogo+1}?: ')))
    status['gols'] = gols[:]
    total = sum(gols)
    status['total'] = total
    jogadores.append(status.copy())
    menu = str (input ('Deseja continuar?: S/N: ')).upper()[0]
    while menu != 'S' and menu != 'N':
        menu = str (input ('Letra Inválida digite S ou N: ')).upper()[0]
    if menu == 'N':
        break

# gambiarra convertendo os valores do dicionario para string para poder formata-los
""" print (f'{"COD":<5} {"NOME":<30} {"GOLS":<20} {"TOTAL":<5}')
for posicao, valor in enumerate(jogadores):
    nome = str (valor['nome'])
    num_gols = str (valor['gols'])
    tot = str (valor['total'])
    print (f'{posicao:<5} {nome:<30} {num_gols:<20} {tot:<5}') """

# usando o for e convertendo o valor para string direto dentro do f stings f'{str ()}
print ('COD  ', end='')
for key in status.keys():
    print (f'{key:<15}', end='')
print ()
for posicao, valor in enumerate(jogadores):
    print (f'{posicao:<5}', end='')
    for valor in valor.values():
        print (f'{str (valor):<15}', end='')
    print ()

while True:
    dados = int (input ('Deseja ver os dados de qual jogador?: (999 para encerrar): '))
    if dados == 999:
        break
    if dados > len(jogadores)-1:
        print ((f'Posição {dados} não existe. Digite a posição do jogador.'))
    else:
        print (f'Levantamento do jogador {jogadores[dados]["nome"]}')

        for posicao, valor in enumerate(jogadores[dados]['gols']):
            print (f'Na partida {posicao+1} fez {valor} gols.')

        # outro jeito:
        """ for jog in range (0, len(jogadores[dados]['gols'])):
            print (f'Na partida {jog+1} fez {jogadores[dados]["gols"][jog]} gols.') """

        print (f'O jogador {jogadores[dados]["nome"]} fez um total de {jogadores[dados]["total"]} gols.')
    
        



