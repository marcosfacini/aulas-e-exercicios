# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. 
# No final, mostre o conteúdo da estrutura na tela.
# abaixo d 5 reprovado/entre 5 e 7 recuperação/acima de 7 aprovado

nome = str (input ('Digite o nome do aluno: '))
media = float (input ('Digite a média do aluno: '))
status = {'nome': nome, 'media': media}

# ou poderia fazer direto dentro do dicionario
# status = {'Nome': input('Insira o nome do aluno: '), 'Média': float(input('Insira a média do aluno: '))}

# ou ir criando as keys:
# status = {}
# status['nome'] = str (input ('nome: '))
# status['media'] = float (input (f'Média de {status['aluno']}: '))

if media < 5:
    status['situação'] = 'Reprovado'
elif media == 5 or media <= 7:
    status['situação'] = 'Recuperação'
elif media > 7:
    status['situação'] = 'Aprovado'

for key, value in status.items():
    print (f'{key} = {value}')
