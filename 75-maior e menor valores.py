# Crie um programa que leia vários números inteiros pelo teclado. 
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

opcao = 'S'
contador = somador = maior = menor = 0

while opcao != 'N':
    numero = int (input ('Digite um número: '))
    contador += 1
    somador += numero
    if contador == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        elif numero < menor:
            menor = numero
    opcao = str (input ('Deseja continuar? S/N: ')).upper().strip()
    
media = somador / contador

print (f'A media desses {contador} valores é {media}')
print (f'O maior valor é {maior} e o menor valor é {menor}')


