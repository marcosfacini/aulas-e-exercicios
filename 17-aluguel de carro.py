#qtd km?
#qtd dias?

#quanto eh o preço a pagar? sabendo que  custa 60reais por dia e o.15 por km rodado

dia = int (input ('Quantos dias você vai ficar com o carro?: '))
km = float (input ('Quantos kilômetros você vai rodar?: '))
total = (dia * 60) + (km * 0.15)

print ('Por {} dias e {:.1f}kms rodados, você irá pagar: R${:.2f}'.format(dia, km, total))