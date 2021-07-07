# Crie um programa que leia o ano de nascimento de sete pessoas. 
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date
print (date.today().year)
contador = 0
somador = 0
for pessoa in range (1, 8):
    ano = int (input (f'Em que ano a {pessoa}º pessoa nasceu?: '))
    if ano > date.today().year - 18:
        contador += 1
    else:
        somador += 1
print (f'Das pessoas alistadas {contador} são menores e {somador} são maiores.')        

