real = float (input('Quantos reais você quer converter? R$:'))
dolar = (real / 3.27)
euro = real / 6.77

print ('Com R${:.2f} reais você pode comprar US${:.2f} dólares.'.format(real, dolar))

print ('Com R${:.2f} reais você pode comprar E${:.2f} euros.'.format(real, euro))

# alterar o valor da variavel dolar conforme a cotação atual