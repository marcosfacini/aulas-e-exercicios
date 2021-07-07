# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 'a função input() do Python, 
# só que fazendo a validação para aceitar apenas um valor numérico.
# Ex: n = leiaInt('Digite um n: ')

def leiaInt(texto):
    print (texto, end='')
    num = str (input ())
    while num.strip() == '':
        print ('\033[1;31mO número não foi digitado\33[m')
        print (texto, end='')
        num = str (input ())
    while num.isnumeric() == False:
        print ('\033[1;31mNúmero Inválido\33[m')
        print (texto, end='')
        num = str (input ())
    return num


n = leiaInt('Digite um número: ')
print (f'Você acabaou de digitar o número: {n}')
