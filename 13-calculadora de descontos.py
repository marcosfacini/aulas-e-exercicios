prod = float (input ('Qual é o preço do produto?: R$'))
desc = float (input ('Qual é a porcentagem do desconto?: '))
porc = (prod * desc) / 100
total = prod - porc
sinal = '%'


print ('O produto que custava R${:.2f} na promoção de {:.0f}{} de desconto vai custar R${:.2f}'.format (prod, desc, sinal, total))

# poderia economizar uma variavel: (eliminando a variavel porc)
#prod = float (input ('Qual é o preço do produto?: R$'))
#desc = float (input ('Qual é a porcentagem do desconto?: '))
#total = prod - (prod * desc / 100)

#print ('O produto que custava R${:.2f} na promoção de {:.0f}{} de desconto vai custar R${:.2f}'.format (prod, desc, sinal, total))
