# Escreva um programa em Python que leia um número inteiro qualquer 
# e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

num = int (input ('Digite o número que deseja converter: '))
convert = int (input ('Digite 1 para binário, 2 para octal e 3 para hexadecimal: '))

if convert == 1:
    print (f'A conversão para binário fica: {num:b}')
elif convert == 2:
    print (f'A conversão para octal fica: {num:o}')
elif convert == 3:
    print (f'A conversão para hexadecimal fica: {num:#x}')
else:
    print ('Número não reconhecido')        

# outra forma descrita na documentação:
# também é possível formatar se quer que apareça o prefixo colocando # depois dos dois pontos no format

# binario = bin(16)
# print (binario)   

# octal = oct(8)
# print (octal)

# hexa = hex(255)
# print (hexa)

# também é possível simplismente apagar os dois primeiros numeros com o comando [2:]
# print (f'A conversão para binário fica: {bin(num)[2:]}')