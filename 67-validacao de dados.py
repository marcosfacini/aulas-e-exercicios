# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. 
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = str (input ('Digite M para Masculino e F para Feminino: ')).strip().upper()
while sexo != 'M' and sexo != 'F':
    sexo = str (input ('Letra Inválida.\nDigite M para Masculino e F para Feminino: ')).strip().upper()

if sexo == 'M':
    sexo = 'Masculino'    
else:
    sexo = 'Feminino'    

print (f'Sexo {sexo} registrado com sucesso.')

# colchetes no final faz pegar somente a primeira letra, caso se digite masculino, ele pega só o m e valida do mesmo jeito,
# mas existe o problema de a pessoa digitar macaco e ainda assim validar porque começou com a letra m
# sexo = str (input ('Digite M para Masculino e F para Feminino: ')).strip().upper()[0]
# nesse caso se valida com o operador not in que significa que a variavel sexo não começa com a letra M ou F
# while sexo not in 'MF':


