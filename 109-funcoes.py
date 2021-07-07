""" # é possível esonder a função clicando na setinha ao lado da palavra def

# função simples
def linha():
    print ('=' * 30)


linha()
print ('Olá Mundo!')
linha()

# função com parametro que vai entre os parenteses
def cabecalho(txt):
    print ('-' * 30)
    print ('Hoje é dia:', txt)
    print ('-' * 30)


cabecalho('30/05/2021')
cabecalho('de praia!')

# funcao de soma
def soma(a, b):
    s = a + b
    print (s)


soma(1, 2)
soma(5,5) """

""" # é possível definir a ordem dos parametros
def soma(a, b):
    s = a + b
    print (s)


soma(a = 5, b = 4)
soma(a = 4, b = 5) """

# nao e necessario informar o numero total de paramentros
# pode-se usar o asterisco dentro do parenteses
""" def contador(* numero):
    print (numero)


contador(2, 4, 6, 8)
contador(1, 2, 3)
contador(5, 10, 15) """

# usando for dentro do def
""" def contador(* numero):
    for num in numero:
        print (num, end=' ')
    print ('FIM')


contador(2, 4, 6, 8)
contador(1, 2, 3)
contador(5, 10) """

# usando len() e print formatado dentro do def
""" def contador(* numeros):
    tamanho = len(numeros)
    print (f'O toral dos valores: {numeros} é: {tamanho}')


contador(2, 4, 6, 8)
contador(1, 2, 3)
contador(5, 10) """

# lista dentro do def
""" def dobrar(lista):
    posicao = 0
    while posicao < len(lista):
        lista[posicao] *= 2
        posicao += 1


valores = [2, 4, 6, 8]
dobrar(valores)
print (valores) """

# usando o desempacotamente com o asterisco dentro do parametro em parenteses
def soma(*numeros):
    s = 0
    for num in numeros:
        s += num
    print (s)


soma(2, 4, 6, 8)
soma(2,3, 5, 10, 20)






