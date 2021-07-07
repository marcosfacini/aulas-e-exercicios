# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: 
# o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, 
# mesmo que algum dado não tenha sido informado corretamente.

def ficha(jogador='<desconhecido>', gols=0):
    if jogador.strip() == '':
        jogador = 'Desconhecido'
    if gols.strip() == '':
        gols = 0
    if gols.isnumeric() == False:
        gols = 0
    if jogador.isnumeric():
        jogador = 'Desconhecido'
    return f'O jogador {jogador} fez {gols} gols.'
    

nome = str (input ('Qual o nome do jogador?: '))
quantidade = str (input ('Quantos gols ele fez?: '))
print (ficha(nome, quantidade))
