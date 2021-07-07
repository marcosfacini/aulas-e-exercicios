# break quebra o laço de repetição infinito sem precisar terminá-lo
# nesse caso o nuúmero 999 não entra na soma

soma = contador = 0
while True:
    numero = int (input ('Digite um número: (999 para parar:) '))
    if numero == 999:
        break
    soma += numero
    contador += 1

print (f'O resultado da soma desses {contador} é: {soma}')
