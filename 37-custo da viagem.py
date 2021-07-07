# Desenvolva um programa que pergunte a distância de uma viagem em Km, e Calcule o preço da passagem, 
# cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

km = float (input ('Quantos kilometros você vai viajar?: '))
if km <= 200:
    print (f'O preço da passagem é: {km * 0.5:.2f}')
else:
    print (f'O preço da passagem é {km * 0.45:.2f}')
