# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO

# usando o comando exit() para parar o programa caso o usuário digite o número errado
n1 = float (input ('Digite a primeira nota entre 0 e 10: '))
if n1 > 10:
    print ('Número inválido. Tente novamente.')
    exit()
n2 = float (input ('Digite a segunda nota entre 0 e 10: '))
if n2 > 10:
    print ('Número inválido. Tente novamente.')
    exit()
media = (n1 + n2) / 2
print (f'A média é: {media:.2f}')

if media < 5:
    print ('REPROVADO')
elif media == 5 or media <= 6.9:
    print ('RECUPERAÇÃO ')    
else:
    print ('APROVADO')       

# outro jeito de fazer, verificando só depois se a media passou de 20, ou seja se foi digitado dois numeros acima de 10
""" n1 = float (input ('Digite a primeira nota entre 0 e 10: '))
n2 = float (input ('Digite a segunda nota entre 0 e 10: '))
media = (n1 + n2) / 2
print (f'A média é {media:.2f})

if media < 5:
    print ('REPROVADO')
elif media == 5 or media <= 6.9:
    print ('RECUPERAÇÃO ')    
elif media >= 7 and media <= 10:
    print ('APROVADO')  
else:
    print ('Coloque valores entre 0 e 10')       """

# usando apenas os operadores matematicos, e tirando os operadores and e or
""" n1 = float (input ('Digite a primeira nota entre 0 e 10: '))
n2 = float (input ('Digite a segunda nota entre 0 e 10: '))
media = (n1 + n2) / 2
print (f'A média é {media:.2f}')

if media < 5:
    print ('REPROVADO')
elif media <= 6.9:
    print ('RECUPERAÇÃO ')    
elif media <= 10:
    print ('APROVADO')  
else:
    print ('Coloque valores entre 0 e 10')       """