# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. 
# Caso o número já exista lá dentro, ele não será adicionado. 
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente. 

lista = []
while True:
    numeros = int (input ('Digite um número: '))

    if numeros in lista:
        print ('Numero já existente')
        
    else:
        lista += [numeros]
        print ('Número adicionado com sucesso.')

    menu = str (input ('Deseja continuar? S/N: ')).strip().upper()[0]
    while menu != 'S' and menu != 'N':
        menu = str (input ('Letra Inválida. Digite S ou N para continuar: ')).strip().upper()[0]
    if menu == 'N':
        break
    
# metodo .sort() primeiro só modifica a lista, e depois você consegue printar a lista nova
lista.sort()
print (f'Os valores digitados foram: {lista}')


