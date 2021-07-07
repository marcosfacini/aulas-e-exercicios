# é possivel criar seu proprio modulo e importa-lo para dentro do seu programa principal,
# desde que o arquivo do modulo esteja na mesma pasta do arquivo do programa principal
# isso deixa o codigo menor e mais organizado

import uteis

num = int (input ('Digite um numero: '))
fat = uteis.fatorial(num)
print (f'O fatorial de {num} é {fat}')
print (f'O dobro de {num} é {uteis.dobro(num)}')
print (f'O triplo de {num} é {uteis.triplo(num)}')

# caso o programa tenha muitos modulos, eles podem ser organizados dentro de um pacote/biblioteca
# essas subpastas contendo os modulos, devem conter o arquivo:  __init__.py