# Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

for contador in range (2, 51, 2):
    print (contador, end=' ')

# comando end=' ' junta o que ficaria na linha debaixo na mesma linha  

# desse jeito gastaria bem mais memoria porque verificaria todos os números de 1 a 50
for pares in range (1, 51):
    if pares % 2 == 0:
        print (pares, end=' ')  