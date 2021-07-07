# para operações matematicas declarar o tipo como inteiro (int) ou decimal (float) antes do input

""" n1 = int (input ('Digite um valor: '))
n2 = int (input ('Digite ouyto valor: '))
s = n1 + n2

print (f'O resultado de {n1} + {n2} é {s}')

# sem o format seria:
# print ('O resultado de' , n1 , '+' , n2 , 'é:' , s)

# com o format antigo fica:
# print ('O resultado de {} + {} é {}'.format (n1, n2, s))

# editar posição da variavel entre chaves com dois pontos (:) seguido do numero de caracteres
# e alinhar a direita com (>)   alinhar a esquerda com (<)  e centralizar com (^) 
nome = input ('Digite o seu nome:')
print (f'Seu nome é: {nome:^20}!')

# modo format {f'} não permite o uso de barra envertida '\' dentro dele.
# é necessário converter a cor na hora de declarar a variavel, antes de colocar a string dentro das chaves
frase = '\33[34mTeste\33[m'
print (f'{frase}')

# para formatar uma string dentro do modo format {f'} é necessarios colocar aspas duplas nela 
print (f'{" LOJAS PYTHON ":=^100}') """

# para faciliat formatção complexa, ultilizar o .format antigo e concatenar com a virgula
pessoas = 2
print ('='* 30, '{}'.format(pessoas), '=' * 30)

print (f'{" LOJAS PYTHON ":=^10}',f'{pessoas}', f'{"Olá"}')