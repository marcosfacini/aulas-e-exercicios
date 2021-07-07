# Faça um programa que tenha uma função chamada maior(), 
# que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

def maior(*n):
    maior = contador = 0
    for number in n:
        if contador == 0:
            maior = number
        else:
            if number > maior:
                maior = number
        contador += 1
    print (f'Você digitou {contador} números. Entre {n} o maior número é o {maior}')


maior(2, 4, 6, 8)
maior(7, 4, 10, 2, 1)
maior(6)
maior()
