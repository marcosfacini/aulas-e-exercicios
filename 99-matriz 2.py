# Aprimore o desafio anterior, mostrando no final: 
# A soma de todos os valores pares digitados.
# A soma dos valores da terceira coluna.
# O maior valor da segunda linha.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = somacoluna = maiorlinha = 0
for linha in range (0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int (input (f'Digite um valor para a posição [{linha}, {coluna}]: '))
for linha in range(0, 3):
    for coluna in range(0, 3):
        print (f'[{matriz[linha][coluna]:^5}]', end='')
        if matriz[linha][coluna] % 2 == 0:
            par += matriz[linha][coluna]
    print()
    
for linha in range(0, 3):
    somacoluna += matriz[linha][2]

for coluna in range(0, 3):
    if coluna == 0:
        maiorlinha = matriz[1][0]
    elif matriz[1][coluna] > maiorlinha:
        maiorlinha = matriz[1][coluna]
     
print (f'A soma dos números pares é: {par}')
print (f'A soma dos valores da terceira coluna é: {somacoluna}')
print (f'A maior valor da segunda linha é: {maiorlinha}')
# ou usando o metodo max diretamente
# print (f'O maior valor da segunda linha é: {max(matriz[1])}')






