""" # contagem do range começa do zero e não contabiliza o ultimo número
for c in range (0 ,4):
    print('Olá Mundo!')

# por isso que nesse caso, só mostra o print 3 vezes em vez de 4:
for c in range (1 ,4):
    print('Olá Mundo!')   

# pode colocar mais de um comando dentro:
for c in range (0 ,3):
    print('Olá Mundo!') 
    print ('BYE!')    

# a variavel c vai realizar o comando seguido dela por 4 vezes
# a variavel c foi criada no momento do for
for c in range (0 ,4):
    print(c)     """

""" # ultima casa dentro do range mostra a ação, nesse caso contar de trás pra frente
for c in range (5 ,0, -1):
    print(c)

# ultima casa do range mostra a ação, nesse caso contar de dois em dois
for c in range (0 ,5, 2):
    print(c)

# uma variavel pode fazer parte do range
n = int (input ('Digite um número: '))
for c in range (1 , n):  
    print (c)   

# comando +1 depois da variável n acrescenta mais um número a contagem, 
# nesse caso levando até o número que foi unputado na variavel n
n = int (input ('Digite um número: '))
for c in range (1 , n+1):  
    print (c)       """

""" inicio = int (input ('Digite o número que vai iniciar a contagem: '))
fim = int (input ('Digite o número em que a contagem vai terminar: '))
pulos = int (input ('Digite de quantas em quantas casas você quer pular: '))
for c in range (inicio, fim+1, pulos):
    print (c)

# é possivel colocar um input dentro do for:
for c in range (0, 3):
    n = int (input ('Digite um número: '))
    print (n)   """  

# a variavel s começa valendo zero, mas a cada uma das repeições ela ganha o valor de n
s = 0
for c in range(0, 4):
    n = int (input ('Digite um número: '))
    s = s + n
print (f'A soma desses 4 números é: {s}') 

""" # o operador s += n tem o mesma função s = s + n
# significa que a variavel vai receber ela mesma, mais outro valor
s = 0
for c in range(0, 4):
    n = int (input ('Digite um número: '))
    s += n
print (f'A soma desses 4 números é: {s}')  """


