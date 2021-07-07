# faca um programa que leia algo pelo teclado
# e mostre na tela o seu tipo primitivo e todas as informações possiveis sobre ele

# todo input é uma string por padrão
n = input ('Digite algo: ')

print ('O tipo primitivo é: ' , type(n))
print ('E somente numeros?' , n.isnumeric())
print ('E somente letras?' , n.isalpha())
print ('Letras maiusculas?' , n.isupper())

# mesmo resultado com o format
#print ('E somente espaço? {}'.format (n.isspace()))
#print ('E alphanumerico? {}'.format (n.isalnum()))
#print ('E somente minusculas {}'.format (n.islower()))
#print ('Esta capitalizado/primeira letra maiuscula? {}'.format(n.istitle()))
