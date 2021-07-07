# Refaça o arquivo 10, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

contador = 0
numero = int (input ('Digite o número da tabuada que deseja fazer: '))
for c in range (1, 11):
    tabuada = numero * c
    contador += 1
    print (f'{numero} X {contador} = {tabuada}')

# daria para fazer sem a variavel contador:
numero = int (input ('Digite o número da tabuada que deseja fazer: '))
for c in range (1, 11):
    tabuada = numero * c
    print (f'{numero} X {c} = {tabuada}')    
