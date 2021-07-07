# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. 
# O programa será interrompido quando o número solicitado for negativo. 

""" while True:
    numero = int (input ('Digite o número da tabuada que deseja visualisar: '))
    if numero < 0:
        print ('Valor negativo')
        break
    for tabuada in range (1, 11):
        resultado = numero * tabuada
        print (f'{numero} X {tabuada} = {resultado}') """

while True:
    numero = int (input ('Digite o número da tabuada que deseja visualisar: '))
    if numero < 0:
        print ('Valor negativo')
        break
    contador = 0
    while contador < 10:
        contador += 1
        resultado = numero * contador
        print (f'{numero} X {contador} = {resultado}')