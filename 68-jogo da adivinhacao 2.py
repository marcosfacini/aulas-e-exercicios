# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. 
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

# desse jeito com a variavel num_pc dentro do while a cada tentativa o numero muda.
""" from random import randint
num_pc = randint(0, 10)
palpites = 0
num_jogador = int (input ('Digite um número entre 0 e 10: '))

while num_jogador > 10:
    num_jogador = int (input ('Valor Inválido. Digite um número entre 0 e 10: '))

while num_jogador != num_pc:
    num_jogador = int (input (f'Você errou! Eu pensei no {num_pc} e você no {num_jogador}.\nTente outra vez: '))
    num_pc = randint(0, 10)
    palpites += 1

print (f'Você acertou! Eu também pensei no {num_jogador}. Você precisou de {palpites} tentativas para acertar.') """

# desse outra forma o numero sempre continua o mesmo e te dá dicas até acertar.
from random import randint
num_pc = randint(0, 10)
palpites = 0
num_jogador = int (input ('Digite um número entre 0 e 10: '))

while num_jogador > 10:
    num_jogador = int (input ('Valor Inválido. Digite um número entre 0 e 10: '))

while num_jogador != num_pc:
    if num_jogador > num_pc:
        num_jogador = int (input (f'Você errou! É um número mais baixo que {num_jogador}. Tente outra vez: '))
    else:
        num_jogador = int (input (f'Você errou! É um número mais alto que {num_jogador}. Tente outra vez: '))
    palpites += 1

if palpites > 1:
    print (f'Você acertou! Eu também pensei no {num_jogador}. Você precisou de {palpites} chances bônus para acertar.')
elif palpites == 1:
    print (f'Você acertou! Eu também pensei no {num_jogador}. Você precisou de {palpites} chance bônus para acertar.') # sem o plural
else:
    print (f'Parabéns! Você acertou de primeira!') 


# versão com True e False dentro do while:
from random import randint
from time import sleep
computador = randint(0, 10)
print('Sou seu computador...Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue advinhar qual foi?')
acertou = False
palpites = 0
# enquanto acertou for not/FALSE ele fica no loop
while not acertou:
    jogador = int(input('Qual seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Tente um número maior!')
        elif jogador > computador:
            print('Tente um número menor!')
print('Analisando...'), sleep(3)
print('Você acertou com {} tentativas! Parabéns'.format(palpites))




