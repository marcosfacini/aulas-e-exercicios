# interactive help/ajuda interativa

# muda o prompt de comando para o help
# help()

# ja mostra direto a definição do que foi colocado entre parenteses
# help(print)

# outro jeito de obter ajuda
# print (input.__doc__)

# DOCSTRINGS são uma string que serve como documentação pra explicar a função ou objetivo de algo
# são 3 aspas duplas logo abaixo da linha do def
def contador(inicio, fim, passo):
    """Faz uma contagem e mostra na tela.
        INICIO = E o inicio da contagem
        FIM = E o final da contagem
        PASSO = E de quanto em quanto vai pular
        RETURN = sem retorno

        Funcao criada no Curso em Vídeo
    """
    cont = inicio
    while cont < fim:
        print (f'{cont}', end=' ')
        cont += passo 


# help(contador)

# PARAMETROS OPICIONAIS 
def somar(a, b, c=0):
    """
    Funcao de soma
    a = primeiro numero a ser somado
    b = segundo numero a ser somado
    c = terceiro nuúmero a ser somado é opcional, não é necessário declará-lo
    """
    s = a + b + c
    print (f'O resultado da soma é: {s}')


# help(somar)
# somar(2, 4, 6)

# dessa forma mesmo colocando apenas dois parametros, não dá erro, porque o terceiro elemnto recebe o zero
# somar (3, 6)

# poderia colocar os 3 parametros como opcionais, dessa forma o programa nao daria erro caso não fosse informado nenhum parametro
# def somar(a=0, b=0, c=0):

# AS VARIAVEIS PODEM SER GLOBAIS QUE FUNCIONAM EM TOD/O O PROGRAMA 
# OU PODEM SER VARIAVEIS LOCAIS QUE FUNCIONAM APENAS DENTRO DO DEF
# VARIAVEIS LOCAIS PODEM RECEBER O VALOR DA VARIAVEL GLOBAL COM O COMANDO CHAMADO: global

# RETORNANDO VALORES 
# o return serve para obter o valor(que você pode guardar em uma variavel) da função 
# serve tambem para finalizar a função semelhante ao break dos laços de repetição, 
# mas o return mas não  imprime/printa na tela o valor que obteve da função

def adição(n1=0, n2=0, n3=0):
    ad = n1 + n2 + n3
    return ad


""" resultado1 = adição(2, 4, 6)
resultado2 = adição(2, 3)
resultado3 = adição(7)
print (f'Os resultados das funções são: {resultado1}, {resultado2} e {resultado3}') """

# exemplo:
def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


""" n = int (input ('Digite um número: '))
print (f'O fatorial de {n} é {fatorial(n)}') """

""" f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print (f'Os resultados são {f1}, {f2} e {f3}') """

# usando o return para valores boleanos
def par(num=0):
    if num % 2 == 0:
        return True
    else:
        return False


num = int (input ('Digite um número: '))
# print (par(num))
if par(num):
    print (f'O {num} é par.')
else:
    print (f'O {num} é impar.')





