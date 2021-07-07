# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# - à vista dinheiro/cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço formal
# - 3x ou mais no cartão: 20% de juros

# cabeçalho feito de forma manual:
# print ('-=-' * 25 , '\33[34mLOJAS PYTHON\33[m' , '-=-' * 25)

# modo format {f'} não permite o uso de barra envertida '\' dentro dele.
# é necessário converter a cor na hora de declarar a variavel, antes de colocar a string dentro das chaves
# para formatar uma string dentro do modo format {f'} é necessarios colocar aspas duplas nela 
# frase = '\33[LOJAS PYTHON\33[m'
# print (f'{frase}')
print (f'{" LOJAS PYTHON ":=^100}')

valor_produto = float (input ('Qual é o valor do produto?: R$'))
condição = int (input ('''Digite a condição de pagamento: 
Digite 1 para pagamento à vista no dinheiro/cheque:
Digite 2 para pagamento no cartão: 
Digite 3 para pagamento em 2x no cartão: 
Digite 4 para pagamento em 3x ou mais no cartão: 
Sua escolha: '''))

# ou poderia apagar esse if e usar o elif do final
if condição != 1 and condição != 2 and condição != 3 and condição != 4:
    print ('Número inválido. Digite um número entre 1 e 4 ')
    exit()

if condição == 1:
        total = valor_produto - (valor_produto * 10 / 100)
        print (f'Um produto de R${valor_produto:.2f} com pagamento a vista/cheque fica: R${total:.2f}')
elif condição == 2:
    total = valor_produto - (valor_produto * 5 / 100)
    print (f'Um produto de R${valor_produto:.2f} com pagamento à vista no cartão fica: R${total:.2f}')
elif condição == 3:
    pag_mensal = valor_produto / 2
    print (f'Um produto de R${valor_produto:.2f} ficará no valor de 2x de R${pag_mensal:.2f} sem juros no cartão.')            
elif condição == 4:
    parcelas = int (input ('Em quantas parcelas?: '))
    if parcelas <= 2 or parcelas > 10:
        print ('Valor inválido. Digite um valor entre 1 a 10')
        exit()
    total = valor_produto + (valor_produto * 20 / 100)
    pag_mensal = total / parcelas
    print (f'Um produto de R${valor_produto:.2f} em {parcelas}x no cartão fica R${pag_mensal:.2f} por mês, num total de R$ {total:.2f}')    

# poderia trocar o primeiro if que barra se digitar o numero errado por um elif no final de tudo, que consideraria o numero 0
# elif condição == 0 or condição >4:
#   print ('Número inválido. Digite um número entre 1 e 4') 
#   exit()