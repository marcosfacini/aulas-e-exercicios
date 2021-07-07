# tuplas são imutáveis, não posso alterar valores uma vez que já foram definidos na sua criação
# tuplas ficam entre parenteses, mas não é necessário colocá-las entre parenteses, o python já faz isso automaticamente.
#             0           1       2         3

lanche = 'Hamburguer', 'Suco', 'Pizza', 'Pudim'
""" print (lanche)

print (lanche[1])

# sinal de menos na frente, começa a contar ao contrário
print (lanche[-2])

# o ultimo número não é considerado
print (lanche[1:3])

print (lanche [2:])

print (lanche [:2])

print (lanche [-2:]) """

""" for comida in lanche:
    print(f'Eu comi {comida}')

print (len (lanche))

for contador in range (0, len(lanche)):
    print (lanche[contador])

# para mostrar a posição tem essas duas formas:
for contador in range (0, len(lanche)):
    print (f'Vou comer {lanche[contador]} na posição {contador}')

for posicao, comida in enumerate(lanche):
    print (f'Vou comer {comida} na posição {posicao}') """

""" # colocar em ordem alfabética com o sorted, mas isso não altera a ordem original definitivamente, só mostra organizado
print (sorted (lanche))
print (lanche)

# somar tuplas, mostra primeiro uma  e depois cola a outra na frente
a = (0, 2, 4 , 6)
b = (1, 3, 5, 7)
c = a + b
print (c)

# altera a ordem:
a = (0, 2, 4 , 6, 0)
b = (1, 3, 5, 7)
c = b + a
print (c)

# metodo count conta quantas vezes aparece dentro da tupla o elemento entre parenteses
print (c.count(0)) """

# metodo index mostra a posição que se encontra o elemento entre parenteses dentro da tupla
# print (lanche)
# print (lanche.index('Pizza'))

a = 1, 2, 3, 4
b = 4, 5, 6 , 7
c = a + b
print (c)
# index mostra a primeira ocorrência do elemento entre parenteses
print (c.index(4))
# pode-se definir apartir de qual posição começar a procurar
# nesse caso, procurar o numero 4 apartir da posição 4
print (c.index(4, 4))

# para deletar uma tupla usar o comando del
# del (lanche)
# print (lanche)


