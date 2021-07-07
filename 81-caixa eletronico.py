# Crie um programa que simule o funcionamento de um caixa eletrônico. 
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) 
# e o programa vai informar quantas cédulas de cada valor serão entregues.
# considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

valor = int (input ('Quanto você quer sacar?: R$'))
total = valor
cedula = 50
contador_cedula = 0

while True:
    if total >= cedula:
        total -= cedula 
        contador_cedula += 1
    else:
        if contador_cedula > 0:
            print (f'Total de {contador_cedula} cédulas de R${cedula} ')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        contador_cedula = 0
        if total == 0:
            break

print ('Obrigado e volte sempre.')

    



    