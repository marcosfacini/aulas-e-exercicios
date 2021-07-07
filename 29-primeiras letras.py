# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".

# ja converti para maiuscula e separei a string logo no input
# quando se usa o split, não tem necessidade do strip, pq quando se divide a string ja se elimina os espaços
# metodos que ultilizam colchetes não funcionam no estilo format novo somente com a letra f no inicio
cid = str (input ('Qual é o nome da cidade?: ')).upper().split()
print ('Essa cidade começa com Santo?: {}'.format('SANTO' == cid[0]))
