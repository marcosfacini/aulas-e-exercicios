n = int (input ('Digite um número: '))

print ('O dobro de {} vale: {}'.format (n, n*2))
print ('O triplo de {} vale: {}'.format (n, n*3))
print ('A raiz quadrada de {} é igual a {:.2f}'.format (n, n**0.5))

# dois pontos seguido de ponto seguido de 2f dentro das chaves do .format
# indicam 2 casas decimais apos a virgula

#  meio pode ser indicado por 0.5 ou por (1/2)

# raiz quadrada com método pow()
#n = float (input ('Digite um número: '))

#rq = pow (n, (1/2))
#print ('A raiz quadrada de {} é: {}'.format (n, rq))
