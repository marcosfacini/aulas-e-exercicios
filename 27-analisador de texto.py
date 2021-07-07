# é possível já eliminar os espaços antes e depois desde o input
nome = str (input ('Digite o seu nome completo?: ')).strip()

# letras maiusculas:
print (f'Seu nome com letras maiusculas fica assim: {nome.upper()}')

# letras minusculas:
# print (f'Seu nome com letras minúsculas fica assim: {nome.lower()}')

# quantas letras tem sem considerar os espaços:
# esp = nome.replace(' ' , '')
# total = len(esp)
# print (f'Total de letras sem considerar os espaços: {total}')
# ou economizando variaveis:
# total = len(nome) - nome.count(' ')
# print (f'Total de letras sem espaço é: {total}')

# total de letras somente do primeiro nome:
# dividido = nome.split()
# result = (dividido [0])
# primeironome = len(result)
# print (f'Seu primeiro nome é {result} e tem {primeironome} letras.')
# ou economizando variaveis:
# o comando find vai mostrar em que carctere aparece o primeiro espaço
# total = nome.find(' ')
# print (f'Seu primeiro nome tem {total} letras')
# ou declarando a posição da lista direto no format:
# dividido = nome.split()
# print (f'Seu primeiro nome é {dividido [0]} e tem {len(dividido [0])} letras.')