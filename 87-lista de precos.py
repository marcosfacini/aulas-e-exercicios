# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. 
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

tupla = ('Lápis', 1.50, 'Caneta', 3.20, 'Caderno', 5.10, 'Estojo', 4.90, 'Computador', 877.50,
'Mouse', 26.10, 'Teclado', 55.00, 'Tablet', 329.99, 'Mochila', 35.00, 'Cobertor', 114.45)

for posição in range(0, len(tupla)):
    if posição % 2 == 0:
        print (f'{tupla[posição]:.<30}', end='')
    else:
        print (f'R${tupla[posição]:>7.2f}')

# outro jeito:
""" for c in range(0, len(tupla), 2):
    print(f"{tupla[c]:.<40}", f" R$ {tupla[c+1]:>7.2f}") """


# verificando o tipo da variavel
""" for i in tupla:
    if type(i) is str:
        print(f'{i:.<32}', end='')
    else:
        print(f'R$ {i:>5.2f}') """