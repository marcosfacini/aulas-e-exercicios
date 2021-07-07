# Crie um programa que tenha uma função fatorial() que receba dois parâmetros: 
# o primeiro que indique o número a calcular e outro chamado show, 
# que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

def fatorial(n, show=False):
    """
    Calcula o fatorial de um numero
    n = o numero a ser calculado o fatorial
    show = parametro opcional, quando True ele mostra a operação completa
    return = o resultado da fatoração
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print (c,end='')
            if c > 1:
                print (' x ', end='')
            else:
                print (' = ', end='')
        f *= c
    return f
    


# help(fatorial)

num = int (input ('Digite um número: '))
print (fatorial(num, show=True))

