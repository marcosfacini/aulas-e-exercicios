# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. 
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

expressao = str (input ('Digite sua expressão: '))
duplas = []

for letra in expressao:
    if letra == '(':
        duplas.append('(')
    elif letra == ')':
        if len(duplas) > 0:
            duplas.pop()
        else:
            duplas.append(')')
            break
if len(duplas) == 0:
    print ('Sua expressão é válida.')
else:
    print ('Sua expressão é inválida.')