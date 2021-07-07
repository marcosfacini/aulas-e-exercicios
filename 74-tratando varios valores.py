# Crie um programa que leia vários números inteiros pelo teclado. 
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

numero = int (input ('Digite um número ou digite 999 para parar: '))
contador = 0
somador = 0

while numero != 999:
    somador += numero
    contador += 1
    numero = int (input ('Digite um número ou digite 999 para parar: '))

print (f'Você digitou {contador} valores e a soma deles é: {somador}')