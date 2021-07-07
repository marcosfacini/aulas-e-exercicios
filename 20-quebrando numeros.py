# transformando um número real em inteiro

import math
num = float (input('Digite um número real: '))
inteiro = math.trunc(num)
print (f'Esse número inteiro é: {inteiro}')

# ou assim já importando o método específico tirando a necessidade do math. antes do trunc
# desse jeito se economiza memoria na execução pq não chama a biblioteca inteira do math
# e sem a necessidade de declarar a variavel colocando ela direto no format

# from math import trunc
# num = float (input ('Digite um número real: '))
# print (f'O número inteiro de {trunc(num)}')

# ou simplesmente por declarar a variavel como numero inteiro, sem a necessidade de importar nenhum metodo
# num = float (input('Digite um número real: '))
# print (f'Esse número inteiro é: {int(num)}')