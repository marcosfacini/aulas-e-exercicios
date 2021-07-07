# Faça um programa que jogue par ou ímpar com o computador. 
# O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo. 

from random import randint
contador = 0
while True:
    num_jogador = int (input ('Escolha um número: '))
    opcao_jogador = str (input ('Escolha P para PAR e I para IMPAR: ')).strip().upper()[0]
    while opcao_jogador != 'I' and opcao_jogador != 'P':
        print ('Letra Inválida. Digite novamente.')
        opcao_jogador = str (input ('Escolha P para PAR e I para IMPAR: ')).strip().upper()[0]
    num_pc = randint(0, 10)
    soma = (num_jogador + num_pc)
    if soma % 2 == 0:
        resultado = 'P'
    else:
        resultado = 'I'
    if opcao_jogador == 'P' and resultado == 'I':
        print (f'Você colocou {num_jogador} e eu coloquei {num_pc}. A soma deu {soma}. Deu IMPAR. Eu ganhei!')
        break
    elif opcao_jogador == 'I' and resultado == 'P':
        print (f'Você colocou {num_jogador} e eu coloquei {num_pc}. A soma deu {soma}. Deu PAR. Eu ganhei!')
        break
    elif opcao_jogador == 'P' and resultado == 'P':
        contador += 1
        print (f'Você colocou {num_jogador} e eu coloquei {num_pc}. A soma deu {soma}. Deu PAR. Você ganhou!')
    elif opcao_jogador == 'I' and resultado == 'I':
        contador += 1
        print (f'Você colocou {num_jogador} e eu coloquei {num_pc}. A soma deu {soma}. Deu IMPAR. Você ganhou!')
    print ('Vamos jogar novamente...')
    
print (f'Você perdeu. E me venceu {contador} vezes.')
        

