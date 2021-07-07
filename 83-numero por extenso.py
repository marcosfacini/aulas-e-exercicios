# Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. 
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
# se o numero digitado for maior que 20 ou enor que zero, deve aparecer uma mensagem de erro

extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 
'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

numero = int (input ('Digite um número entre 0 e 20: '))
while numero > 20 or numero < 0:
    numero = int (input ('Número inválido. Digite um número entre 0 e 20: '))

print (f'Você digitou o número {extenso[numero]}')

