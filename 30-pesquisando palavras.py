# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
nome = str (input ('Digite seu nome completo: ')).upper().split()
print ('Esse nome contem o sobrenome Silva?: {}'.format("SILVA" in nome))

# ou informando o upper só no format:
# nome = str (input ('Digite seu nome completo: ')).split()
# print ('Esse nome contem o sobrenome Silva?: {}'.format("SILVA" in nome.upper()))
