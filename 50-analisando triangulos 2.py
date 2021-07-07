# Refaça o arquivo 41 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - EQUILÁTERO: todos os lados iguais
# - ISÓSCELES: dois lados iguais, um diferente
# - ESCALENO: todos os lados diferentes

# usando o end= para colocar dois prints na mesma linha
print ('-=-' * 30)
print ('Analisando triângulos')
print ('-=-' * 30)
r1 = float (input ('Digite o tamanho da primeira reta: '))
r2 = float (input ('Digite o tamanho da segunda reta: '))
r3 = float (input ('Digite o tamanho da terceira reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os seguimentos acima podem formar um triângulo' , end=' ')
    if r1 == r2 and r2 == r3:
        print ('EQUILÁTERO')    
    elif r1 == r2 != r3 or r2 == r3 != r1 or r1 == r3 != r2:
        print ('ISÓSCELES')    
    else:
        print ('ESCALENO')    

else:
    print ('Os seguimentos a cima não podem formar um triângulo')     




