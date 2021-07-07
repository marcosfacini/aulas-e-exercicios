# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, 
# retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

# colocar a importação do modulo date somente dentro da função,
# faz com que o modulo só funcione dentro dela,
# porém o lado bom é que economiza memoria do programa

def voto(ano):
    from datetime import date
    anoatual = date.today().year
    if ano > anoatual - 16:
        return f'Com {anoatual - ano} anos o status é: NEGADO'
    elif ano < anoatual - 65:
        return f'Com {anoatual - ano} anos o status é: OPCIONAL'
    else:
        return f'Com {anoatual - ano} anos o status é: OBRIGATÓRIO'


birth = int (input ('Em que ano você nasceu?: ')) 
print (voto(birth))
