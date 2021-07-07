# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500.

# acumulador: soma cada novo número incluso no laço com o valor do anterior
# contador: soma apenas a quantidade de vezes que ocorre a operação dentro do if

acumulador = 0
contador = 0
for laço in range (1, 501, 2):
    if laço % 3 == 0:
        acumulador = acumulador + laço
        contador = contador + 1
print (f'A soma de todos os {contador} números solicitados é {acumulador}')

# acumulador fora do if irá terá outro resultado, nesse caso mais amplo, contando todos os números ímpares
# pode representar co  o operador += (vide arquivo 54 ultimo item)
acumulador = 0
contador = 0
for laço in range (1, 501, 2):
    if laço % 3 == 0:
        acumulador += laço
    contador += 1
print (f'A soma de todos os {contador} números solicitados é {acumulador}')
    