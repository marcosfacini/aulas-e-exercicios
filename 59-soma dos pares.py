# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. 
# Se o valor digitado for ímpar, desconsidere-o.

acumulador = 0
contador = 0
for c in range (1,7):
    numero = int (input (f'Digite o {c}º valor: '))
    if numero % 2 == 0:
        acumulador += numero
        contador += 1
if contador == 1:
    print (f'Você informou apenas um número par, que foi o número: {acumulador}') 
elif contador == 0:
    print ('Você não informou nenhum número par.')
else:               
    print (f'A soma dos {contador} números pares é: {acumulador}')

