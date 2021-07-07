# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

maior = 0
menor = 0
for pessoas in range (1, 6):
    peso = float (input (f'Qual é o peso da {pessoas}º pessoa?: '))
    # assume-se que o primeiro do laço vai ter o menor e o maior peso
    if pessoas == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso        

print(f'O maior peso foi {maior:.2f}kg e o menor peso foi {menor:.2f}kg')    

# outro jeito de resolver, usando uma lista vazia e acrescentado os valores nela:
lst=[]  #lista vazia
for c in range(1, 6):
    peso=float(input('Peso da {}ª pessoa: '.format(c)))
    lst+=[peso]   #adc os valores de peso na lista
print('')
print('O Maior peso foi:', max(lst))  #maximo valor da lista
print('O Menor peso foi:', min(lst))  #minimo valor da lista

# ou ordenando a lista:
pesos = []
for i in range(1,6):
    peso = float(input(f"Qual o peso da {i}ª pessoa? "))
    pesos += [peso]
pesos.sort()
print(f'O maior peso lido foi de {pesos[4]} Kg e o menor peso foi de {pesos[0]}')