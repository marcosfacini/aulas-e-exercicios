def aumentar(preco=0, porcentagem=0):
    mais = preco + (preco * porcentagem / 100)
    return mais


def diminuir(preco=0, porcentagem=0):
    menos = preco - (preco * porcentagem / 100)
    return menos


def dobro(preco=0):
    return preco * 2


def metade(preco=0):
    return preco / 2


def moeda(preco=0):
    formatado = str (f'R${preco:.2f}'.replace('.', ','))
    return formatado