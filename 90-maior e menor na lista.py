# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. 
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista. 

# só pegando a primeira posição:
""" n = 1
numeros = []
for num in range (0, 5):
    numeros.append(int (input (f'Digite o {n}º número: ')))
    n += 1
    

print (f'O maior valor foi: {max(numeros)} na posição {numeros.index(max(numeros))+1}')
print (f'O menor valor foi {min(numeros)} na posição {numeros.index(min(numeros))+1}') """

# pegando todas as posições em que ocorre:
numeros = []
for num in range (0, 5):
    numeros.append(int (input (f'Digite um valor para a posição {num}: ')))

print (f'Você digitou os valores {numeros}')

maior = numeros[0]
menor = numeros[0]

for num in numeros:
    if num > maior:
        maior = num
    if num < menor:
        menor = num

# para não printar a frase várias vezes, colocar ela antes do for
print (f'O maior valor é: {maior} na posição: ', end='')
for posicao, elemento in enumerate(numeros):
    if elemento == maior:
        print (f'{posicao}, ', end='')

# pode-se quebrar um end='' com um print vazio, ou com o quebra de linha \n
print()

print (f'O menor valor é {menor} na posição: ', end='')
for posicao, elemento in enumerate(numeros):
    if elemento == menor:
        print(f'{posicao}, ', end='')
        


