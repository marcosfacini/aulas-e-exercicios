# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, 
# indo de 10 até 0, com uma pausa de 1 segundo entre eles.
# mostre emoji de explosão!

import emoji
from time import sleep
print (f'{" FIM DO ANO!!! ":=^60}')
for c in range (10, -1, -1):
    print (c)
    sleep(1)
print (emoji.emojize(':boom:', use_aliases=True) * 10 , 'BOOM!!!!', emoji.emojize(':boom:', use_aliases=True) * 10)    