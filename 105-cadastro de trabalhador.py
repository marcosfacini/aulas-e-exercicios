# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. 
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. 
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar. (35 anos trabalhados)

from datetime import date
info = {'Nome': input('Nome: '), 'Ano de nascimento': int(input('Ano de nascimento: ')),
        'Carteira de trabalho': int (input ('Carteira de trabalaho: (Digite 0 se não tiver): '))}
info['idade'] = date.today().year - info['Ano de nascimento']

if info['Carteira de trabalho'] == 0:
    for item in info:
        print (f'{item} = {info[item]}')

else:
    info['Ano de contratação'] = int (input ('Ano de contratação: '))
    info['Salário'] = float (input ('Salário: '))
    # ordem dos parenteses começa pelos de dentro para os de fora
    info['Vai se aposentar com:'] = info['idade'] + (35 - (date.today().year - info['Ano de contratação']))

    for item in info:
        print (f'{item} = {info[item]}')

