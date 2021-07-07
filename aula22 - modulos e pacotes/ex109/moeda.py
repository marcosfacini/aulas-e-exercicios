def aumentar(preco=0, porcentagem=0, change=False):
    mais = preco + (preco * porcentagem / 100)
    if change == False:
        return mais
    else:
        return moeda(mais)


def diminuir(preco=0, porcentagem=0, change=False):
    menos = preco - (preco * porcentagem / 100)
    if change == False:
        return menos
    else: 
        return moeda(menos)


def dobro(preco=0, change=False):
    dob = preco * 2
    if change == False:
        return dob
    else:
        return moeda(dob)


def metade(preco=0, change=False):
    met = preco / 2
    if change == False:
        return met
    else:
        return moeda(met)


def moeda(preco=0):
    formatado = str (f'R${preco:.2f}'.replace('.', ','))
    return formatado