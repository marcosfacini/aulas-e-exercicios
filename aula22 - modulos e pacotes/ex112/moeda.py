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


""" def resumo(preco, aumento, desconto):
    print (f'O preço analisado é: {moeda(preco)}')
    print (f'{moeda(preco)} com {aumento}% de aumento fica: {aumentar(preco, aumento, True)}')
    print (f'{moeda(preco)} com {desconto}% de desconto fica: {diminuir(preco, desconto, True)}')
    print (f'O dobro de {moeda(preco)} é: {dobro(preco, True)}')
    print (f'A metade de {moeda(preco)} é: {metade(preco, True)}') """

# outra maneira de formatar o print da def resumo()
def resumo(preco=0, aumento=0, desconto=0):
    print ('=' * 51)
    print (f'{"RESUMO DO VALOR":^50}')
    print ('=' * 51)
    print (f'{"Preço analisado:":<40} {moeda(preco):>10}')
    print (f'{"Com aumento:":<40} {aumentar(preco, aumento, True):>10}') # aumento e desconto nao aparece
    print (f'{"Com desconto:":<40} {diminuir(preco, desconto, True):>10}')
    print (f'{"Dobro do preço:":<40} {dobro(preco, True):>10}')
    print (f'{"Metade do preço:":<40} {metade(preco, True):>10}')
    print ('=' * 51)