# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) 
# e mostre a área do terreno.

def area(larg, cumpri):
    total = largura * cumprimento
    print (f'A área do terreno que mede {largura} x {cumprimento} é: {total} m²')

while True:
    largura = float (input ('Digite a largura em metros: '))
    cumprimento = float (input ('Digite o cumprimento em metros: '))
    area(largura, cumprimento)
    menu = str (input ('Deseja continuar?: S/N: ')).upper().strip()[0]
    while menu != 'S' and menu != 'N':
        menu = str (input ('Letra Inválida. Digite S ou N: ')).upper().strip()[0]
    if menu == 'N':
        break

