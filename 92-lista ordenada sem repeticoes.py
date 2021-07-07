# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, 
# já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

valores = []
for valor in range (0, 5):
    numero = int (input ('Digite um valor: '))
    if valor == 0:
        valores.append(numero)
        print ('Adicionado ao final da lista.')
    elif numero > valores[-1]:
        valores.append(numero)
        print ('Adicionado ao final da lista.')
    else:
        posicao = 0
        while posicao < len(valores):
            if numero <= valores[posicao]:
                valores.insert(posicao, numero)
                print (f'Adiconado na posição {posicao} da lista')
                break
            posicao += 1

print (f'Os valores digitados foram: {valores}')