""" Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso. """

# maneira simplificada sem usar o True e False:
n1 = int (input ('Digite o primeiro valor: '))
n2 = int (input ('Digite o segundo valor: '))
menu = 0

while menu != 5:
    menu = int (input ("""Digite uma das opções: 
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Qual é a sua opção?: """))
    if menu == 1:
        print (f'{n1} + {n2} = {n1 + n2}')
    elif menu == 2:
        print (f'{n1} x {n2} = {n1 * n2}')
    elif menu == 3:
        if n1 > n2:
            print (f'Entre {n1} e {n2} o maior é: {n1}')
        elif n1 < n2:    
            print (f'Entre {n1} e {n2} o maior é: {n2}')
        elif n1 == n2:
            print ('Os dois número são iguais.')
    elif menu == 4:
        n1 = int (input ('Digite o novo primeiro valor: '))        
        n2 = int (input ('Digite o novo segundo valor: '))
    elif menu == 5:
        print ('Obrigado e volte sempre.')
    else:
        print ('Número Inválido.')


# usando o True ou False:
# pode-se usar o float também e limitar a quantidade de casas decimais com o comando :.2f dentro das chaves do format

n1 = float (input ('Digite o primeiro valor: '))
n2 = float (input ('Digite o segundo valor: '))

condicao = False

while condicao is not True:
    menu = int (input ("""#Digite uma das opções: 
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa
# Qual é a sua opção: """))
    if menu == 1:
        print (f'{n1:.2f} + {n2:.1f} = {n1 + n2:.0f}')
    elif menu == 2:
        print (f'{n1} x {n2} = {n1 * n2}')
    elif menu == 3:
        if n1 > n2:
            print (f'Entre {n1} e {n2} o maior é: {n1}')
        elif n1 < n2:    
            print (f'Entre {n1} e {n2} o maior é: {n2}')
        elif n1 == n2:
            print ('Os dois número são iguais.')
    elif menu == 4:
        n1 = float (input ('Digite o novo primeiro valor: '))        
        n2 = float (input ('Digite o novo segundo valor: '))
    elif menu == 5:
        condicao = True
    else:
        print ('Número Inválido.')

print ('Obrigado e volte sempre.')