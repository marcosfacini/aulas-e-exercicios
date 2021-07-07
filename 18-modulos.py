# import + nome do modulo = importa a biblioteca inteira desse modulo
import math
num = int (input ('Digite o número que você quer saber a raiz quadrada: '))
raiz = math.sqrt(num)

print (f'A raiz quadrada de {num} é {raiz:.2f}')



# from + nome do modulo + import + nome do arquivo especifico dentro da biblioteca = importa só o arquivo especifico
# dessa maneira nao tem necessidade do .math na variavel raiz
# from math import sqrt
# num = int (input ('Digite o número: '))
# raiz = sqrt(num)

# print (f'A raiz quadrada de {num} é {raiz:.2f}')



# para importar mais de uma, mas não todas, apenas colocar a vírgula na frente
# from math import sqrt, pow


# ultilizar comando (ceil) para arredondar valor para cima
# import math
# num = int (input ('Digite um número: '))
# raiz = math.sqrt(num)

# print ('A raiz quadrada de {} é {}'.format (num, math.ceil(raiz)))

# ultilizar comando (floor) para arredondar valor para baixo
# import math
# num = int (input ('Digite o número: '))
# raiz = math.sqrt(num)

# print ('A raiz quadrada de {} é {}'.format (num, math.floor(raiz)))

# import random
# numero aleatório de 0 a 1 com:
# print (random.random)
# demilitar a aleatoriedade dos numeros com:
# print (random.randint (1, 10))



