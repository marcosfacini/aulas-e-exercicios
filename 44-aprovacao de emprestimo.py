# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

casa = float (input ('Qual é o valor da casa?: R$'))
sal = float (input ('Qual é o seu salário?: R$'))
ano = int (input ('Em quantos anos você vai pagar a casa?: '))
prest = (casa / ano) / 12
print (f'Para comprar uma casa no valor de R${casa:.2f} em {ano} anos, a prestação será de {prest:.2f}')
if prest > (sal * 30 / 100):
    print ('Seu empréstimo foi negado.')
else:
    print ('Parabéns! Seu empréstimo foi aprovado!')    