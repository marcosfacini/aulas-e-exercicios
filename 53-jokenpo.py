escolha = int (input ('''Digite a sua opção:
Digite 0 para escolher pedra.
Digite 1 para escolher papel.
Digite 2 para escolher tesoura.
Seu escolha é: '''))

if escolha > 2:
    print ('Número inválido. Digite um número entre 0 e 2')
    exit()

from random import choice
from time import sleep
pc = choice([0, 1, 2])
print ('JO')
sleep(1)
print ('KEN')
sleep(1)
print ('POW!!!')

if escolha == 0:
    if pc == 0:
        print ('Você escolheu pedra e eu escolhi pedra: DEU EMPATE!')
    elif pc == 1:
        print ('Você escolheu pedra e eu escolhi papel: EU GANHEI!')
    else:
        print ('Você escolheu pedra e eu escolhi tesoura: VOCÊ GANHOU!')        

elif escolha == 1:
    if pc == 0:
        print ('Você escolheu papel e eu escolhi pedra: VOCÊ GANHOU!')
    elif pc == 1:
        print ('Você escolheu papel e eu escolhi papel: DEU EMPATE!')  
    elif pc == 2:
        print ('Você escolheu papel e eu escolhi tesoura: EU GANHEI!') 

elif escolha == 2:
    if pc == 0:
        print ('Você escolheu tesoura e eu escolhi pedra: EU GANHEI!')
    elif pc == 1:
        print ('Você escolheu tesoura e eu escolhi papel: VOCÊ GANHOU!')    
    else:
        print ('Você escolheu tesoura e eu escolhi tesoura: DEU EMPATE!')

