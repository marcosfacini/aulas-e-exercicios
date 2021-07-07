import random
a1 = input ('Nome do primeiro aluno: ')
a2 = input ('Nome do segundo aluno: ')
a3 = input ('Nome do terceiro aluno: ')
a4 = input ('Nome do quarto aluno: ')
sorte = [a1, a2, a3, a4]
print (f'A ordem fica assim: {random.choices(sorte, k=4)}')

# comando shuffle só embaralha a lista mas não retorna nenhum valor, por isso não pode ser colocado direto no format da string
# from random import shuffle
# a1 = input ('Nome do primeiro aluno: ')
# a2 = input ('Nome do segundo aluno: ')
# a3 = input ('Nome do terceiro aluno: ')
# a4 = input ('Nome do quarto aluno: ')
# sorte = [a1, a2, a3, a4]
# shuffle(sorte)
# print (f'A ordem será: {sorte}')
