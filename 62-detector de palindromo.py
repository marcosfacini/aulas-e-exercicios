# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

frase = str (input ('Digite uma frase: ')).replace(' ', '').lower()
invertida = frase[::-1]
if frase == invertida:
    print ('Essa frase é um palíndromo.')
else:
    print ('Essa frase não é um palíndromo.') 

# outro modo de fazer usando o for
""" frase = str (input ('Digite uma frase: ')).strip().upper()
separada = frase.split()
junta = ''.join(separada)
inverso = ''

for letra in range (len(junta)-1, -1, -1):
    inverso += junta[letra]
print (f'A frase: {frase} ao contrário fica: {inverso}')    

if inverso == junta:    
    print ('Temos um palíndromo')
else:
    print ('Essa frase não é um palíndromo.')     """
